# Fix Guidance for q08

The QA pipeline flagged this question. Rewrite `q08.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

# Stem 2: Homicide, Causation, and Plea Negotiations

Blake has died from his injuries in the hospital. The investigation into the aftermath of the shooting revealed a 45-minute delay in calling 911 and a major hospital error. I need you to evaluate Alex's homicide grading based on his emotional state, and analyze whether his omission or the medical error affects his liability for the completed homicide.

**Q8.** Assume Alex is charged with murder in a jurisdiction that follows the Model Penal Code's Extreme Emotional Disturbance (EED) standard. Which of the following provides Alex's strongest argument for mitigating the charge to manslaughter?

(a) Blake's insulting remark about Alex being a "pathetic loser" strictly meets the traditional common-law categorical requirements for adequate provocation by a victim.
(b) The combination of Blake's insult and Alex's trespassing created a spontaneous mutual combat situation that automatically negates the malice aforethought requirement.
(c) Alex acted under an extreme emotional disturbance for which there was a reasonable explanation, based partly on his severe depression following his wife's death. <!-- correct -->
(d) Alex's sudden realization that he had shot an unarmed man caused him to panic, establishing that the actual killing occurred in the heat of passion.
(e) Blake's sudden act of reaching into his heavy jacket provided adequate physical provocation that would cause an ordinary, reasonable man to lose all self-control.

**Answer:** (c)

**Explanation:** (c) is correct because the MPC's EED standard allows for subjective mitigation based on the defendant's emotional state, such as severe depression from recent trauma (Fact 1), rather than requiring a specific provocative act. (a) is incorrect because "mere words" (Fact 5) do not meet the strict common-law categories for adequate provocation. (b) is incorrect because mutual combat requires mutual physical engagement, not just an insult and a trespass. (d) is incorrect because the emotional disturbance must precede or coincide with the killing, not arise after the victim is shot (Fact 9). (e) is incorrect because reaching into a pocket (Fact 6) is analyzed under self-defense, not as a provocation causing a loss of self-control.

**Tags:** chapters: [12], topics: [extreme emotional disturbance, provocation, manslaughter], difficulty: medium, cognitive: application

**Grounding:** Chapter 12, Extreme Emotional Disturbance (EED expands old categories and considers defendant's subjective state).

<!-- audit: MUST FIX
check 1: pass
check 2: pass
check 3: finding (The explanation for (e) states that reaching into a pocket is analyzed under self-defense, not provocation. While true at common law, MPC EED allows for extreme fear or terror to mitigate murder to manslaughter; it is not limited to anger. The actual reason (e) is wrong under the MPC is that its wording ("ordinary, reasonable man," "adequate physical provocation") relies on the rigid common-law objective standard rather than the MPC's subjective "actor's situation" standard.)
check 4: finding (The stem contains a blatant leaked AI prompt instruction: "I need you to evaluate Alex's homicide grading...". Additionally, the stem lacks the necessary facts to answer the question. The options and explanations rely on missing numbered facts like Alex's severe depression, Blake's insulting remark, and the pocket reach, indicating this question was detached from a larger shared fact pattern and is not self-contained.)
check 5: pass
check 6: pass
check 7: pass
Recommended fix: Remove the leaked AI instruction from the stem. Integrate the missing facts (Alex's depression, the insult, the pocket reach) directly into the stem so the question is functionally self-contained. Revise the explanation for (e) to reflect that MPC EED can indeed involve fear, but the option fails because it uses the objective common-law standard instead of the MPC's standard.
-->
