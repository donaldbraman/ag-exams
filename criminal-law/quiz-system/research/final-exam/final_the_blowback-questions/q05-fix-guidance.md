# Fix Guidance for q05

The QA pipeline flagged this question. Rewrite `q05.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

<!-- audit: MUST FIX -->

**Safety Block Triggered.** The previous version of this question was blocked by Gemini's safety filters as unsafe. Please rewrite the fact pattern to reduce the risk of unsafe content blocking.

Error: Model returned empty or blocked response.

## Issue 2 — argpass-sonnet

**Q5.** Assume Benny is prosecuted in a jurisdiction that follows the Maryland standard (*Beckwitt*) for depraved heart murder. Is Benny guilty of second-degree depraved heart murder?

(a) Yes, because dumping lethal chemicals in a residential area demonstrates a gross deviation from the standard of care a reasonable person would exercise.
(b) Yes, because Benny's conscious disregard of the toxic cloud risk satisfies the standard for recklessness manifesting extreme indifference to human life.
(c) No, because the creation of a toxic cloud under pouring rain was not reasonably likely, if not certain, to cause death. <!-- correct -->
(d) No, because Benny's primary motive was to save his own life from Carmine's threat, completely negating the required element of malice.
(e) No, because Victor voluntarily assumed the risk of injury by choosing to jog outside near a residential drainage ditch during a rainstorm.

**Answer:** (c)

**Explanation:** Under Maryland's *Beckwitt* standard, depraved heart murder requires conduct that is "reasonably likely, if not certain, to cause death," which is a higher threshold than gross negligence. Dumping chemicals in a ditch during pouring rain, while highly dangerous, does not meet the near-certainty threshold required to elevate the crime to murder. Option (a) is wrong because gross negligence only establishes involuntary manslaughter, not depraved heart murder. Option (b) applies the MPC standard, not the specific Maryland formulation. Option (d) is wrong because motive (self-preservation) does not legally negate the malice of a highly dangerous act. Option (e) is wrong because jogging in public is not a legally recognized assumption of the risk of toxic gas inhalation.

**Tags:** chapters: [13], topics: [depraved heart murder, extreme indifference, likely if not certain], difficulty: medium, cognitive: application

**Grounding:** Chapter 13: likely-if-not-certain-standard / *Beckwitt v. State*

<!-- argument-pass: MUST FIX
(a) Argument-for: A student could argue that dumping "lethal chemicals" in a "residential area" is an extremely hazardous act. The option accurately describes this as a "gross deviation from the standard of care." Because a reasonable person would never dump lethal chemicals where people live, a student might conclude that this egregious level of negligence is definitively sufficient to satisfy the requirements for depraved heart murder, making this option an attractive choice.
(b) Argument-for: A student could argue that Benny's actions perfectly meet the traditional "recklessness manifesting extreme indifference to human life" standard taught in most criminal law courses. Creating a toxic cloud in a residential area undeniably demonstrates a conscious disregard for a massive risk to human life. Because the question involves highly lethal chemicals, a student could reasonably conclude that this extreme indifference is so severe it warrants a murder conviction even under Maryland's heightened threshold.
(c) Argument-for: A student would argue that this option correctly identifies and applies the specific legal test requested: Maryland's *Beckwitt* standard. *Beckwitt* requires that the defendant's conduct be "reasonably likely, if not certain, to cause death." While dumping the chemicals is highly dangerous, variables such as pouring rain and the outdoor environment mean that death is a mere possibility rather than a near-certainty. Thus, the facts fall logically short of the specific, heightened legal threshold required by the jurisdiction.
(d) Argument-for: A student could argue that Benny's mental state was driven entirely by self-preservation ("to save his own life from Carmine's threat"). Because malice historically implies a wicked, abandoned, or depraved mind, a student might reason that acting strictly out of necessity or duress completely negates the extreme indifference required for depraved heart murder. Under this view, the justifiable survival motive overrides the malice aforethought element.
(e) Argument-for: A student could argue that Victor's choice to jog outside during a severe rainstorm next to a drainage ditch was highly unreasonable and constitutes an assumption of the risk. In some legal contexts, a victim's unforeseeable or deeply negligent behavior can sever the chain of proximate causation. Therefore, a student might conclude that Victor's voluntary exposure to dangerous weather conditions legally absolves Benny of homicide liability.

Head-to-head: 
Option (c) correctly identifies the unique *Beckwitt* standard, but its factual conclusion is highly vulnerable; a strong student could easily argue that creating a lethal toxic cloud in a residential area *is* factually "likely, if not certain" to cause death, making Option (b) arguably just as strong. Furthermore, Options (a) and (b) fail the close-call standard because they rely on implicit omissions rather than explicit, falsifiable legal claims. Both accurately describe Benny's conduct under lesser mens rea standards (gross negligence and MPC extreme indifference) but fail to explicitly and falsely state that these standards are *legally sufficient* to satisfy the *Beckwitt* rule. Option (d) provides a strong distractor by using the absolute phrase "completely negating," and Option (e) uses a great explicitly false legal concept for criminal law ("voluntarily assumed the risk").

Falsifiable claim per distractor:
- (a): "demonstrates a gross deviation from the standard of care..." — implicitly wrong because this is the standard for involuntary manslaughter, not *Beckwitt* murder, but lacks an absolute word stating this standard categorically establishes murder.
- (b): "satisfies the standard for recklessness manifesting extreme indifference..." — implicitly wrong because it cites the MPC standard rather than the requested MD standard, but it lacks an explicitly false claim that this standard legally governs in Maryland.
- (d): "completely negating the required element of malice" — wrong because a self-preservation motive does not categorically or legally negate the objective malice of an extremely reckless act.
- (e): "voluntarily assumed the risk of injury" — wrong because assumption of risk is a tort doctrine, not a recognized defense to criminal homicide.

Recommended fix: MUST FIX. Revise (a) and (b) to include explicit, locked false legal claims so they do not rely on implicit omissions. Revise (c) to firmly tie the conclusion to the legal rule rather than a debatable factual premise.
Example edits:
(a) Yes, because a gross deviation from the standard of care categorically establishes malice for depraved heart murder in every jurisdiction.
(b) Yes, because the MPC standard of recklessness manifesting extreme indifference to human life automatically satisfies the *Beckwitt* test.
(c) No, because under the *Beckwitt* standard, the conduct must be reasonably likely, if not certain, to cause death, an evidentiary threshold these facts fail to reach.
-->

## Issue 3 — argpass-opus

**Q5.** Assume Benny is prosecuted in a jurisdiction that follows the Maryland standard (*Beckwitt*) for depraved heart murder. Is Benny guilty of second-degree depraved heart murder?

(a) Yes, because dumping lethal chemicals in a residential area demonstrates a gross deviation from the standard of care a reasonable person would exercise.
(b) Yes, because Benny's conscious disregard of the toxic cloud risk satisfies the standard for recklessness manifesting extreme indifference to human life.
(c) No, because the creation of a toxic cloud under pouring rain was not reasonably likely, if not certain, to cause death. <!-- correct -->
(d) No, because Benny's primary motive was to save his own life from Carmine's threat, completely negating the required element of malice.
(e) No, because Victor voluntarily assumed the risk of injury by choosing to jog outside near a residential drainage ditch during a rainstorm.

**Answer:** (c)

**Explanation:** Under Maryland's *Beckwitt* standard, depraved heart murder requires conduct that is "reasonably likely, if not certain, to cause death," which is a higher threshold than gross negligence. Dumping chemicals in a ditch during pouring rain, while highly dangerous, does not meet the near-certainty threshold required to elevate the crime to murder. Option (a) is wrong because gross negligence only establishes involuntary manslaughter, not depraved heart murder. Option (b) applies the MPC standard, not the specific Maryland formulation. Option (d) is wrong because motive (self-preservation) does not legally negate the malice of a highly dangerous act. Option (e) is wrong because jogging in public is not a legally recognized assumption of the risk of toxic gas inhalation.

**Tags:** chapters: [13], topics: [depraved heart murder, extreme indifference, likely if not certain], difficulty: medium, cognitive: application

**Grounding:** Chapter 13: likely-if-not-certain-standard / *Beckwitt v. State*

<!-- argument-pass: SHOULD FIX
(a) Argument-for: A student could argue that Benny's dumping of lethal chemicals in a residential area is undeniably highly dangerous. Depraved heart murder requires an exceptionally high degree of negligence, often described as a gross deviation from a reasonable standard of care. By characterizing the chemical dumping as a gross deviation, this option accurately captures the foundational mens rea for unintentional homicide. Therefore, the student might conclude that this extreme recklessness in a residential zone satisfies the requirement for depraved heart murder.
(b) Argument-for: A student could contend that depraved heart murder is universally understood as a homicide resulting from "recklessness manifesting extreme indifference to human life," which is the Model Penal Code standard. Even if a jurisdiction has specific case law like *Beckwitt*, the core underlying concept remains extreme indifference. Benny's conscious disregard of a toxic cloud in a residential area easily meets this MPC baseline. Thus, a student might reason that option (b) correctly states the universally recognized substantive legal standard for the crime.
(c) Argument-for: Under Maryland law, established in cases like *Beckwitt v. State*, the threshold for depraved heart murder is exceptionally high. It requires that the defendant's conduct be "reasonably likely, if not certain, to cause death." While dumping chemicals is dangerous, the creation of a deadly toxic cloud under pouring rain—which might wash away or dilute the chemicals—is not "likely, if not certain" to kill someone. Therefore, option (c) correctly applies the specific jurisdictional rule to the facts to conclude Benny lacks the requisite level of risk for this specific charge.
(d) Argument-for: A student might argue that Benny only acted under the immediate threat to his life from Carmine. Under general criminal law principles, acting out of a desire for self-preservation or under duress can alter or negate the mens rea for certain crimes. Since depraved heart murder requires "malice," which implies a wicked or abandoned heart, acting solely to save one's own life ostensibly lacks this inherent wickedness. Thus, the student could argue that the self-preservation motive definitively strips the act of the required malice.
(e) Argument-for: A student could argue that causation in criminal law can be severed by an unforeseeable or voluntary act of the victim. Victor chose to jog outside during a severe rainstorm near a drainage ditch, which is an inherently risky and unusual activity. By voluntarily placing himself in a hazardous environment, Victor assumed the risk of injury. A student might conclude this voluntary act supersedes Benny's initial dumping, breaking the chain of causation and relieving Benny of criminal liability.

Head-to-head: The keyed answer (c) correctly applies the specific *Beckwitt* standard mandated by the call of the question. Distractors (a) and (b) rely on standards from other contexts (gross negligence for manslaughter, and extreme indifference for the MPC, respectively), but they lack absolute qualifiers, leaving them vulnerable to complaints that they contain factually true but merely incomplete legal statements. Distractor (d) correctly locks a false legal claim by asserting that self-preservation "completely negat[es]" malice. Distractor (e) explicitly imports the tort doctrine of assumption of risk into criminal homicide, providing a clear, falsifiable error. 

Falsifiable claim per distractor:
- (a): "demonstrates a gross deviation from the standard of care" — wrong because it relies on the involuntary manslaughter standard (gross negligence), but it lacks absolute phrasing to explicitly claim this standard is categorically sufficient for murder.
- (b): "satisfies the standard for recklessness manifesting extreme indifference" — wrong because it relies on the MPC formulation rather than the prompt's mandated Maryland standard, but it lacks absolute phrasing to definitively block a student from arguing it is merely an implicitly incomplete statement.
- (d): "completely negating the required element of malice" — wrong because motive (even self-preservation) does not automatically negate implied malice for a highly dangerous act.
- (e): "voluntarily assumed the risk of injury" — wrong because assumption of risk is generally a tort concept, not an affirmative defense that negates criminal homicide.

Recommended fix: Add absolute locking words to distractors (a) and (b) to ensure they contain explicitly false sufficiency claims. Edit (a) to: "Yes, because dumping lethal chemicals in a residential area is a gross deviation from the standard of care, which categorically establishes depraved heart murder." Edit (b) to: "Yes, because Benny's conscious disregard of the toxic cloud risk automatically satisfies the standard for depraved heart murder, regardless of whether death was reasonably likely."
-->
