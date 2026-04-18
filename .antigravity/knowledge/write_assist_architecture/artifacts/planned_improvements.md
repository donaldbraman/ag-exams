# write-assist Planned Improvements

Analysis of the codebase revealed several areas for architectural and functional enhancement, which are currently being addressed.

## 1. Implementation of Research Capabilities (COMPLETED)

**Gap Addressed**: The `DrafterAgent` now has a functional research phase using a text-based ReAct loop.
- **Tool-Use Loop**: Implemented in `DrafterAgent._research_loop` using a multi-turn conversation parsing the `Tool: search(...)` pattern.
- **Search Tool**: Implemented `SearchTool` using the Google Custom Search API, integrated with the agentic loop.
- **Improved Integration**: Research findings are gathered into a `research_context` and injected into the final drafting prompt.

## 2. Configuration & Flexibility

**Identified Gap**: LLM model versions (e.g., `claude-opus-4-5-20251101`) are hardcoded in `src/write_assist/agents/base.py`.

**Planned Solution**:
- Move provider-to-model mappings to a configuration file (`config.yaml`) or environment variables managed by `pydantic-settings`.

## 3. Testing Strategy Improvements (COMPLETED)

**Gap Addressed**: Unit tests for the research loop have been added to verify ReAct parsing and tool integration without real API calls.
- **Mocked Unit Tests**: `tests/test_research.py` uses `unittest.mock` to simulate LLM responses and search tool results.
- **Async Handling**: Tests were refined to correctly use `AsyncMock` for the LLM client's `chat` method, ensuring realistic simulation of async agent interactions.

## 4. GitHub Issue Tracking (COMPLETED)

GitHub issue #32 was used to track the "Implement Research Capabilities for DrafterAgent" task and has been closed.
