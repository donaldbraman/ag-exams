# Fix Guidance for q10

The QA pipeline flagged this question. Rewrite `q10.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q10.** Assume Marcus is charged with felony murder for the watchman's death based on the predicate felony of attempted arson. How would his duress claim affect this charge?

(a) Under the MPC, Marcus's duress claim fails categorically because he was at fault for willingly associating with a notoriously violent criminal syndicate.
(b) Under the common law, duress serves as a complete defense to all forms of murder, rendering the felony murder charge legally invalid from the outset.
(c) Under the common law, duress is unavailable for intentional murder but is automatically permitted for unintentional felony murder in every modern American jurisdiction.
(d) Under the common law, duress is categorically unavailable for any murder charge, but some jurisdictions allow it for felony murder if the predicate felony was coerced. <!-- correct -->
(e) Under the MPC, duress is treated as a partial justification that strictly reduces any felony murder charge to a lesser grade of involuntary manslaughter.

**Answer:** (d)

**Explanation:** Under traditional common law, duress is categorically unavailable as a defense to any form of murder, because a person may not take an innocent life to save their own. However, several states (e.g., Michigan, Maryland) have carved out an exception for felony murder: if the underlying predicate felony (here, attempted arson) was committed under duress, the duress defense may break the chain of felony-murder liability (*People v. Reichard*). (a) is incorrect because the MPC does not automatically bar duress for associating with bad actors unless the actor recklessly placed themselves in the situation where coercion was probable. (b) is incorrect because the common law murder bar strictly prohibits duress as a defense to murder. (c) is incorrect because the felony-murder exception is a minority rule, not one adopted by every modern jurisdiction. (e) is incorrect because the MPC treats duress as an excuse, not a partial justification, and it fully allows duress as a defense to murder without automatically reducing it to manslaughter.

**Tags:** chapters: [21], topics: [felony murder, duress, murder bar exception], difficulty: medium, cognitive: application

**Grounding:** Chapter 21 - felony-murder-duress-exception

<!-- audit: MUST FIX
Check 1: pass (The correct answer accurately states the traditional common law rule and the modern jurisdictional split regarding the felony-murder exception).
Check 2: finding (Option (a) is a highly defensible distractor—or potentially a correct answer depending on the missing facts. Under MPC § 2.09(2), willingly associating with a "notoriously violent criminal syndicate" is the casebook's textbook example of recklessly placing oneself in a situation where coercion is probable, which *does* bar the defense. A prepared student could strongly argue this categorically defeats the claim.)
Check 3: finding (The explanation dismisses (a) by stating the MPC doesn't "automatically" bar duress for associating with bad actors unless the actor was reckless. But "willingly associating with a notoriously violent criminal syndicate" virtually defines that recklessness standard under the MPC, making the explanation's reasoning weak/evasive.)
Check 4: finding (The stem is completely missing the macro fact pattern. It refers to "Marcus," "the watchman's death," and his "duress claim" without providing any facts about the coercion or his prior associations, making it impossible to confidently evaluate fact-applied options like (a).)
Check 5: finding (The question asks how the claim would affect *his* charge, but does not stipulate a jurisdiction. The correct answer (d) just states that "some jurisdictions" allow the defense, which surveys the law rather than resolving Marcus's specific case.)
Check 6: pass
Check 7: pass
Recommended fix: Provide the missing facts in the stem (or ensure this is explicitly linked to a macro pattern). Revise the call of the question to ask "Which of the following statements about his duress claim is most accurate?" so option (d)'s jurisdictional survey fits the prompt logically. Finally, weaken option (a) by changing "notoriously violent criminal syndicate" to a softer association (e.g., "willingly associating with a known petty thief") so it doesn't clearly trigger the MPC § 2.09(2) recklessness exception.
-->
