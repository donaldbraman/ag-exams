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


HARD EXCLUSIONS:
- No domestic violence or intimate-partner-violence content.
- No rape or sexual-assault content.
- No minors as customers or victims.
- No direct plot lifts from the inspiration source.
"""

_MULTI_DEFENDANT_BRIEF = """\
Multi-defendant killing scenario with layered liability.

Homicide grading across multiple participants. Tests accomplice liability, \
conspiracy, Pinkerton reach-through, and attempt alongside substantive \
homicide charges. Defense theories include self-defense and provocation. \
Requires analysis of grading distinctions (murder vs. manslaughter) as \
applied to each defendant's role and mental state.\


HARD EXCLUSIONS:
- No domestic violence or intimate-partner-violence content.
- No rape or sexual-assault content.
- No minors as customers or victims.
- No direct plot lifts from the inspiration source.
"""

_DUTY_OMISSION_BRIEF = """\
Duty and omission death scenario.

A death resulting from failure to act. Tests causation, omission liability, \
and duty-to-act doctrines. Explores accomplice by omission and the necessity \
defense. Focuses on chapters covering actus reus, causation, and omissions.\


HARD EXCLUSIONS:
- No domestic violence or intimate-partner-violence content.
- No rape or sexual-assault content.
- No minors as customers or victims.
- No direct plot lifts from the inspiration source.
"""

_REGULATORY_BRIEF = """\
Regulatory and public welfare offense scenario.

Strict liability versus mens rea requirements in a regulatory context. Tests \
public welfare doctrine, mistake of fact and law defenses, and the boundaries \
of criminal liability without traditional mens rea. Draws on punishment \
theory, mens rea, and public welfare chapters.\


HARD EXCLUSIONS:
- No domestic violence or intimate-partner-violence content.
- No rape or sexual-assault content.
- No minors as customers or victims.
- No direct plot lifts from the inspiration source.
"""

_CHARGING_BRIEF = """\
Charging and plea scenario.

Statutory interpretation and charge selection exercise. Tests understanding of \
criminal code structure, charging decisions, and plea dynamics. Focuses on \
legality, proportionality, and statutory interpretation chapters.\


HARD EXCLUSIONS:
- No domestic violence or intimate-partner-violence content.
- No rape or sexual-assault content.
- No minors as customers or victims.
- No direct plot lifts from the inspiration source.
"""

_SELF_DEFENSE_BRIEF = """\
Self-defense scenario.

Homicide or assault charge with self-defense claim. Tests proportionality, \
duty to retreat, castle doctrine, and the reasonable belief standard. Explores \
the intersection of self-defense with imperfect self-defense and heat of \
passion. Focused on the self-defense chapter.\


HARD EXCLUSIONS:
- No domestic violence or intimate-partner-violence content.
- No rape or sexual-assault content.
- No minors as customers or victims.
- No direct plot lifts from the inspiration source.
"""

_GENERAL_KNOWLEDGE_BRIEF = """\
General knowledge questions (standalone, not fact-pattern-based).

Drawn from foundational chapters on punishment theory, procedural justice, \
and motivated cognition. Not framed as rulings — factual and theoretical \
statements. Generated closer to the existing quiz format rather than the \
scenario-based approach.\


HARD EXCLUSIONS:
- No domestic violence or intimate-partner-violence content.
- No rape or sexual-assault content.
- No minors as customers or victims.
- No direct plot lifts from the inspiration source.
"""



_MOCK_THE_GENESIS_BRIEF = """\
Single-stem scenario: The Genesis (The Cook & The Product)

Inspiration: Breaking Bad (inspired-by only — not a direct plot lift).
Budget: 15 questions, single-doctrine-per-question bias.

FRAME: A tenured chemistry professor receives a terminal diagnosis. Desperate for money, the professor partners with a former student to synthesize a controlled substance. A miscalculation leads to an unintended chemical reaction injuring a lab assistant, and the professor inadvertently violates obscure public welfare regulations regarding chemical storage.

CHARACTERS:
- The Chemistry Professor: terminal diagnosis, financial desperation.
- The Ex-Student: provides street infrastructure.
- The Lab Assistant: injured by the chemical reaction.

SUGGESTED PLOT DIRECTION:
Focus on the act of synthesizing the product and the immediate fallout of the manufacturing process, rather than the distribution. Cover voluntary acts, causation of the injury, mistake of fact regarding the chemicals, and public welfare offenses regarding the unregistered lab.

DOCTRINAL TARGETS:
- Ch 7 voluntary act / omissions
- Ch 8 causation (but-for + proximate)
- Ch 10 mistake of fact / mistake of law
- Ch 11 strict/public-welfare liability

HARD EXCLUSIONS:
- No RICO or enterprise analysis.
- No domestic violence or sexual assault.
- No minors as victims.
"""

_MOCK_THE_DISTRIBUTION_RING_BRIEF = """\
Single-stem scenario: The Distribution Ring

Inspiration: Breaking Bad (inspired-by only — not a direct plot lift).
Budget: 15 questions, single-doctrine-per-question bias.

FRAME: The professor's former student takes over street-level distribution, recruiting three corner boys. The group forms an agreement to expand their territory. One boy attempts to sell to an undercover cop but abandons the effort. Another boy acts as a lookout during a stash house robbery where the principal unexpectedly commits a homicide.

CHARACTERS:
- The Ex-Student: the ringleader of the street distribution.
- Corner Boy 1: attempts a sale to a cop but gets cold feet.
- Corner Boy 2: acts as a lookout for a robbery that escalates into murder.
- Corner Boy 3: co-conspirator.

SUGGESTED PLOT DIRECTION:
Test the boundaries of inchoate crimes. Focus on the agreement to expand (Conspiracy), the abandoned sale (Attempt / Abandonment), and the lookout's liability for the unexpected homicide. You MUST force a comparative analysis of the lookout's liability under both the traditional "natural and probable consequences" doctrine AND the modern MPC/reform approach that rejects it (e.g., SB 1437). Likewise, test liability for a co-conspirator's acts under both Pinkerton doctrine and the MPC's rejection of it.

DOCTRINAL TARGETS:
- Ch 17 Attempts (substantial step, abandonment, impossibility)
- Ch 18 Accomplice Liability (mens rea, actus reus, natural and probable consequences vs. MPC reform)
- Ch 19 Conspiracy (agreement, overt act, withdrawal, Pinkerton vs. MPC rejection)

HARD EXCLUSIONS:
- No RICO or enterprise analysis.
- No domestic violence or intimate-partner-violence content.
- No rape or sexual-assault content.
- No minors as customers or victims.
- No direct plot lifts from the inspiration source.
"""

_MOCK_THE_EMPIRE_BUSINESS_BRIEF = """\
Single-stem scenario: The Empire Business

Inspiration: Breaking Bad / Better Call Saul (inspired-by only — not a direct plot lift).
Budget: 15 questions, single-doctrine-per-question bias.

FRAME: A massive, sophisticated logistics executive uses a chain of commercial businesses to distribute the product across state lines. The executive employs armed guards who mix guns with the drug trade. The operation operates as a highly structured enterprise. A lower-level enforcer is charged under § 922(g) (felon in possession) after a raid; there is factual ambiguity regarding whether the enforcer *knew* his prior conviction was a qualifying felony (testing *Rehaif*).

CHARACTERS:
- The Executive: calculating logistics mastermind.
- The Enforcer: uses firearms; prior ambiguous felony record.
- The Front Manager: manages the legitimate business masking the operation.

SUGGESTED PLOT DIRECTION:
Focus on enterprise liability and federal enhancements. The interaction between drug distribution (PWID) and firearm possession (924c) should be a focal point, alongside the structure of the RICO enterprise. Crucially, test the modern mens rea of status elements (*Rehaif*) by forcing students to connect mistake-of-law principles to the substantive § 922(g) gun offense.

DOCTRINAL TARGETS:
- Ch 10 Mens Rea of Status Elements (mistake of law, *Rehaif*)
- Ch 15 Drugs and Guns (constructive possession, PWID, 924c enhancements, 922g felon-in-possession)
- Ch 20 RICO and Enterprise Liability (pattern of racketeering, enterprise structure)

HARD EXCLUSIONS:
- No domestic violence or intimate-partner-violence content.
- No rape or sexual-assault content.
- No minors as customers or victims.
- No direct plot lifts from the inspiration source.
"""

_MOCK_THE_BLOWBACK_BRIEF = """\
Single-stem scenario: The Blowback (The Homicides)

Inspiration: Breaking Bad (inspired-by only — not a direct plot lift).
Budget: 15 questions, single-doctrine-per-question bias.

FRAME: The violence of the drug trade escalates. A rival distributor is intentionally poisoned with premeditation. A customer suffers a fatal overdose due to a highly concentrated batch. During a botched drug robbery, a fleeing driver strikes and kills a pedestrian.

CHARACTERS:
- The Rival: poisoned intentionally.
- The Customer: overdoses unintentionally.
- The Driver: causes a fatal accident fleeing a felony.

SUGGESTED PLOT DIRECTION:
Test the full spectrum of homicide grading. Distinguish between premeditated murder, extreme emotional disturbance, depraved-heart murder, and felony murder. 

DOCTRINAL TARGETS:
- Ch 12 Intentional Homicide (premeditation, EED, provocation)
- Ch 13 Unintentional Homicide (depraved-heart, gross negligence)
- Ch 14 Felony Murder / Misdemeanor Manslaughter (inherently dangerous, merger, agency vs proximate cause)


HARD EXCLUSIONS:
- No domestic violence or intimate-partner-violence content.
- No rape or sexual-assault content.
- No minors as customers or victims.
- No direct plot lifts from the inspiration source.
"""

_MOCK_THE_CORNERED_DEFENSES_BRIEF = """\
Single-stem scenario: The Cornered Defenses

Inspiration: Breaking Bad / Better Call Saul (inspired-by only — not a direct plot lift).
Budget: 15 questions, single-doctrine-per-question bias.

FRAME: Characters in the criminal underworld are backed into corners. A low-level cook is violently coerced by a cartel lieutenant into destroying a massive shipment of volatile precursor chemicals to prevent them from detonating and destroying a city block. The cook's actions support both a Necessity (justification) and a Duress (excuse) defense. Later, a traumatized bodyguard suffers a psychotic break during a raid, and a dealer shoots a rival claiming self-defense.

CHARACTERS:
- The Coerced Cook: forced to destroy property to prevent greater harm.
- The Traumatized Bodyguard: suffers a break from reality.
- The Cornered Dealer: uses deadly force in alleged self-defense.

SUGGESTED PLOT DIRECTION:
Focus heavily on affirmative defenses. You MUST force a rigorous analysis of the theory behind defenses by having students identify why the cook's actions could be pled as Necessity (a justified act that was right) versus Duress (an excused act lacking responsibility), and how the legal consequences for an accomplice would differ depending on which theory prevails. Also test the imminence requirement in self-defense, and the cognitive/volitional prongs of the insanity defense.

DOCTRINAL TARGETS:
- Ch 21 Necessity (Justification) and Duress (Excuse)
- Ch 22 Self-Defense (imminence, duty to retreat, imperfect self-defense)
- Ch 23 The Insanity Defense (M'Naghten, MPC, irresistible impulse)

HARD EXCLUSIONS:
- No domestic violence or intimate-partner-violence content.
- No rape or sexual-assault content.
- No minors as customers or victims.
- No direct plot lifts from the inspiration source.
"""

_MOCK_PROCEDURAL_BLOCK_BRIEF = """\
Single-stem scenario: The Procedural Block (The Fix)

Inspiration: Better Call Saul / Breaking Bad (inspired-by only — not a direct plot lift).
Budget: 15 questions, single-doctrine-per-question bias.

FRAME: Following the raid on Apex Freight, CEO Marcus Vance is facing a massive federal RICO trial. Vance's slick, morally bankrupt defense attorney, "The Fixer," orchestrates a campaign of institutional corruption to save Vance's empire. The trial Judge accepts a $50,000 "thank you" gift from Vance three weeks after unexpectedly suppressing key evidence, raising questions about bribery versus gratuities. In the jury room, a rogue juror admits to convicting a lower-level minority co-defendant purely out of racial animus. Finally, Vance secures a highly controversial, blanket pardon from the state's Governor in exchange for a massive super PAC donation.

CHARACTERS:
- Marcus Vance: Trial defendant and CEO orchestrating the legal manipulation.
- The Fixer (Defense Attorney): Orchestrates the strategic corruption.
- The Judge: Trial judge whose post-ruling financial windfalls test corruption statutes.
- The Rogue Juror: Tests the limits of jury secrecy and the Peña-Rodriguez exception.
- The Governor: Issues a plenary pardon testing executive power limits.

SUGGESTED PLOT DIRECTION:
Test the boundaries of institutional law and corruption. For the Judge and Governor, force students to apply recent Supreme Court public corruption precedent (Snyder's bribe vs. gratuity distinction, Skilling's honest services fraud, and McDonnell's official acts). For the Juror, test the clash between FRE 606(b) jury secrecy (Tanner) and constitutional racial bias exceptions. For the Governor, test the absolute nature of executive clemency despite corrupt motives.

DOCTRINAL TARGETS:
- Ch 4 Juries (Batson challenges, jury secrecy, Peña-Rodriguez racial bias exception)
- Ch 5 Legislatures & Courts (executive pardon power, Snyder bribe vs gratuity, Skilling honest services fraud, McDonnell official acts)
- Ch 6 Prosecutors (selective prosecution, prosecutorial immunity)

HARD EXCLUSIONS:
- No domestic violence or intimate-partner-violence content.
- No rape or sexual-assault content.
- No minors as customers or victims.
- No direct plot lifts from the inspiration source.
"""


_FINAL_THE_GENESIS_BRIEF = """\
Single-stem scenario: The Genesis (The Stash House Fire)

Inspiration: Generalized Organized Crime
Budget: 15 questions, single-doctrine-per-question bias.

FRAME: An underground drug organization operates out of low-income high-rises. A mid-level manager stores a highly volatile cutting agent in an unregistered warehouse, inadvertently violating strict public welfare laws. When a worker mistakenly handles the substance, a chemical fire breaks out, causing severe injuries.

CHARACTERS:
- Arthur: The CEO who oversees the entire organized operation.
- Brenda: The Logistics Manager who runs the stash house.
- Charles: The Worker injured by the volatile chemicals.
- David: The Chemical Supplier who sold the cutting agent.
- Elena: The Inspector who investigates the unregistered site.

SUGGESTED PLOT DIRECTION:
Focus on the act of storing and mixing the product. Cover voluntary acts, causation of the fire/injury, mistake of fact regarding the chemical's properties, and public welfare offenses regarding the unregistered warehouse.

DOCTRINAL TARGETS:
- Ch 7 voluntary act / omissions
- Ch 8 causation (but-for + proximate)
- Ch 10 mistake of fact / mistake of law
- Ch 11 strict/public-welfare liability

HARD EXCLUSIONS:
- No domestic violence or intimate-partner-violence content.
- No rape or sexual-assault content.
- No minors as customers or victims.
"""

_FINAL_THE_DISTRIBUTION_RING_BRIEF = """\
Single-stem scenario: The Distribution Ring (The Turf Defense)

Inspiration: Generalized Street-Level Drug Network
Budget: 15 questions, single-doctrine-per-question bias.

FRAME: A crew of street-level dealers runs a sophisticated hand-to-hand distribution network in a courtyard. They form an agreement to defend their turf from a rival crew. One dealer attempts a drive-by shooting but misses entirely. Another acts as a lookout during a stash house robbery where the principal unexpectedly commits a homicide.

CHARACTERS:
- Felix: The Crew Chief who organizes the turf defense.
- George: The Shooter who attempts the drive-by.
- Helen: The Lookout who aids the stash house robbery.
- Ian: The Enforcer who commits the unexpected homicide during the robbery.

SUGGESTED PLOT DIRECTION:
Test the boundaries of inchoate crimes. Focus on the agreement to defend the turf (Conspiracy), the missed drive-by (Attempt / Impossibility), and the lookout's liability for the unexpected homicide. You MUST force a comparative analysis of the lookout's liability under both the traditional "natural and probable consequences" doctrine AND the modern MPC/reform approach that rejects it (e.g., SB 1437). Likewise, test liability for a co-conspirator's acts under both Pinkerton doctrine and the MPC's rejection of it.

DOCTRINAL TARGETS:
- Ch 17 Attempts (substantial step, abandonment, impossibility)
- Ch 18 Accomplice Liability (mens rea, actus reus, natural and probable consequences vs. MPC reform)
- Ch 19 Conspiracy (agreement, overt act, withdrawal, Pinkerton vs. MPC rejection)

HARD EXCLUSIONS:
- No domestic violence or intimate-partner-violence content.
- No rape or sexual-assault content.
- No minors as customers or victims.
"""

_FINAL_THE_EMPIRE_BUSINESS_BRIEF = """\
Single-stem scenario: The Empire Business (The Waste Management Front)

Inspiration: Generalized Organized Crime Syndicate
Budget: 15 questions, single-doctrine-per-question bias.

FRAME: A powerful organized crime family uses a waste management business as a front for their illicit activities. The family engages in a pattern of racketeering, including extortion and large-scale interstate drug distribution. The family employs operatives who carry unregistered firearms. A capo is charged under § 922(g) (felon in possession) after a federal wiretap; there is factual ambiguity regarding whether the capo *knew* his prior conviction qualified as a felony (testing *Rehaif*).

CHARACTERS:
- Jack: The Boss, head of the crime family.
- Kevin: The Capo who manages the street-level crews; has a prior ambiguous felony record.
- Laura: The Dispatcher who runs the legitimate waste management business front.
- Matthew: The Victim targeted for extortion by the family.

SUGGESTED PLOT DIRECTION:
Focus on enterprise liability and federal enhancements. The interaction between massive drug distribution/extortion and firearm possession (924c) should be a focal point, alongside the structure and predicates of the RICO enterprise. Crucially, test the modern mens rea of status elements (*Rehaif*) by forcing students to connect mistake-of-law principles to the substantive § 922(g) gun offense.

DOCTRINAL TARGETS:
- Ch 10 Mens Rea of Status Elements (mistake of law, *Rehaif*)
- Ch 15 Drugs and Guns (constructive possession, PWID, 924c enhancements, 922g felon-in-possession)
- Ch 20 RICO and Enterprise Liability (pattern of racketeering, enterprise structure)

HARD EXCLUSIONS:
- No domestic violence or intimate-partner-violence content.
- No rape or sexual-assault content.
- No minors as customers or victims.
"""

_FINAL_THE_BLOWBACK_BRIEF = """\
Single-stem scenario: The Blowback (The Informant Homicides)

Inspiration: Generalized Organized Crime Syndicate
Budget: 15 questions, single-doctrine-per-question bias.

FRAME: Paranoia sweeps the crime family as they suspect an informant in their ranks. A Capo lures the suspected informant onto a boat and intentionally shoots him (premeditated). Meanwhile, a low-level associate recklessly disposes of toxic waste in a residential area, resulting in a civilian's death. Finally, during a botched hijacking of a commercial truck, a fleeing associate's vehicle strikes and kills a bystander.

CHARACTERS:
- Nora: The Capo who executes the suspected informant.
- Oscar: The Associate who is legally reckless with the toxic waste disposal.
- Penelope: The Hijacker whose fleeing vehicle causes the fatal crash.
- Quinn: The Getaway Driver who assists Penelope in fleeing the hijacking.
- Rachel: The Suspected Informant who is lured to the boat and killed.

SUGGESTED PLOT DIRECTION:
Test homicide grading. Distinguish between premeditated murder, depraved-heart murder, and felony murder during the flight from a felony.

DOCTRINAL TARGETS:
- Ch 12 Intentional Homicide (premeditation, EED, provocation)
- Ch 13 Unintentional Homicide (depraved-heart, gross negligence)
- Ch 14 Felony Murder / Misdemeanor Manslaughter (inherently dangerous, merger, agency vs proximate cause)

HARD EXCLUSIONS:
- No domestic violence or intimate-partner-violence content.
- No rape or sexual-assault content.
- No minors as customers or victims.
"""

_FINAL_PROCEDURAL_BLOCK_BRIEF = """\
Single-stem scenario: The Procedural Block (The Pardon)

Inspiration: Generalized Organized Crime / Corruption
Budget: 15 questions, single-doctrine-per-question bias.

FRAME: Following a massive federal wiretap on a waste management front, a top Capo is facing a federal RICO trial. The Capo's slick defense attorney orchestrates a campaign of institutional corruption to save the Capo. The trial Judge accepts a $50,000 "thank you" gift from the Capo three weeks after unexpectedly suppressing key evidence, raising questions about bribery versus gratuities. In the jury room, a rogue juror admits to convicting a lower-level minority co-defendant purely out of racial animus. Finally, the Capo secures a highly controversial, blanket pardon from the state's Governor in exchange for a massive super PAC donation.

CHARACTERS:
- Kevin: The Trial Defendant and Capo, facing federal RICO charges.
- Steve: The Defense Attorney who orchestrates the strategic corruption.
- Thomas: The Trial Judge whose post-ruling windfalls test corruption statutes.
- Ursula: The Rogue Juror whose actions test the limits of jury secrecy.
- Victor: The Governor who issues a plenary pardon.

SUGGESTED PLOT DIRECTION:
Test the boundaries of institutional law and corruption. For the Judge and Governor, force students to apply recent Supreme Court public corruption precedent (Snyder's bribe vs. gratuity distinction, Skilling's honest services fraud, and McDonnell's official acts). For the Juror, test the clash between FRE 606(b) jury secrecy (Tanner) and constitutional racial bias exceptions. For the Governor, test the absolute nature of executive clemency despite corrupt motives.

DOCTRINAL TARGETS:
- Ch 4 Juries (Batson challenges, jury secrecy, Peña-Rodriguez racial bias exception)
- Ch 5 Legislatures & Courts (executive pardon power, Snyder bribe vs gratuity, Skilling honest services fraud, McDonnell official acts)
- Ch 6 Prosecutors (selective prosecution, prosecutorial immunity)

HARD EXCLUSIONS:
- No domestic violence or intimate-partner-violence content.
- No rape or sexual-assault content.
- No minors as customers or victims.
"""

_FINAL_HAMSTERDAM_BRIEF = """\
Single-stem scenario: Hamsterdam (The Free Zone)

Inspiration: Police Corruption / Drug Zones
Budget: 15 questions, single-doctrine-per-question bias.

FRAME: A rogue Police Major claims that the only way to save the city from rampant violence is to create a secret, localized, police-sanctioned "free zone" where drug dealing is informally legalized. Inside the zone, a drug dealer must violently defend his stash against an armed stick-up robber. The incident escalates when the robber, suffering a psychological break from severe drug intoxication, commits a subsequent offense. The entire arrangement ultimately triggers a federal investigation into whether the rogue police department faction constitutes a corrupt RICO enterprise.

CHARACTERS:
- William: The Police Major who creates the illegal drug zone and asserts a Necessity defense.
- Xavier: The Dealer operating inside the zone who must claim Self-Defense.
- Yasmin: The armed Robber who tests the Insanity defense due to voluntary intoxication.

SUGGESTED PLOT DIRECTION:
Focus on the policy rationales of punishment and affirmative defenses. Force students to weigh the utilitarian "What We Punish" goals behind William's decision to legalize the zone. Then, analyze William's criminal liability under the Necessity (Choice of Evils) defense. Inside the zone, rigorously test Xavier's claim of Self-Defense (imminence, duty to retreat) against Yasmin's robbery. Finally, analyze Yasmin's liability through the lens of Insanity (M'Naghten vs. MPC) and voluntary intoxication.

DOCTRINAL TARGETS:
- Ch 3 What We Punish (deterrence, incapacitation vs. retributivism)
- Ch 21 Necessity (Justification)
- Ch 22 Self-Defense (imminence, duty to retreat, imperfect self-defense)
- Ch 23 The Insanity Defense (M'Naghten, MPC, irresistible impulse)
- Ch 20 RICO (Official misconduct and enterprise structure)

HARD EXCLUSIONS:
- No domestic violence or intimate-partner-violence content.
- No rape or sexual-assault content.
- No minors as customers or victims.
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
        chapters=[7, 8, 9, 21, 18],
        estimated_questions=(10, 15),
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
        estimated_questions=(10, 15),
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
        estimated_questions=(10, 15),
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
        estimated_questions=(10, 15),
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
        estimated_questions=(15, 20),
        stem_count=0,
        brief_text=_GENERAL_KNOWLEDGE_BRIEF,
        statutes="",
    ),

    "mock_the_genesis": ScenarioBrief(
        name="mock_the_genesis",
        title="Mock: The Genesis (The Cook & The Product)",
        substantive_base="Actus Reus, Causation, Strict Liability",
        inchoate_layers=[],
        defenses=["mistake-of-fact", "mistake-of-law"],
        chapters=[7, 8, 10, 11],
        estimated_questions=(10, 15),
        stem_count=1,
        brief_text=_MOCK_THE_GENESIS_BRIEF,
        statutes="",
    ),
    "mock_the_distribution_ring": ScenarioBrief(
        name="mock_the_distribution_ring",
        title="Mock: The Distribution Ring",
        substantive_base="Inchoate Crimes",
        inchoate_layers=["attempt", "accomplice", "conspiracy", "pinkerton"],
        defenses=["abandonment"],
        chapters=[17, 18, 19],
        estimated_questions=(10, 15),
        stem_count=1,
        brief_text=_MOCK_THE_DISTRIBUTION_RING_BRIEF,
        statutes="",
    ),
    "mock_the_empire_business": ScenarioBrief(
        name="mock_the_empire_business",
        title="Mock: The Empire Business",
        substantive_base="Drugs, Guns, and RICO",
        inchoate_layers=["rico", "rico-conspiracy"],
        defenses=[],
        chapters=[15, 20, 10],
        estimated_questions=(10, 15),
        stem_count=1,
        brief_text=_MOCK_THE_EMPIRE_BUSINESS_BRIEF,
        statutes="",
    ),
    "mock_the_blowback": ScenarioBrief(
        name="mock_the_blowback",
        title="Mock: The Blowback (Homicides)",
        substantive_base="Homicide Grading",
        inchoate_layers=[],
        defenses=["provocation", "eed"],
        chapters=[12, 13, 14],
        estimated_questions=(10, 15),
        stem_count=1,
        brief_text=_MOCK_THE_BLOWBACK_BRIEF,
        statutes="",
    ),
    "mock_procedural_block": ScenarioBrief(
        name="mock_procedural_block",
        title="Mock: The Fixer's Defense (Procedural Block)",
        substantive_base="Institutional law",
        inchoate_layers=[],
        defenses=[],
        chapters=[4, 5, 6, 2, 3],
        estimated_questions=(10, 15),
        stem_count=1,
        brief_text=_MOCK_PROCEDURAL_BLOCK_BRIEF,
        statutes="",
    ),
    "mock_the_cornered_defenses": ScenarioBrief(
        name="mock_the_cornered_defenses",
        title="Mock: The Cornered Defenses",
        substantive_base="Defenses",
        inchoate_layers=[],
        defenses=["necessity", "duress", "self-defense", "insanity"],
        chapters=[21, 22, 23],
        estimated_questions=(10, 15),
        stem_count=1,
        brief_text=_MOCK_THE_CORNERED_DEFENSES_BRIEF,
        statutes="",
    ),
    "final_the_genesis": ScenarioBrief(
        name="final_the_genesis",
        title="Final: The Genesis (The Barksdale Stash)",
        substantive_base="Actus Reus, Causation, Strict Liability",
        inchoate_layers=[],
        defenses=["mistake-of-fact", "mistake-of-law"],
        chapters=[7, 8, 10, 11],
        estimated_questions=(10, 15),
        stem_count=1,
        brief_text=_FINAL_THE_GENESIS_BRIEF,
        statutes="",
    ),
    "final_the_distribution_ring": ScenarioBrief(
        name="final_the_distribution_ring",
        title="Final: The Distribution Ring",
        substantive_base="Inchoate Crimes",
        inchoate_layers=["attempt", "accomplice", "conspiracy", "pinkerton"],
        defenses=["abandonment"],
        chapters=[17, 18, 19],
        estimated_questions=(10, 15),
        stem_count=1,
        brief_text=_FINAL_THE_DISTRIBUTION_RING_BRIEF,
        statutes="",
    ),
    "final_the_empire_business": ScenarioBrief(
        name="final_the_empire_business",
        title="Final: The Empire Business",
        substantive_base="Drugs, Guns, and RICO",
        inchoate_layers=["rico", "rico-conspiracy"],
        defenses=[],
        chapters=[15, 20, 10],
        estimated_questions=(10, 15),
        stem_count=1,
        brief_text=_FINAL_THE_EMPIRE_BUSINESS_BRIEF,
        statutes="",
    ),
    "final_the_blowback": ScenarioBrief(
        name="final_the_blowback",
        title="Final: The Blowback (Homicides)",
        substantive_base="Homicide Grading",
        inchoate_layers=[],
        defenses=["provocation", "eed"],
        chapters=[12, 13, 14],
        estimated_questions=(10, 15),
        stem_count=1,
        brief_text=_FINAL_THE_BLOWBACK_BRIEF,
        statutes="",
    ),
    "final_procedural_block": ScenarioBrief(
        name="final_procedural_block",
        title="Final: The Procedural Block",
        substantive_base="Institutional law",
        inchoate_layers=[],
        defenses=[],
        chapters=[4, 5, 6, 2, 3],
        estimated_questions=(10, 15),
        stem_count=1,
        brief_text=_FINAL_PROCEDURAL_BLOCK_BRIEF,
        statutes="",
    ),
    "final_hamsterdam": ScenarioBrief(
        name="final_hamsterdam",
        title="Final: Hamsterdam",
        substantive_base="Defenses & Misconduct",
        inchoate_layers=["rico"],
        defenses=["necessity", "self-defense", "insanity"],
        chapters=[3, 20, 21, 22, 23],
        estimated_questions=(10, 15),
        stem_count=1,
        brief_text=_FINAL_HAMSTERDAM_BRIEF,
        statutes="",
    ),

}
