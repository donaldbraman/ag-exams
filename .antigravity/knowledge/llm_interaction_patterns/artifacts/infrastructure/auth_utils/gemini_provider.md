# Gemini Provider Implementation (auth-utils)

The `GoogleProvider` in the `auth-utils` library implements the interface for Google's Gemini models (e.g., `gemini-3-flash-preview`). 

## Technical Insights & Fixes

### 1. Tool Call Support in GenerateContent
A critical implementation detail was identified during the January 2026 refactor of the `criminal-law` pipeline. By default, the `google-genai` SDK requires tools to be explicitly passed within the `GenerateContentConfig` for they to be available to the model.

**The Fix (Verified Jan 2026):**
In `auth_utils/src/auth_utils/llm/providers/google.py`, ensure that any `tools` passed in via `**kwargs` (or `_kwargs`) are added to the `GenerateContentConfig` before calling the model. This fix has been successfully verified to enable native tool calling for Gemini-3 models, allowing agents to transition from text-based ReAct loops to native function calling.

```python
# Configure generation
config_kwargs = {
    "max_output_tokens": max_tokens,
    "temperature": temperature,
    "system_instruction": system_instruction,
}

# Add tools if provided (CRITICAL for Gemini support)
if "tools" in _kwargs and _kwargs["tools"]:
    config_kwargs["tools"] = _kwargs["tools"]

config = types.GenerateContentConfig(**config_kwargs)

# Use async client for generate_content
response = await self._client.aio.models.generate_content(
    model=self.model,
    contents=gemini_contents,
    config=config,
)
```

Without this explicit passing, the Gemini model will return a 404 error or a "tools is not supported" message if the agent configuration includes tool definitions (like `web_search`).

### 2. Provider Name
The internal provider name is `"gemini"`.

### 3. Model Compatibility
- Primary tested model: `gemini-3-flash-preview`.
- Requires `GOOGLE_API_KEY` in environment.

## Advanced Features & Pitfalls

### 4. Grounding Proofs
Gemini's web search capability (grounding) provides cryptographic and structural proof of non-hallucination.
- **Artifact Evidence**: Responses that successfully use grounding will contain `grounding_metadata` with `vertexaisearch` redirect links.
- **Verification**: These links serve as a provenance trail, confirming that the model retrieved information from live web sources rather than internal weights.

### 5. Google Scholar Access (Rate Limiting)
Direct fetching content from Google Scholar (e.g., using `web_fetch` or `requests.get`) frequently results in **429 Too Many Requests** errors, as Scholar strictly blocks automated bots. 
- **Polite Workaround**: Instead of fetching raw HTML, use Gemini's **Google Search Grounding** (`web_search` tool). The model can "read" search results and snippets to extract citations and IDs without triggering the bot protections that a direct HTTP request would encounter.

### 6. Mixed Tool Conflicts (400 Invalid Argument)
A significant error was identified when an agent (e.g., `research-verifier` or `document-retriever`) attempts to use both `web_fetch` and `web_search` simultaneously.
- **The Error**: `400 INVALID_ARGUMENT. {'error': {'code': 400, 'message': 'Tool use with function calling is unsupported', 'status': 'INVALID_ARGUMENT'}}`.
- **Root Cause**: There is a known conflict in some Gemini model versions when standard function calling (local tools like `web_fetch`) is mixed with server-side grounding (web search).
- **Verified Solution (Single Tool Responsibility Pattern)**: Restrict each agent to a single tool or a single category of tools. Specifically, do not mix server-side grounding (`web_search`) with client-side function calls (`web_fetch`) in the same model call. 
- **Data Flow Consequence**: If a step fails with this 400 error (e.g., `retrieve-documents`), subsequent steps (e.g., `edit-case`) may receive empty or default input, leading to severe hallucinations (e.g., the editor defaulting to *Palsgraf* when omission case research was expected). 
- **Validation**: This pattern was validated in the `criminal-law` project (Jan 2026). Specializing the `document-retriever` and `research-verifier` to use only `web_search` (grounding) resolved the 400 errors and successfully restored high-quality data flow (retrieving *State v. Lisa* instead of hallucinating *Palsgraf*).
