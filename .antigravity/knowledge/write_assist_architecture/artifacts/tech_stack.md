# write-assist Tech Stack

The project is built on modern Python tooling and integrates with a shared utility ecosystem.

## Core Language & Tooling
*   **Python**: >=3.11
*   **Package Manager**: `uv` (managed via `pyproject.toml` and `uv.lock`)
*   **Build System**: `hatchling`
*   **Linting/Formatting**: `ruff`

## Key Dependencies
*   **auth-utils**: A local, editable dependency (`../auth-utils`) providing LLM client abstractions.
*   **google-api-python-client**: Added to support the agentic research phase via the Google Custom Search API.
*   **httpx**: For asynchronous HTTP requests.
*   **pydantic**: For data validation and structured agent outputs. Note: Plans include moving to `pydantic-settings` for better configuration management.
*   **diskcache**: For local caching.
*   **tenacity**: For retry logic.
*   **click/rich**: For CLI interface and terminal formatting.

## Project Layout
*   `src/write_assist/`: Core package.
    *   `agents/`: Agent logic (Base, Drafter, Editor, Judge).
    *   `llm/`: Client re-exports from `auth-utils`.
    *   `pipeline/`: Orchestration logic.
    *   `tools/`: Agent tool implementations (e.g., SearchTool).
    *   `citations/`: Bluebook formatting.
*   `.claude/`: Agent instructions, skills (Bluebook), and shared guides.
