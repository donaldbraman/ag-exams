# Research Phase Design (ReAct Pattern)

The `DrafterAgent` is being upgraded from a single-shot draft generator to an autonomous researcher using a text-based ReAct (Reasoning + Acting) loop.

## Motivation
The shared `auth-utils` library provides unified LLM client abstractions. Historically, it lacked native support for tool-calling/function-calling schemas (e.g., Anthropic's `tools` or OpenAI's `functions`). To provide research capabilities without modifying the shared library, `write-assist` implements a text-based ReAct pattern.

**Note on Native Tool Support (Jan 2026):** Recent updates to the `GoogleProvider` in `auth-utils` have fixed native tool support for Gemini models. While this enables a potential migration from ReAct to native function calling, it is subject to the **Mixed Tool Conflict** (400 error) if an agent attempts to use both `web_search` (grounding) and custom functions (like a local database fetch) in the same call. Migration should follow the **Single Tool Responsibility Pattern** to ensure stability.

## Implementation Details

### The ReAct Loop
Instead of a single message exchange, the `DrafterAgent` now follows a multi-turn conversation:
1. **Thought**: The agent analyzes the topic and decides what information is missing.
2. **Action**: The agent outputs a structured tool call in text (e.g., `Tool: search(query="legal precedent for...")`).
3. **Observation**: The system parses the text, executes the tool, and feeds the results back to the agent as a "User" message.
4. **Repeat**: Steps 1-3 continue until the agent announces it has sufficient information.
5. **Drafting**: The agent consumes the entire conversation history to produce the final structured JSON draft.

### Key Components
- **`BaseTool`**: An abstract base class in `src/write_assist/tools/base.py`.
- **`SearchTool`**: Implementation using `google-api-python-client` in `src/write_assist/tools/search.py`, leveraging the Google Custom Search API.
- **Parsing Logic**: The `DrafterAgent` parses the LLM's text output using regex to identify `Tool: search(...)` calls.

### Dependencies
- **Google Search**: Switched from Tavily to Google Custom Search API. Requires `GOOGLE_API_KEY` and `GOOGLE_CSE_ID` in environment.

### Source Prioritization
The `DrafterAgent` is designed to prioritize internal/local sources for maximum reliability:
1.  **Provided Source Materials**: Documents manually loaded by the user.
2.  **cite-assist Local DB**: Pre-fetched scholarship and relevant excerpts from the local academic database. This is the primary source for reliable academic citations. (See the **Legal Retrieval Infrastructure** KI for implementation and ModernBERT details).
3.  **Google Web Research**: Used to fill gaps, find recent cases, or identify seminal works not present in the local cache.

## Execution Flow
- **Phase 0 (Research)**: Multi-turn ReAct loop gathers external data.
- **Phase 1 (Drafting)**: Single message containing the gathered research and the original prompt instructions to generate the final JSON.

## Configuration Change
Model versions and API keys for search are moved to environmental configuration to allow for easier model upgrades (e.g., switching to newer Claude or GPT versions).
