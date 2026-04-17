# Fix Guidance for q13

The QA pipeline flagged this question. Rewrite `q13.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q13.** Independent of Arthur's liability, the prosecution charges Chloe with homicide based on her failure to call 911. Did Chloe have a legal duty to act?

(a) No, because Chloe did not physically manufacture or distribute the drug that caused Marcus to overdose.
(b) Yes, because the Good Samaritan paradox imposes a universal legal duty to rescue anyone in imminent danger of death.
(c) No, because Chloe's actions only constituted a passive omission, and omissions are never punishable as criminal homicide.
(d) Yes, because by dragging Marcus into dense brush, she secluded him and prevented others from coming to his aid. <!-- correct -->
(e) Yes, because as the owner of the van, she had a statutory duty to ensure the safety of anyone who entered her vehicle.

**Answer:** (d)

**Explanation:** Under the *Jones* categories for omission liability, a duty to act arises if a person voluntarily undertakes to assist someone but then secludes them, preventing others from rendering aid. By dragging the unconscious Marcus into dense brush, Chloe actively isolated him and prevented paramedics or bystanders from helping him, triggering a duty. (a) is wrong because her duty arises from her seclusion of the victim, regardless of who manufactured the drug. (b) is wrong because there is no universal "Good Samaritan" duty to rescue in American criminal law. (c) is wrong because omissions are punishable when there is a legal duty to act. (e) is wrong because vehicle ownership does not inherently create a statutory duty to rescue passengers.

**Tags:** chapters: [9], topics: [omissions, duty to act, voluntary assumption, seclusion], difficulty: medium, cognitive: application

**Grounding:** voluntary-assumption-plus-seclusion

<!-- audit: MUST FIX
Check 1: pass
Check 2: pass
Check 3: pass
Check 4: MUST FIX - The question stem is entirely missing the underlying fact pattern. It references actors (Arthur, Chloe, Marcus) and events (an overdose, dragging someone into brush, owning a van) that are never introduced in the text, likely because this was pulled from a multi-question scenario but the facts were not carried over.
Check 5: pass
Check 6: pass
Check 7: pass
Recommended fix: Add the missing scenario facts to the question stem so the student knows what Chloe actually did.
-->

## Issue 2 — argpass-opus

**Q13.** Independent of Arthur's liability, the prosecution charges Chloe with homicide based on her failure to call 911. Did Chloe have a legal duty to act?

(a) No, because Chloe did not physically manufacture or distribute the drug that caused Marcus to overdose.
(b) Yes, because the Good Samaritan paradox imposes a universal legal duty to rescue anyone in imminent danger of death.
(c) No, because Chloe's actions only constituted a passive omission, and omissions are never punishable as criminal homicide.
(d) Yes, because by dragging Marcus into dense brush, she secluded him and prevented others from coming to his aid. <!-- correct -->
(e) Yes, because as the owner of the van, she had a statutory duty to ensure the safety of anyone who entered her vehicle.

**Answer:** (d)

**Explanation:** Under the *Jones* categories for omission liability, a duty to act arises if a person voluntarily undertakes to assist someone but then secludes them, preventing others from rendering aid. By dragging the unconscious Marcus into dense brush, Chloe actively isolated him and prevented paramedics or bystanders from helping him, triggering a duty. (a) is wrong because her duty arises from her seclusion of the victim, regardless of who manufactured the drug. (b) is wrong because there is no universal "Good Samaritan" duty to rescue in American criminal law. (c) is wrong because omissions are punishable when there is a legal duty to act. (e) is wrong because vehicle ownership does not inherently create a statutory duty to rescue passengers.

**Tags:** chapters: [9], topics: [omissions, duty to act, voluntary assumption, seclusion], difficulty: medium, cognitive: application

**Grounding:** voluntary-assumption-plus-seclusion

<!-- argument-pass: SHOULD FIX
(a) Argument-for: A student could argue that criminal omissions require the defendant to have directly created the perilous situation. By pointing out that Chloe did not manufacture or distribute the drugs, the student could argue she did not create the peril. Therefore, she would just be a mere bystander. Since bystanders generally have no duty to rescue, the student might conclude that her lack of involvement in the drug's origin entirely shields her from a duty to act.
(b) Argument-for: A student might conflate moral obligations with legal ones when extreme danger is involved. They might recall discussions of "Good Samaritan" laws and mistakenly assume these laws create affirmative duties rather than just shielding voluntary rescuers from civil liability. Consequently, they could argue that a universal doctrine exists compelling rescue when someone is facing imminent death, especially if the cost to rescue is low.
(c) Argument-for: A student could argue that criminal homicide strictly requires an affirmative act to satisfy the actus reus element. By merely failing to call 911, Chloe committed a passive omission rather than an affirmative act. Believing that omissions are inherently distinct from acts, the student might incorrectly deduce that passive omissions can never serve as the basis for a criminal homicide charge.
(d) Argument-for: Under the *Jones v. United States* framework for omission liability, the general no-duty rule has specific exceptions. A legal duty arises if a defendant voluntarily undertakes care of a helpless person and secludes them, thereby preventing others from rendering aid. By dragging Marcus into the dense brush, Chloe actively isolated him and cut off his chance of rescue, perfectly satisfying this recognized exception to the no-duty rule.
(e) Argument-for: A student might correctly recall that special relationships can trigger a legal duty to act. Applying that concept loosely, they might assume that owning the vehicle in which the victim overdosed creates a special legal status. Thus, they could argue that a statutory "premises" or "custodial" relationship obligates the vehicle owner to seek medical help for anyone injured inside their property.

Head-to-head: Option (d) correctly applies the voluntary-assumption-plus-seclusion doctrine from *Jones*. Option (c) is easily falsifiable due to the absolute word "never." Option (b) explicitly relies on a fabricated "universal legal duty." Option (e) explicitly asserts a non-existent "statutory duty" for vehicle owners. Option (a), however, is structurally weak under the close-call standard: it relies on a true factual premise (Chloe didn't manufacture the drug) and uses it to justify "No," but requires the unstated, implicit false premise that *only* manufacturing or distributing the drug creates a duty. Because it lacks an absolute restrictor, it violates the rule that implicit omissions do not suffice to falsify a distractor.

Falsifiable claim per distractor:
- (a): "because Chloe did not physically manufacture or distribute the drug" — wrong because it lacks an explicit false claim; it relies on an implicit omission that *only* manufacturing the drug creates a duty, which violates the strict standard.
- (b): "imposes a universal legal duty to rescue" — wrong because there is categorically no universal duty to rescue in American criminal law.
- (c): "omissions are never punishable as criminal homicide" — wrong because omissions are punishable when a special legal duty to act exists.
- (e): "she had a statutory duty to ensure the safety" — wrong because vehicle owners do not possess a blanket statutory duty to rescue passengers under criminal law.

Recommended fix: Lock option (a) with an absolute word. Change to: "(a) No, because a legal duty to rescue an overdose victim arises solely if the defendant physically manufactured or distributed the drug."
-->
