# Fix Guidance for q10

The QA pipeline flagged this question. Rewrite `q10.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q10.** Assume Sloane is charged with Vance's murder under the *Pinkerton* doctrine, based solely on her membership in the fentanyl distribution network. Which of the following is her strongest defense against this specific charge?

(a) The murder of Vance was a spontaneous response to a personal insult at a diner and therefore fell entirely outside the reasonably foreseeable scope of the drug distribution conspiracy. <!-- correct -->
(b) She effectively and legally withdrew from the criminal conspiracy by ensuring she was not physically present at the diner when Deacon covertly poisoned the rival distributor's coffee cup.
(c) The *Pinkerton* doctrine is categorically and universally inapplicable to intentional homicide offenses because such crimes inherently require a distinct showing of actual malice aforethought by the defendant.
(d) She cannot be held criminally liable for the homicide because she did not personally perform the physical overt act of pouring the lethal poison into the victim's beverage.
(e) The overarching agreement to manufacture and distribute fentanyl was implicitly dissolved the moment Deacon made the unilateral decision to utilize poison instead of conventional firearms against a rival.

**Answer:** (a)

**Explanation:** (a) is correct. The *Pinkerton* doctrine holds a conspirator liable only for substantive offenses committed by co-conspirators that are both in furtherance of the conspiracy and reasonably foreseeable as a necessary or natural consequence of the agreement. Deacon poisoning Vance over a personal spitting insult at a diner is a frolic and detour that falls outside the scope of an agreement to manufacture and sell fentanyl. (b) is wrong because withdrawal requires an affirmative act to communicate abandonment or thwart the conspiracy, not merely physical absence. (c) is wrong because *Pinkerton* can apply to intentional homicide if it was a foreseeable part of the conspiracy (e.g., a hitman ring). (d) is wrong because *Pinkerton* expressly creates liability for acts the defendant did *not* personally perform. (e) is wrong because a co-conspirator's unilateral, out-of-scope act does not automatically dissolve the underlying agreement.

**Tags:** chapters: [19], topics: [conspiracy, Pinkerton scope], difficulty: medium, cognitive: application

**Grounding:** Chapter 19, scope-procedural-stakes

<!-- audit: SHOULD FIX
check 1: pass
check 2: pass
check 3: pass
check 4: fails. The stem fails to provide the basic facts of the murder, leaving them to be introduced piecemeal (and contradictorily) in the options. Option (a) implies a spontaneous personal insult, whereas options (b) and (e) suggest the victim was a "rival distributor," which might actually make the killing foreseeable/in furtherance of the drug conspiracy. While (a) is the only legally sound statement of a defense, failing to establish the facts in the stem creates unnecessary cognitive load and ambiguity.
check 5: pass
check 6: pass
check 7: pass
check 8: pass
Recommended fix: Move the core facts of the homicide into the stem. E.g., "Sloane and Deacon are members of a fentanyl distribution network. Without Sloane's knowledge, Deacon spontaneously poisons Vance at a diner in response to a personal insult. Assume Sloane is charged with Vance's murder under the Pinkerton doctrine based solely on her membership in the network. Which of the following is her strongest defense...?" Then trim the distractors to just refer to these established facts.
-->
