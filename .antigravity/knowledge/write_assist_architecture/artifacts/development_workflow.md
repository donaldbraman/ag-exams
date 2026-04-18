# write-assist Development Workflow

The project enforces strict development practices to support parallel agent execution and maintain code quality.

## Git Worktrees

**Mandatory Usage**: All development must happen in Git Worktrees. Direct commits to `main` are blocked by pre-commit hooks.
*   **Reasoning**: Enables multiple agents (or the human developer) to work on different features/phases in parallel without branch conflicts or shared state issues.
*   **Location Pattern**: `../write-assist-worktrees/<feature-name>`

### Common Commands
```bash
# Create worktree
git worktree add ../write-assist-worktrees/feat-name -b feat/feature-name

# Cleanup after merge
git worktree remove ../write-assist-worktrees/feat-name
git branch -d feat/feature-name
```

## Critical Rules

1.  **Hybrid Testing Strategy**:
    *   **Integration Tests**: Tests in `tests/` that verify full system behavior should use real data and LLM integrations.
    *   **Mocked Unit Tests**: Orchestration logic (like the ReAct loop in `DrafterAgent`) should be tested using `unittest.mock` and `AsyncMock` to ensure reliability and cost-efficiency without real API calls.
2.  **Tooling Execution**: Always use `uv run` (e.g., `uv run python`, `uv run pytest`).
3.  **No Temporary Commits**: Temporary scripts belong in the gitignored `temp/` directory.
4.  **Linting**: Run `uv run ruff check . && uv run ruff format .` before every commit.
    *   **Fixtures**: Use `# noqa: ARG001` to suppress "unused argument" errors for pytest fixtures that are required but not directly referenced in the test body.

## Agent Definitions
Agents are defined as Markdown instructions in `.claude/agents/`:
*   `drafter-agent.md`
*   `editor-agent.md`
*   `judge-agent.md`
