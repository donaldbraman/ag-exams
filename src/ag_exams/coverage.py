"""Smooth Weighted Round Robin (SWRR) coverage tracker for exam question generation.

Uses the NGINX SWRR algorithm to produce smooth, proportionally-weighted
doctrine selections for exam coverage. Weights are empirically derived from
block-level binary counting across casebook chapters + slide bonuses.

Algorithm (each selection round):
    1. For each doctrine i: current_weight[i] += static_weight[i]
    2. Select j = argmax(current_weight)
    3. current_weight[j] -= Total    (Total = sum of all static weights)
"""

from __future__ import annotations

import json
from pathlib import Path


class CoverageTracker:
    """Track exam question coverage across doctrines using SWRR scheduling.

    Args:
        doctrines: Mapping of doctrine names to their integer weights.
            Higher weights mean more questions should cover that doctrine.
    """

    def __init__(self, doctrines: dict[str, int]) -> None:
        if not doctrines:
            raise ValueError("doctrines must be a non-empty dict")
        self.static_weight: dict[str, int] = dict(doctrines)
        self.current_weight: dict[str, int] = dict.fromkeys(doctrines, 0)
        self.total: int = sum(doctrines.values())
        self.coverage: dict[str, int] = dict.fromkeys(doctrines, 0)

    def next_priorities(self, k: int) -> list[str]:
        """Run SWRR for k rounds, return ranked priority list.

        Args:
            k: Number of doctrine selections to produce.

        Returns:
            Ordered list of k doctrine names, selected proportionally
            to their weights via the SWRR algorithm.
        """
        selections: list[str] = []
        for _ in range(k):
            for d in self.current_weight:
                self.current_weight[d] += self.static_weight[d]
            best = max(self.current_weight, key=self.current_weight.get)  # type: ignore[arg-type]
            selections.append(best)
            self.current_weight[best] -= self.total
        return selections

    def record_coverage(self, doctrine: str, question_count: int = 1) -> None:
        """Record that a doctrine was covered by question_count questions.

        Updates both the coverage counter and the SWRR current weights
        so future selections account for already-covered doctrines.

        Args:
            doctrine: Name of the doctrine that was covered.
            question_count: Number of questions covering this doctrine.

        Raises:
            KeyError: If doctrine is not in the tracker.
        """
        if doctrine not in self.coverage:
            raise KeyError(f"Unknown doctrine: {doctrine!r}")
        self.coverage[doctrine] += question_count
        for _ in range(question_count):
            self.current_weight[doctrine] += self.static_weight[doctrine]
            self.current_weight[doctrine] -= self.total

    def is_complete(self, min_questions: int = 100, min_weight_threshold: int = 3) -> bool:
        """Check if coverage requirements are met.

        Coverage is complete when:
        - Total questions >= min_questions
        - All doctrines with weight >= min_weight_threshold have at least 1 question

        Args:
            min_questions: Minimum total questions required.
            min_weight_threshold: Minimum weight for a doctrine to require coverage.

        Returns:
            True if both conditions are satisfied.
        """
        total_qs = sum(self.coverage.values())
        high_covered = all(
            self.coverage[d] > 0 for d, w in self.static_weight.items() if w >= min_weight_threshold
        )
        return total_qs >= min_questions and high_covered

    def coverage_report(self) -> dict[str, dict[str, int]]:
        """Return a summary of coverage status for all doctrines.

        Returns:
            Dict keyed by doctrine name, each value containing:
            - weight: the static weight
            - covered: 1 if any questions cover it, 0 otherwise
            - questions: number of questions covering this doctrine

            Sorted by weight descending.
        """
        items = sorted(self.static_weight.items(), key=lambda x: x[1], reverse=True)
        return {
            d: {
                "weight": w,
                "covered": 1 if self.coverage[d] > 0 else 0,
                "questions": self.coverage[d],
            }
            for d, w in items
        }

    def uncovered_doctrines(self, min_weight: int = 1) -> list[str]:
        """Return doctrines with weight >= min_weight that have 0 coverage.

        Args:
            min_weight: Minimum weight threshold for inclusion.

        Returns:
            List of uncovered doctrine names, sorted by weight descending.
        """
        return [
            d
            for d, w in sorted(self.static_weight.items(), key=lambda x: x[1], reverse=True)
            if w >= min_weight and self.coverage[d] == 0
        ]

    def coverage_ratio(self) -> float:
        """Return fraction of weighted doctrines covered.

        Computes sum(weight for covered doctrines) / total weight.
        A doctrine counts as covered if it has at least 1 question.

        Returns:
            Float between 0.0 and 1.0.
        """
        if self.total == 0:
            return 0.0
        covered_weight = sum(w for d, w in self.static_weight.items() if self.coverage[d] > 0)
        return covered_weight / self.total

    def to_json(self) -> str:
        """Serialize tracker state to JSON string.

        Returns:
            JSON string containing static_weight, current_weight, and coverage.
        """
        return json.dumps(
            {
                "static_weight": self.static_weight,
                "current_weight": self.current_weight,
                "coverage": self.coverage,
            },
            indent=2,
        )

    @classmethod
    def from_json(cls, data: str) -> CoverageTracker:
        """Deserialize tracker from JSON string.

        Args:
            data: JSON string produced by to_json().

        Returns:
            Restored CoverageTracker with all state intact.
        """
        parsed = json.loads(data)
        tracker = cls(parsed["static_weight"])
        tracker.current_weight = parsed["current_weight"]
        tracker.coverage = parsed["coverage"]
        tracker.total = sum(parsed["static_weight"].values())
        return tracker


def load_chapter_map_weights(chapter_map_dir: str) -> dict[str, int]:
    """Load doctrine weights from v4 chapter map files.

    Reads all chapter-NN.md files from chapter_map_dir, extracts doctrine
    names from the Coverage Checklist table, and returns the merged dict.

    Args:
        chapter_map_dir: Path to directory containing chapter-NN.md map files.

    Returns:
        Dict mapping doctrine names to integer weights.

    Raises:
        NotImplementedError: Parser not yet implemented.
    """
    # TODO: Parse v4 markdown chapter maps. The Coverage Checklist table
    # in each chapter-NN.md contains doctrine names and practiced status.
    # See criminal-law/quiz-system/research/chapter-maps/ for the format.
    _ = Path(chapter_map_dir)  # validate path is constructible
    raise NotImplementedError(
        "Chapter map weight parser not yet implemented. "
        "See criminal-law/quiz-system/research/chapter-maps/ for v4 format."
    )
