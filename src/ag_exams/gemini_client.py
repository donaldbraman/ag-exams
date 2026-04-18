"""Gemini API client with context caching and disk caching for ag-exams."""

import hashlib
import json
import logging
import os
from pathlib import Path

from diskcache import Cache
from google import genai
from google.genai import types

from auth_utils.secrets import get_secret

logger = logging.getLogger(__name__)

CACHE_DIR = Path.home() / ".cache" / "ag-exams"
CACHE_VERSION = "v1"

_cache = Cache(str(CACHE_DIR))

def _get_client() -> genai.Client:
    """Return an authenticated Gemini client."""
    api_key = get_secret("google-api-key")
    return genai.Client(api_key=api_key)

def _compute_cache_key(prompt: str, system: str, model: str) -> str:
    """Compute SHA-256 cache key for the request."""
    raw = json.dumps({
        "prompt": prompt,
        "system": system,
        "model": model,
        "version": CACHE_VERSION
    }, sort_keys=True)
    return hashlib.sha256(raw.encode()).hexdigest()

async def dispatch_gemini(
    prompt: str,
    system_instruction: str = "",
    model: str = "gemini-3-pro-preview",
    use_diskcache: bool = False,
    response_mime_type: str = "text/plain",
) -> str:
    """Dispatch a request to Gemini, utilizing local diskcache if enabled."""
    client = _get_client()

    skip_cache = os.environ.get("EXAM_NO_CACHE", "").lower() in ("1", "true")
    if skip_cache:
        use_diskcache = False

    cache_key = ""
    if use_diskcache:
        cache_key = _compute_cache_key(prompt, system_instruction, model)
        cached = _cache.get(cache_key)
        if cached is not None:
            logger.info(f"Diskcache hit: {cache_key[:8]}")
            return cached

    logger.info(f"Dispatching to {model}...")

    # We use generate_content_async. 
    # If the user passes large contexts, they should ideally be in context caching, 
    # but for now we pass them in the prompt.
    # Configure safety settings to bypass filters for legal fact patterns
    safety_settings = [
        types.SafetySetting(category="HARM_CATEGORY_HATE_SPEECH", threshold="BLOCK_ONLY_HIGH"),
        types.SafetySetting(category="HARM_CATEGORY_DANGEROUS_CONTENT", threshold="BLOCK_ONLY_HIGH"),
        types.SafetySetting(category="HARM_CATEGORY_HARASSMENT", threshold="BLOCK_ONLY_HIGH"),
        types.SafetySetting(category="HARM_CATEGORY_SEXUALLY_EXPLICIT", threshold="BLOCK_ONLY_HIGH"),
    ]

    config = types.GenerateContentConfig(
        system_instruction=system_instruction if system_instruction else None,
        response_mime_type=response_mime_type,
        safety_settings=safety_settings,
    )

    import asyncio
    
    for attempt in range(3):
        try:
            response = await client.aio.models.generate_content(
                model=model,
                contents=prompt,
                config=config,
            )
        except Exception as e:
            if attempt < 2:
                logger.warning(f"HTTP/API Exception ({type(e).__name__}): {str(e)}. Retrying {attempt+1}/3...")
                await asyncio.sleep(2)
                continue
            logger.error(f"HTTP/API Exception in generate_content: {type(e).__name__}: {str(e)}")
            raise
        
        try:
            result = response.text
        except ValueError as e:
            finish_reason = getattr(response.candidates[0], "finish_reason", "UNKNOWN") if response.candidates else "UNKNOWN"
            if "MALFORMED_FUNCTION_CALL" in str(finish_reason):
                if attempt < 2:
                    logger.warning(f"Caught MALFORMED_FUNCTION_CALL. Retrying {attempt+1}/3...")
                    prompt += f"\n\n<!-- retry perturbation {attempt} -->"
                    await asyncio.sleep(2)
                    continue
            err_msg = f"Text extraction failed ({e}). Finish Reason: {finish_reason}. Raw prompt preview: {prompt[:100]}..."
            logger.error(err_msg)
            raise ValueError(err_msg)

        if not result:
            finish_reason = getattr(response.candidates[0], "finish_reason", "UNKNOWN") if response.candidates else "UNKNOWN"
            if "MALFORMED_FUNCTION_CALL" in str(finish_reason):
                if attempt < 2:
                    logger.warning(f"Caught MALFORMED_FUNCTION_CALL on empty string. Retrying {attempt+1}/3...")
                    prompt += f"\n\n<!-- retry perturbation {attempt} -->"
                    await asyncio.sleep(2)
                    continue
            err_msg = f"Empty string returned. Finish Reason: {finish_reason}. Raw prompt preview: {prompt[:100]}..."
            logger.error(err_msg)
            raise ValueError(err_msg)
            
        # If we got here, we succeeded
        break

    import time
    try:
        prompt_tokens = response.usage_metadata.prompt_token_count if response.usage_metadata else 0
        output_tokens = response.usage_metadata.candidates_token_count if response.usage_metadata else 0
        
        metrics_line = json.dumps({
            "timestamp": time.time(),
            "model": model,
            "prompt_tokens": prompt_tokens,
            "output_tokens": output_tokens,
        })
        with open(CACHE_DIR / "metrics.jsonl", "a") as f:
            f.write(metrics_line + "\n")
    except Exception as e:
        logger.warning(f"Failed to log metrics: {e}")

    if use_diskcache:
        _cache.set(cache_key, result)

    return result
