# Fix Guidance for q07

The QA pipeline flagged this question. Rewrite `q07.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q7.** Assume Trey is prosecuted for misdemeanor manslaughter regarding Omar's death, using only the suspended license violation as the predicate offense. How will the court rule under the proximate-cause limitation?

(a) Not guilty, because the unlawful aspect of driving with a suspended license was not causally connected to Omar's death. <!-- correct -->
(b) Not guilty, because driving with a suspended license is a malum in se offense that requires independent proof of malice.
(c) Guilty, because Trey would not have been driving on that street but for his deliberate decision to drive with a suspended license.
(d) Guilty, because the Model Penal Code expressly permits misdemeanor manslaughter for any minor traffic offense resulting in death.
(e) Guilty, because the strict-liability structure of misdemeanor manslaughter eliminates the need to prove any form of causal nexus.

**Answer:** (a)

**Explanation:** The proximate cause limitation to misdemeanor manslaughter (*Commonwealth v. Williams*) requires that the specific unlawful aspect of the defendant's conduct cause the death. Here, Trey's reckless speeding caused the crash, not his lack of a valid administrative license, making (a) correct. (b) misclassifies a suspended license as malum in se; it is a classic malum prohibitum offense. (c) applies mere "but-for" causation, which the proximate cause limitation was explicitly designed to reject. (d) is entirely false; the MPC completely rejects the misdemeanor manslaughter doctrine. (e) is wrong because while the doctrine substitutes for mens rea, it still requires legal causation connecting the illegality to the death.

**Tags:** chapters: [14], topics: [misdemeanor manslaughter, proximate cause], difficulty: medium, cognitive: application

**Grounding:** Chapter 14: Felony Murder and Misdemeanor Manslaughter -> mm-proximate-cause-limit

<!-- audit: MUST FIX
1: pass
2: pass
3: pass
4: MUST FIX. The stem lacks the facts necessary to answer the question and assumes context from a missing fact pattern. It references "Trey," "Omar's death," and a "suspended license," but the explanation relies on facts ("Trey's reckless speeding caused the crash") that appear nowhere in the prompt.
5: pass
6: pass
7: pass
8: pass
Recommended fix: Provide the factual scenario in the stem (e.g., "While recklessly speeding, Trey strikes and kills Omar. At the time, Trey was driving with a suspended license. Assume Trey is prosecuted...").
-->

## Issue 2 — argpass-sonnet

**Q7.** Assume Trey is prosecuted for misdemeanor manslaughter regarding Omar's death, using only the suspended license violation as the predicate offense. How will the court rule under the proximate-cause limitation?

(a) Not guilty, because the unlawful aspect of driving with a suspended license was not causally connected to Omar's death. <!-- correct -->
(b) Not guilty, because driving with a suspended license is a malum in se offense that requires independent proof of malice.
(c) Guilty, because Trey would not have been driving on that street but for his deliberate decision to drive with a suspended license.
(d) Guilty, because the Model Penal Code expressly permits misdemeanor manslaughter for any minor traffic offense resulting in death.
(e) Guilty, because the strict-liability structure of misdemeanor manslaughter eliminates the need to prove any form of causal nexus.

**Answer:** (a)

**Explanation:** The proximate cause limitation to misdemeanor manslaughter (*Commonwealth v. Williams*) requires that the specific unlawful aspect of the defendant's conduct cause the death. Here, Trey's reckless speeding caused the crash, not his lack of a valid administrative license, making (a) correct. (b) misclassifies a suspended license as malum in se; it is a classic malum prohibitum offense. (c) applies mere "but-for" causation, which the proximate cause limitation was explicitly designed to reject. (d) is entirely false; the MPC completely rejects the misdemeanor manslaughter doctrine. (e) is wrong because while the doctrine substitutes for mens rea, it still requires legal causation connecting the illegality to the death.

**Tags:** chapters: [14], topics: [misdemeanor manslaughter, proximate cause], difficulty: medium, cognitive: application

**Grounding:** Chapter 14: Felony Murder and Misdemeanor Manslaughter -> mm-proximate-cause-limit

<!-- argument-pass: SHOULD FIX
(a) Argument-for: The proximate-cause limitation to misdemeanor manslaughter requires that the specific unlawful aspect of the defendant's conduct be the proximate cause of death. Here, the unlawful aspect is the lack of an administrative license, which has no direct causal nexus to the physical mechanics of the crash. Since the suspended license merely placed him on the road, it fails the proximate-cause test under cases like *Commonwealth v. Williams*. Thus, Trey is not guilty based solely on the license violation.
(b) Argument-for: Driving with a suspended license involves a deliberate defiance of a state safety order, which a student could argue elevates the act to a *malum in se* offense. If classified as *malum in se*, the offense is inherently dangerous and wrong in itself, traditionally requiring independent proof of malice or criminal intent. Because Trey's act was malum in se, the court would require this independent malice to convict, leading to a not guilty verdict if it is absent.
(c) Argument-for: Proximate cause inherently encompasses "but-for" causation as its foundational step. A student could argue that under a broad interpretation of proximate cause, Trey's deliberate decision to drive illegally was the initiating cause of the entire sequence of events. But for his choice to violate the suspension, he would not have been at the scene of the accident, making him legally responsible for the resulting death.
(d) Argument-for: The Model Penal Code historically aimed to codify and standardize homicide offenses across jurisdictions. A student might argue that the MPC incorporates a modernized version of misdemeanor manslaughter that applies specifically to minor traffic offenses to deter dangerous driving. Under this view, any traffic violation resulting in death is expressly permitted to serve as the predicate for manslaughter.
(e) Argument-for: Misdemeanor manslaughter operates as a strict-liability mechanism regarding the death, substituting the intent to commit the misdemeanor for the mens rea of homicide. A student could argue that this strict-liability structure completely eliminates the need to establish proximate cause. Since the causal nexus requirement is removed by the doctrine's strict-liability nature, Trey is guilty simply because the death occurred during the offense.

Head-to-head: Option (a) correctly applies the proximate-cause limitation, properly distinguishing the unlawful administrative aspect of the act from the physical cause of death. Option (b) fails because a suspended license is universally classified as *malum prohibitum*, not *malum in se*. Option (c) is incorrect because it conflates mere "but-for" causation with proximate cause; however, its phrasing lacks an absolute word to explicitly lock the premise that but-for causation alone is sufficient. Option (d) contains an explicitly false claim about the Model Penal Code, which outright rejects the misdemeanor manslaughter doctrine. Option (e) falsely claims that strict liability eliminates the need for *any* form of causal nexus, when in fact causation is still strictly required even for strict-liability offenses.

Falsifiable claim per distractor:
- (b): "is a malum in se offense that requires independent proof of malice" — wrong because driving on a suspended license is a classic *malum prohibitum* regulatory offense.
- (c): "Guilty, because Trey would not have been driving on that street but for his deliberate decision" — wrong because mere but-for presence on the road does not satisfy the proximate-cause limitation, but lacks an absolute word to firmly lock the legal falsehood.
- (d): "Model Penal Code expressly permits misdemeanor manslaughter" — wrong because the MPC entirely rejects the misdemeanor manslaughter rule.
- (e): "eliminates the need to prove any form of causal nexus" — wrong because strict liability removes the mens rea requirement for the resulting harm, not the actus reus requirement of a causal nexus.

Recommended fix: Edit (c) to lock the error with an absolute word: "(c) Guilty, solely because Trey would not have been driving on that street but for his deliberate decision to drive with a suspended license."
-->
