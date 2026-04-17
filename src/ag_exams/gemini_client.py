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
    model: str = "gemini-3.0-flash-preview",
    use_diskcache: bool = False,
    response_mime_type: str = "application/json",
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
    config = types.GenerateContentConfig(
        system_instruction=system_instruction if system_instruction else None,
        response_mime_type=response_mime_type,
    )

    response = await client.aio.models.generate_content(
        model=model,
        contents=prompt,
        config=config,
    )
    
    result = response.text

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
