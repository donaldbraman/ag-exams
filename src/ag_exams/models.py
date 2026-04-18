"""Data models for the exam generation pipeline.

Dataclasses for scenario briefs, question stubs, scenario packages,
critique results, fully-formed questions, and exam configuration.
All models are JSON-serializable via to_json/from_json methods.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[3]


def _load_brief(exam: str, scenario_dir: str) -> str:
    """Read a scenario brief from its canonical 00-brief.md location."""
    path = _REPO_ROOT / f"criminal-law/quiz-system/research/{exam}-build-2026/scenarios/{scenario_dir}/00-brief.md"
    try:
        return path.read_text()
    except FileNotFoundError:
        return f"**WARNING:** Missing brief at {path}"


# ---------------------------------------------------------------------------
# Scenario brief
# ---------------------------------------------------------------------------


@dataclass
class ScenarioBrief:
    """Scenario definition from the scenario map."""

    name: str  # e.g., "psilocybin"
    title: str  # e.g., "Psilocybin Operation"
    substantive_base: str  # e.g., "Possession, cultivation, distribution"
    inchoate_layers: list[str]  # e.g., ["accomplice", "conspiracy", "pinkerton", "rico"]
    defenses: list[str]  # e.g., ["duress", "mistake"]
    chapters: list[int]  # e.g., [10, 11, 15, 17, 18, 19, 20, 21]
    estimated_questions: tuple[int, int]  # e.g., (30, 40)
    stem_count: int  # e.g., 2
    brief_text: str  # Full scenario brief text for agent prompts
    statutes: str  # Federal statutes text provided to students


# ---------------------------------------------------------------------------
# Whiteboarding models
# ---------------------------------------------------------------------------


@dataclass
class QuestionStub:
    """Lightweight question stub from whiteboarding."""

    id: str  # e.g., "Q3"
    doctrine: str  # e.g., "pinkerton-liability"
    description: str  # e.g., "apply Pinkerton to C for A's weapon escalation"
    facts_referenced: list[int]  # e.g., [1, 5, 6]
    stem: int  # Which stem (1 or 2)
    status: str = "proposed"  # proposed | accepted | rejected | revised


@dataclass
class CharacterEntry:
    """Character in the scenario."""

    name: str
    role: str
    stems: list[int]
    doctrinal_target: str


@dataclass
class ScenarioPackage:
    """The evolving artifact passed between architect and critic rounds."""

    scenario_name: str
    facts: list[str]  # Numbered fact list
    characters: list[CharacterEntry]
    stubs: list[QuestionStub]
    doctrines_covered: list[str]
    boss_requests: list[str]  # Transition text between stems
    round_number: int = 0
    architect_confidence: int = 0
    critic_confidence: int = 0
    open_questions: list[str] = field(default_factory=list)

    def to_json(self) -> str:
        return json.dumps(self.__dict__, default=lambda o: o.__dict__, indent=2)

    @classmethod
    def from_json(cls, data: str) -> ScenarioPackage:
        d = json.loads(data)
        d["characters"] = [CharacterEntry(**c) for c in d.get("characters", [])]
        d["stubs"] = [QuestionStub(**s) for s in d.get("stubs", [])]
        return cls(**d)


# ---------------------------------------------------------------------------
# Critique result
# ---------------------------------------------------------------------------


@dataclass
class CritiqueResult:
    """Output from the critic agent."""

    status: str  # "ITERATE" or "CONVERGED"
    scenario_package: ScenarioPackage
    accepted_stubs: list[str]  # stub IDs
    rejected_stubs: list[dict]  # [{id, reason}]
    proposed_stubs: list[QuestionStub]
    fact_issues: list[dict]  # [{fact_number, issue, severity}]
    opportunities: list[str]  # Missed doctrinal testing opportunities
    confidence: int  # 1-10

    def to_json(self) -> str:
        return json.dumps(self.__dict__, default=lambda o: o.__dict__, indent=2)

    @classmethod
    def from_json(cls, data: str) -> CritiqueResult:
        d = json.loads(data)
        d["scenario_package"] = ScenarioPackage.from_json(json.dumps(d["scenario_package"]))
        d["proposed_stubs"] = [QuestionStub(**s) for s in d.get("proposed_stubs", [])]
        return cls(**d)


# ---------------------------------------------------------------------------
# Fully formed questions
# ---------------------------------------------------------------------------


@dataclass
class Question:
    """A fully formed MC question."""

    number: int
    stem_text: str
    options: list[dict]  # [{label: "a", text: "...", correct: bool}]
    answer: str  # e.g., "(b)"
    explanation: str
    tags: dict  # {chapters: [], topics: [], difficulty: str, cognitive: str}
    grounding: str = ""


@dataclass
class QuestionSet:
    """Output from the question writer."""

    scenario_name: str
    header_text: str  # Fact pattern + boss requests
    questions: list[Question]
    doctrines_covered: list[str]

    def to_json(self) -> str:
        return json.dumps(self.__dict__, default=lambda o: o.__dict__, indent=2)

    @classmethod
    def from_json(cls, data: str) -> QuestionSet:
        d = json.loads(data)
        d["questions"] = [Question(**q) for q in d.get("questions", [])]
        return cls(**d)


# ---------------------------------------------------------------------------
# Exam configuration and result
# ---------------------------------------------------------------------------


@dataclass
class ExamConfig:
    """Configuration for a full exam generation run."""

    scenarios: list[str]  # Scenario names to generate, or ["all"]
    target_questions: int = 100
    skip_grounding: bool = False
    skip_adversarial: bool = False
    dry_run: bool = False  # Stop after whiteboarding
    output_dir: str = "criminal-law/quiz-system/research/final-exam"
    # If True, skip the architect/critic whiteboarding loop and read an
    # existing {scenario_name}-scenario.md from output_dir. Used to iterate
    # on the writer/grounding/adversarial stages without re-generating a
    # good scenario package.
    reuse_whiteboard: bool = False
    # Serialized CoverageTracker state for continue-as-new
    tracker_state: str | None = None
    completed_scenarios: list[str] = field(default_factory=list)


@dataclass
class ExamResult:
    """Final output of the workflow."""

    exam_file: str  # Path to assembled exam
    total_questions: int
    scenarios_completed: list[str]
    coverage_report: dict  # From CoverageTracker
    gaps: list[str]  # Doctrines with weight >= 3 not covered


# ---------------------------------------------------------------------------
# Scenario map — all 7 scenarios from the exam blueprint
# ---------------------------------------------------------------------------

_PSILOCYBIN_STATUTES = """\
21 USC § 841 - unlawful to knowingly or intentionally cultivate, \
distribute, or possess with intent psilocybin
18 USC § 2 - accomplices punishable as principals
21 USC § 846 - attempt and conspiracy, same penalties, no overt act required
18 USC § 1962 - RICO (enterprise + pattern + conspiracy)\
"""

_PSILOCYBIN_BRIEF = """\
Two-stem psilocybin grow operation expanding into national distribution.

STEM 1 — THE LOCAL OPERATION
Frame: Your boss hands you a case file. A psilocybin grow operation was \
discovered in a residential basement.

Characters:
- Brother A (grower): Operates the grow. Possession + cultivation under §841.
- Brother B: Lives in house, vaguely aware. Constructive possession — \
awareness ≠ dominion?
- A's spouse: Knows, doesn't participate. Constructive possession, spousal \
issues.
- Roommate: Just moved in, hasn't been to basement. No knowledge defense, \
strict liability?
- Supplier: Sells grow lights, spores, fertilizer. Accomplice — purpose vs. \
knowledge (Gladstone).
- Local buyer: Purchases output. Possession of product, not premises.

Doctrinal coverage: Possession (Ch. 15), constructive possession (Jenkins, \
White), accomplice (Ch. 18), mistake/mens rea (Ch. 10), public welfare \
(Ch. 11).
Stem 1 ends: Brother A convicted, goes to prison.

STEM 2 — THE NATIONAL EXPANSION
Frame: Six months later, your boss calls you back in.

Characters:
- Brother B (now principal): Runs expanded operation. New conspiracy or \
always in?
- Brother A (in prison): Still communicating with B. Withdrawal while \
incarcerated? Pinkerton for B's actions?
- Business partner (phone): Planning national distribution. Conspiracy scope \
— hub-and-spoke vs. chain (Kotteakos).
- Supplier (continuing): Now supplying at scale. Mens rea changed? \
Profit-sharing = purpose?
- Courier: Transports between states. Accomplice to distribution, Pinkerton.
- Coerced participant: Threatened into helping. Duress — imminency, \
well-grounded fear (Ch. 21).

Fact progression: Texts between B and partner discussing distribution network. \
Partner sets up shell company and website — RICO enterprise? (Boyle). Deal \
goes wrong — courier assaults buyer — Pinkerton for A (in prison)? Courier \
claims B threatened his family — duress defense. RICO conspiracy under \
§1962(d) — Salinas breadth.

Doctrinal coverage: Conspiracy (Ch. 19), Pinkerton (Ch. 19), RICO (Ch. 20), \
accomplice at scale (Ch. 18), duress (Ch. 21), felony murder (Ch. 14), \
attempt/abandonment (Ch. 17), homicide grading (Ch. 12-13).\
"""

_MULTI_DEFENDANT_BRIEF = """\
Multi-defendant killing scenario with layered liability.

Homicide grading across multiple participants. Tests accomplice liability, \
conspiracy, Pinkerton reach-through, and attempt alongside substantive \
homicide charges. Defense theories include self-defense and provocation. \
Requires analysis of grading distinctions (murder vs. manslaughter) as \
applied to each defendant's role and mental state.\
"""

_DUTY_OMISSION_BRIEF = """\
Duty and omission death scenario.

A death resulting from failure to act. Tests causation, omission liability, \
and duty-to-act doctrines. Explores accomplice by omission and the necessity \
defense. Focuses on chapters covering actus reus, causation, and omissions.\
"""

_REGULATORY_BRIEF = """\
Regulatory and public welfare offense scenario.

Strict liability versus mens rea requirements in a regulatory context. Tests \
public welfare doctrine, mistake of fact and law defenses, and the boundaries \
of criminal liability without traditional mens rea. Draws on punishment \
theory, mens rea, and public welfare chapters.\
"""

_CHARGING_BRIEF = """\
Charging and plea scenario.

Statutory interpretation and charge selection exercise. Tests understanding of \
criminal code structure, charging decisions, and plea dynamics. Focuses on \
legality, proportionality, and statutory interpretation chapters.\
"""

_SELF_DEFENSE_BRIEF = """\
Self-defense scenario.

Homicide or assault charge with self-defense claim. Tests proportionality, \
duty to retreat, castle doctrine, and the reasonable belief standard. Explores \
the intersection of self-defense with imperfect self-defense and heat of \
passion. Focused on the self-defense chapter.\
"""

_GENERAL_KNOWLEDGE_BRIEF = """\
General knowledge questions (standalone, not fact-pattern-based).

Drawn from foundational chapters on punishment theory, procedural justice, \
and motivated cognition. Not framed as rulings — factual and theoretical \
statements. Generated closer to the existing quiz format rather than the \
scenario-based approach.\
"""

_CHEMISTRY_PROFESSOR_STEM_A_BRIEF = """\
Single-stem scenario: The Chemistry Professor — First Sale Sequence.

Inspiration: Breaking Bad (inspired-by only — not a direct plot lift).
Budget: 10 questions, single-doctrine-per-question bias.

FRAME: A tenured chemistry professor at a midwestern university receives a \
terminal pancreatic cancer diagnosis. Desperate for money to fund experimental \
treatment and leave something for a disabled child, the professor partners with \
a former undergraduate student to synthesize a controlled substance in a mobile \
lab. This single stem covers the first sale and a customer's overdose death.

CHARACTERS (writer assigns names from the name pool — setting should differ \
meaningfully from the inspiration source; different city, different cancer \
specifics):
- The chemistry professor (primary defendant): terminal diagnosis, financial \
desperation, novice to criminal enterprise.
- The ex-student partner: prior low-level drug record, provides the street \
infrastructure.
- The first customer (the victim): recreational user, overdoses on the \
inaugural batch.

REQUIRED PLOT BEATS:
1. A contaminated or unusually-potent first batch is sold to a single customer.
2. The customer uses the drug and begins to decompensate in the professor's \
presence (or shortly after, in a way that tests proximate cause).
3. The professor has a clear opportunity to call 911 and makes a choice.
4. The customer dies; a charging decision must distinguish between felony-murder, \
depraved-heart, and gross-negligence theories.

DOCTRINAL TARGETS (test across these 10 Qs):
- Ch 7 voluntary act / omissions (did the professor act or omit to summon help \
when the customer collapsed?)
- Ch 8 causation (but-for + proximate: intervening drug-use choices, \
contributory conditions, foreseeability)
- Ch 10 mistake of fact (professor's beliefs about batch purity)
- Ch 11 strict/public-welfare liability (controlled-substance distribution \
statutes)
- Ch 13 unintentional homicide (depraved-heart / reckless-indifference murder \
vs. gross-negligence manslaughter vs. ordinary negligence)
- Ch 14 felony-murder predicate analysis (is drug distribution a qualifying \
inherently-dangerous felony under the Ireland/merger analysis? agency vs. \
proximate-cause FM theories)

DISTRACTOR STRATEGY:
- Students confuse depraved-heart (extreme recklessness as to human life) with \
gross negligence (gross deviation from reasonable care) and with generic \
recklessness. Offer plausible-sounding but doctrinally wrong mens-rea labels.
- On FM, invite students to skip the merger/inherently-dangerous analysis.
- On causation, tempt students with "the customer chose to use" as a \
superseding cause when it isn't.

HARD EXCLUSIONS:
- No domestic violence or intimate-partner-violence content.
- No rape or sexual-assault content.
- No minors as customers or victims.
- No direct plot lifts from the inspiration source.
- No interstate/federal drug-conspiracy issues (keep jurisdiction single-state).
- No RICO or enterprise analysis.
- No accomplice-liability deep dive.\
"""

_MOCK_PROCEDURAL_BLOCK_BRIEF = """\
Single-stem scenario: The Fixer's Procedural Block.

Inspiration: Better Call Saul / Breaking Bad (inspired-by only — not a direct plot lift).
Budget: 6-8 questions, single-doctrine-per-question bias.

FRAME: Following the fallout of a massive narcotics ring (referencing the Chemistry Professor), the cartel's top lieutenant is facing trial. The organization's slick, morally bankrupt "criminal" lawyer is tasked with orchestrating a massive campaign of institutional corruption to keep the lieutenant out of prison.

CHARACTERS:
- The Fixer (Defense Attorney): A corrupt but brilliant attorney orchestrating the institutional manipulation.
- The Prosecutor (DA): An ambitious District Attorney making aggressive charging decisions.
- The Judge: A jaded trial judge susceptible to subtle blackmail or influence from the cartel.
- The Legislator: A corrupt state senator on the cartel's payroll.
- The Governor: A state executive willing to commute sentences or issue pardons for a massive cash bribe.

SUGGESTED PLOT DIRECTION:
The narrative should explore the boundaries of institutional law by featuring a mix of acts:
1. Some acts should clearly cross the legal line into outright corruption (e.g., explicit bribery, extortion).
2. Other acts should be shielded by the specific legal immunities, discretionary powers, or laws protecting the decisions made by persons in each of their respective institutions.
Let the characters interact organically to test these boundaries.

DOCTRINAL TARGETS (test across these Qs):
- Ch 4 Juries (voir dire, Batson challenges, jury nullification, right to a jury trial)
- Ch 5 Legislatures (statutory interpretation, ex post facto laws, executive pardon power limits)
- Ch 6 Prosecutors (prosecutorial discretion, charging decisions, vindictive prosecution, plea bargaining bounds)
"""

SCENARIO_MAP: dict[str, ScenarioBrief] = {
    "psilocybin": ScenarioBrief(
        name="psilocybin",
        title="Psilocybin Operation",
        substantive_base="Possession, cultivation, distribution",
        inchoate_layers=[
            "accomplice",
            "conspiracy",
            "pinkerton",
            "rico",
            "rico-conspiracy",
        ],
        defenses=["duress", "mistake"],
        chapters=[10, 11, 12, 13, 14, 15, 17, 18, 19, 20, 21],
        estimated_questions=(30, 40),
        stem_count=2,
        brief_text=_PSILOCYBIN_BRIEF,
        statutes=_PSILOCYBIN_STATUTES,
    ),
    "multi_defendant_killing": ScenarioBrief(
        name="multi_defendant_killing",
        title="Multi-Defendant Killing",
        substantive_base="Homicide grading",
        inchoate_layers=["accomplice", "conspiracy", "pinkerton", "attempt"],
        defenses=["self-defense", "provocation"],
        chapters=[12, 13, 14, 17, 18, 19, 22],
        estimated_questions=(15, 18),
        stem_count=1,
        brief_text=_MULTI_DEFENDANT_BRIEF,
        statutes="",
    ),
    "duty_omission": ScenarioBrief(
        name="duty_omission",
        title="Duty/Omission Death",
        substantive_base="Causation, omission liability",
        inchoate_layers=["accomplice-by-omission"],
        defenses=["necessity"],
        chapters=[7, 8, 9, 21],
        estimated_questions=(8, 10),
        stem_count=1,
        brief_text=_DUTY_OMISSION_BRIEF,
        statutes="",
    ),
    "regulatory": ScenarioBrief(
        name="regulatory",
        title="Regulatory/Public Welfare",
        substantive_base="Strict liability vs. mens rea",
        inchoate_layers=[],
        defenses=["mistake-of-fact", "mistake-of-law"],
        chapters=[1, 10, 11],
        estimated_questions=(6, 8),
        stem_count=1,
        brief_text=_REGULATORY_BRIEF,
        statutes="",
    ),
    "charging": ScenarioBrief(
        name="charging",
        title="Charging & Plea",
        substantive_base="Statutory interpretation, charge selection",
        inchoate_layers=[],
        defenses=[],
        chapters=[4, 5, 6],
        estimated_questions=(6, 8),
        stem_count=1,
        brief_text=_CHARGING_BRIEF,
        statutes="",
    ),
    "self_defense": ScenarioBrief(
        name="self_defense",
        title="Self-Defense",
        substantive_base="Homicide or assault",
        inchoate_layers=[],
        defenses=["self-defense", "proportionality", "retreat"],
        chapters=[22],
        estimated_questions=(6, 8),
        stem_count=1,
        brief_text=_SELF_DEFENSE_BRIEF,
        statutes="",
    ),
    "general_knowledge": ScenarioBrief(
        name="general_knowledge",
        title="General Knowledge",
        substantive_base="Foundational theory",
        inchoate_layers=[],
        defenses=[],
        chapters=[1, 2, 3],
        estimated_questions=(10, 12),
        stem_count=0,
        brief_text=_GENERAL_KNOWLEDGE_BRIEF,
        statutes="",
    ),
    "chemistry_professor_stem_a": ScenarioBrief(
        name="chemistry_professor_stem_a",
        title="The Chemistry Professor — First Sale",
        substantive_base="Unintentional homicide via drug distribution",
        inchoate_layers=[],
        defenses=[],
        chapters=[7, 8, 10, 11, 13, 14],
        estimated_questions=(10, 10),
        stem_count=1,
        brief_text=_CHEMISTRY_PROFESSOR_STEM_A_BRIEF,
        statutes="",
    ),
    "mock_procedural_block": ScenarioBrief(
        name="mock_procedural_block",
        title="Mock Procedural Block (Jury, Legislatures, Prosecutors)",
        substantive_base="Institutional law",
        inchoate_layers=[],
        defenses=[],
        chapters=[4, 5, 6],
        estimated_questions=(6, 8),
        stem_count=1,
        brief_text=_MOCK_PROCEDURAL_BLOCK_BRIEF,
        statutes="",
    ),
    "mock_defense_layer": ScenarioBrief(
        name="mock_defense_layer",
        title="Chemistry Professor Defense Layer — Self-Defense + Insanity",
        substantive_base="Self-defense and insanity doctrine",
        inchoate_layers=[],
        defenses=["self-defense", "insanity"],
        chapters=[22, 23],
        estimated_questions=(10, 10),
        stem_count=1,
        brief_text=_load_brief("mock", "06-defense-layer"),
        statutes="",
    ),
    "final_procedural_block": ScenarioBrief(
        name="final_procedural_block",
        title="Final Procedural Block (Jury, Legislatures, Prosecutors)",
        substantive_base="Institutional law",
        inchoate_layers=[],
        defenses=[],
        chapters=[4, 5, 6],
        estimated_questions=(6, 8),
        stem_count=0,
        brief_text=_load_brief("final", "05-procedural-block"),
        statutes="",
    ),
    "final_defense_layer": ScenarioBrief(
        name="final_defense_layer",
        title="Corner-Crew Defense Layer — Self-Defense + Insanity",
        substantive_base="Self-defense and insanity doctrine",
        inchoate_layers=[],
        defenses=["self-defense", "insanity"],
        chapters=[22, 23],
        estimated_questions=(10, 10),
        stem_count=1,
        brief_text=_load_brief("final", "06-defense-layer"),
        statutes="",
    ),
}
