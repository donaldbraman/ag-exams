# Fix Guidance for q01

The QA pipeline flagged this question. Rewrite `q01.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q1.** Is Arthur guilty of manufacturing a Schedule I substance despite his genuine belief it was a legal nootropic?

(a) Yes, because under the dangerous items heuristic, a person who knows the specific chemical structure of a synthetic drug acts at their peril regarding its legal classification. <!-- correct -->
(b) Yes, because the Morissette presumption against strict liability is automatically rebutted whenever a statute imposes severe felony penalties for public welfare offenses.
(c) No, because his genuine mistake of fact regarding the chemical's classification negates the "knowing" mental state required for the manufacturing element.
(d) No, because the statute's silence on mens rea means the prosecution must prove at least recklessness under the default rules of the Model Penal Code.
(e) No, because a professor synthesizing chemicals is engaged in conduct that is entirely innocent, defeating the strict liability notice requirement established by precedent.

**Answer:** (a)

**Explanation:** (a) is correct. Under the dangerous items heuristic established in *United States v. Balint*, individuals dealing in highly dangerous substances (like synthetic drugs) are placed on notice of their likely regulation and act at their peril. Arthur knew the exact chemical structure he was distributing, satisfying the actus reus and basic knowledge requirement; his mistake regarding its legal classification is an invalid mistake of law defense. (b) is incorrect because severe penalties generally trigger the *Staples* presumption of mens rea, rather than rebutting it. (c) is incorrect because his mistake is about the penal law classification, not the factual nature of the chemical structure itself. (d) is incorrect because the dangerous items heuristic displaces the MPC recklessness default for these specific public welfare offenses. (e) is incorrect because synthesizing powerful synthetic drugs does not constitute "entirely innocent" conduct like possessing an ordinary firearm.

**Tags:** chapters: [11], topics: [public welfare offenses, dangerous items, mistake of law], difficulty: medium, cognitive: application

**Grounding:** Chapter 11 - Dangerous Items or Activities (Morissette Factor 2); United States v. Balint

<!-- audit: MUST FIX
Check 1: Fails. The correct answer (a) assumes Arthur knew the specific chemical structure, a fact completely absent from the barebones stem.
Check 2: Fails. Option (d) is a highly defensible distractor. Without a specified jurisdiction, a student could validly argue that under the MPC, strict liability for crimes is abolished and statutory silence on mens rea defaults to at least recklessness (MPC §§ 2.05, 2.02(3)).
Check 3: Fails. The explanation relies on "ghost facts" not present in the stem (e.g., asserting that Arthur knew the exact chemical structure he was distributing).
Check 4: Fails completely. The stem is essentially just a call line and lacks the actual fact pattern. It omits the statutory text, penalty level, Arthur's factual knowledge, and his profession (which appears out of nowhere in option e).
Check 5: Fails. The jurisdiction (e.g., a federal prosecution applying Balint/Staples vs. an MPC jurisdiction) is not stipulated, causing a fatal ambiguity between (a) and (d).
Check 6: Pass.
Check 7: Pass. The concepts (Balint, Morissette, MPC defaults) map to the Chapter 11 and 10 tags.
Recommended fix: Restore the missing fact pattern to the stem. Ensure it details Arthur's exact knowledge of the chemical structure, the text and penalties of the statute, his profession, and specifies that this is a federal prosecution (or a jurisdiction applying common-law background rules) to legitimately rule out the MPC default in (d).
-->

## Issue 2 — argpass-opus

**Q1.** Is Arthur guilty of manufacturing a Schedule I substance despite his genuine belief it was a legal nootropic?

(a) Yes, because under the dangerous items heuristic, a person who knows the specific chemical structure of a synthetic drug acts at their peril regarding its legal classification. <!-- correct -->
(b) Yes, because the Morissette presumption against strict liability is automatically rebutted whenever a statute imposes severe felony penalties for public welfare offenses.
(c) No, because his genuine mistake of fact regarding the chemical's classification negates the "knowing" mental state required for the manufacturing element.
(d) No, because the statute's silence on mens rea means the prosecution must prove at least recklessness under the default rules of the Model Penal Code.
(e) No, because a professor synthesizing chemicals is engaged in conduct that is entirely innocent, defeating the strict liability notice requirement established by precedent.

**Answer:** (a)

**Explanation:** (a) is correct. Under the dangerous items heuristic established in *United States v. Balint*, individuals dealing in highly dangerous substances (like synthetic drugs) are placed on notice of their likely regulation and act at their peril. Arthur knew the exact chemical structure he was distributing, satisfying the actus reus and basic knowledge requirement; his mistake regarding its legal classification is an invalid mistake of law defense. (b) is incorrect because severe penalties generally trigger the *Staples* presumption of mens rea, rather than rebutting it. (c) is incorrect because his mistake is about the penal law classification, not the factual nature of the chemical structure itself. (d) is incorrect because the dangerous items heuristic displaces the MPC recklessness default for these specific public welfare offenses. (e) is incorrect because synthesizing powerful synthetic drugs does not constitute "entirely innocent" conduct like possessing an ordinary firearm.

**Tags:** chapters: [11], topics: [public welfare offenses, dangerous items, mistake of law], difficulty: medium, cognitive: application

**Grounding:** Chapter 11 - Dangerous Items or Activities (Morissette Factor 2); United States v. Balint

<!-- argument-pass: SHOULD FIX
(a) Argument-for: Under the dangerous items heuristic established in *United States v. Balint*, individuals dealing with highly regulated or dangerous substances are placed on notice of strict regulation. In *McFadden v. United States*, the Supreme Court held that knowledge of the specific chemical structure of a controlled substance satisfies the mens rea, even if the defendant is ignorant of its legal scheduling. Because Arthur knew the exact chemical structure, his belief that it was a legal nootropic is an invalid mistake of law defense, meaning he acts at his peril.
(b) Argument-for: A student could argue that the public welfare doctrine is specifically designed to dispense with mens rea to protect the public from highly dangerous activities. If a statute targets the illicit manufacturing of drugs and carries severe felony penalties, one could reason that the legislature's intent was to prioritize deterrence and strict enforcement. Therefore, they might incorrectly conclude that the severity of the penalty underscores a legislative intent to automatically rebut the *Morissette* presumption against strict liability.
(c) Argument-for: A student could argue that Arthur's belief about the substance being a legal nootropic represents a fundamental misunderstanding of an attendant circumstance. By genuinely believing the drug lacked the properties or status of a scheduled substance, he failed to possess the "knowing" mental state required to manufacture an illegal drug. This argument treats the legal classification on a penal schedule as a mistake of fact that negates the offense's underlying mens rea.
(d) Argument-for: Under Model Penal Code § 2.02(3), when a statute is silent regarding the requisite mens rea, the default culpability level is recklessness. A student could argue that because Arthur genuinely believed the substance was legal, he did not consciously disregard a substantial and unjustifiable risk that he was manufacturing a Schedule I drug. Therefore, the prosecution cannot meet its burden to prove default recklessness, resulting in an acquittal.
(e) Argument-for: Relying on the *Staples v. United States* exception to the dangerous items heuristic, a student could argue that synthesizing chemical compounds for academic or nootropic research is traditionally innocent conduct. Because academic chemistry does not bear the obvious hallmarks of illicit drug trafficking, Arthur is not put on strict notice that his conduct is heavily regulated. This defeats the strict liability notice requirement, requiring the prosecution to prove he knew the substance was illegal.

Head-to-head: 
Option (a) is the clearly correct legal outcome, properly applying the *Balint* and *McFadden* precedents to show that knowing a specific chemical structure satisfies the mens rea, while ignorance of its scheduled status is an invalid mistake of law. Option (b) contains a starkly backwards legal claim; severe felony penalties actually strengthen the *Staples* presumption against strict liability rather than automatically rebutting it. Option (c) explicitly mischaracterizes the governing law, falsely classifying a mistake about a penal drug schedule as a "mistake of fact." Option (e) is factually and legally incorrect in categorizing the synthesis of complex synthetic drugs as "entirely innocent," violating the dangerous items heuristic. Option (d), however, relies on an implicit application error rather than an explicit false claim: while it correctly states the MPC recklessness default, it implicitly (and incorrectly) assumes that recklessness applies to mistake of law (legal classification) under MPC § 2.02(9). It lacks the absolute framing needed to definitively lock in its falsity under a strict standard.

Falsifiable claim per distractor:
- (b): "automatically rebutted whenever a statute imposes severe felony penalties" — wrong because under *Staples*, severe felony penalties actually strengthen the presumption against strict liability rather than rebutting it.
- (c): "genuine mistake of fact regarding the chemical's classification" — wrong because the classification of a chemical on a penal schedule is a matter of governing law, rendering this a mistake of law rather than fact.
- (d): "means the prosecution must prove at least recklessness" — wrong in its implicit causal application since MPC § 2.02(9) excludes governing legal status from the recklessness default, but the option currently lacks an absolute word to explicitly lock in this falsity.
- (e): "engaged in conduct that is entirely innocent" — wrong because manufacturing active synthetic chemicals is a highly regulated, dangerous activity under *Balint*, not a traditionally "entirely innocent" baseline.

Recommended fix: Edit (d) to include absolute wording that locks in the false legal application. Change (d) to: "No, because the statute's silence on mens rea categorically requires the prosecution to prove recklessness regarding the chemical's legal classification under the Model Penal Code."
-->
