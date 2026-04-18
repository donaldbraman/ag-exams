# Implementation Notes

## Research Loop ReAct Pattern

The `DrafterAgent` implements a text-based ReAct loop to bypass the lack of native tool-calling support in `auth-utils`.

### Parsing Mechanism
The agent uses regex to extract tool calls from the LLM's text response.
- **Pattern**: `re.search(r"Tool:\s*search\((.*?)\)", content, re.IGNORECASE)`
- **Argument Parsing**: Simple regex extraction for the `query` argument: `re.search(r"query=['\"](.*?)['\"]", args_str)`.

### Transition to Google Search
The search capability was pivoted from Tavily to **Google Custom Search API** to meet specific user requirements.
- **Dependency**: `google-api-python-client`
- **Configuration**: Requires `GOOGLE_API_KEY` and `GOOGLE_CSE_ID`.

## Technical Hurdles & Fixes

### 1. Undefined Type Hints (F821)
During implementation of the research loop, `ruff` identified `F821 Undefined name Provider` in `drafter.py`. 
- **The Issue**: The `Provider` type was used in a string forward reference (`provider: "Provider"`) in method signatures, but it was not imported or available in the module's scope.
- **Resolution**: The `Provider` type was imported from `write_assist.agents.models` to satisfy the type-hinting requirements in `drafter.py`.

### 2. Async Mocking for ReAct Loops
Testing multi-turn async agent interactions requires careful configuration of `AsyncMock`.
- **Side Effects**: When mocking the `LLMClient.chat` method, use `AsyncMock(side_effect=[Response1, Response2])`. This allows the mocked client to return a sequence of responses when awaited in multiple turns of the research loop.

### 3. Pre-commit Hook Strictness
The repository uses pre-commit hooks that block direct commits to `main` and enforce `ruff` checks.
- **Workaround**: Always develop in a branch via Git Worktree.
- **Linting Fixes**: Use `# noqa: ARG001` for pytest fixtures to satisfy `ruff`'s unused argument check.
