"""Per-stage model + cache lookup for the exam pipeline.

Activities call ``get_stage_config(stage)`` at dispatch time and use the
returned ``(model, cache)`` for their Gemini API invocation. The
config file is read fresh on every lookup (no caching), so edits to the YAML
take effect on the next stage without restarting the worker.

The default config lives at ``config/exam-models.yml`` and is a
project-level knob — trade cost against quality by flipping models or caching
levels there.

Override the active config file by setting the ``EXAM_MODEL_CONFIG`` env var
to an alternate path. Activities read the env var at each dispatch.
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_MODEL_CONFIG_PATH = REPO_ROOT / "config" / "exam-models.yml"


def _resolve_config_path() -> Path:
    """Return the active model-config path, honoring ``EXAM_MODEL_CONFIG``."""
    override = os.environ.get("EXAM_MODEL_CONFIG")
    if override:
        path = Path(override)
        if not path.is_absolute():
            path = REPO_ROOT / path
        return path
    return DEFAULT_MODEL_CONFIG_PATH


@dataclass(frozen=True)
class StageConfig:
    model: str
    cache: bool


def get_stage_config(stage: str) -> StageConfig:
    """Return the (model, cache) configured for ``stage``.

    Raises KeyError if the stage is missing from the config file, ValueError
    if the model is invalid, and FileNotFoundError if the config doesn't exist.
    """
    path = _resolve_config_path()
    if not path.exists():
        raise FileNotFoundError(
            f"Model config not found at {path}. "
            "The exam pipeline requires a stage-keyed config."
        )
    data = yaml.safe_load(path.read_text()) or {}
    stages = data.get("stages") or {}
    entry = stages.get(stage)
    if entry is None:
        raise KeyError(
            f"No entry for stage {stage!r} in {path}. "
            f"Known stages: {sorted(stages.keys())}"
        )
    
    model = entry.get("model")
    if not model or not model.startswith("gemini-"):
        raise ValueError(f"Stage {stage!r}: model {model!r} must start with 'gemini-'")
        
    cache = bool(entry.get("cache", False))
    return StageConfig(model=model, cache=cache)
