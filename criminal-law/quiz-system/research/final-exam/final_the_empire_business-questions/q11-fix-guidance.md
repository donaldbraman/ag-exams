# Fix Guidance for q11

The QA pipeline flagged this question. Rewrite `q11.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q11.** Assume Dominic is convicted of felony murder for Victor's death. Does the underlying felony (armed extortion/robbery) merge with the homicide, preventing a felony murder conviction?

(a) Yes, it merges, because the robbery involved the threat of physical violence, making it an integral part of the resulting homicide rather than an independent felonious act.
(b) No, it does not merge, because the robbery had an independent felonious purpose—obtaining the cash—separate and distinct from the physical act of killing the restaurant owner. <!-- correct -->
(c) Yes, it merges, because the shooting occurred in the exact same location and time as the robbery, eliminating any meaningful temporal break between the two distinct crimes.
(d) No, it does not merge, because all crimes committed with firearms are statutorily exempt from the merger doctrine under modern felony murder reform rules in most jurisdictions.
(e) Yes, it merges, because Dominic only fired his weapon after the robbery attempt had already failed, meaning the two events are legally indistinguishable acts under the merger doctrine.

**Answer:** (b)

**Explanation:** Under the merger doctrine (independent felonious purpose test), an underlying felony does not merge with the homicide if it has an independent purpose separate from the killing. Armed robbery and extortion have the independent purpose of acquiring property, so they can serve as valid predicate offenses for felony murder. (a) is incorrect because the threat of violence in a robbery is a means to acquire property, not an intent to commit the homicide itself. (c) is incorrect because temporal and spatial proximity are required for the felony murder rule to apply in the first place; they do not trigger merger. (d) is incorrect because there is no blanket statutory exemption for all firearm crimes from the merger doctrine. (e) is incorrect because a death occurring during the immediate flight or failure of a robbery is still considered part of the continuous transaction.

**Tags:** chapters: [14], topics: [felony murder, merger doctrine, independent purpose], difficulty: medium, cognitive: application

**Grounding:** Merger doctrine; Independent felonious purpose test

<!-- audit: MUST FIX
<check 1>: pass. Robbery and extortion have an independent felonious purpose (obtaining property) and therefore do not merge with the homicide under the standard doctrine.
<check 2>: MUST FIX. The stem begins, "Assume Dominic is convicted of felony murder..." and then asks "Does the underlying felony merge..., preventing a felony murder conviction?" By stipulating that he is *convicted*, the stem inadvertently leaks the answer (if he's convicted, merger logically couldn't have prevented the conviction). A savvy student can answer correctly purely on test-taking logic.
<check 3>: pass. The explanation accurately describes the independent felonious purpose test.
<check 4>: pass. (Assuming this is a child question attached to a master fact pattern containing the details about Dominic, Victor, the restaurant, and the cash). 
<check 5>: SHOULD FIX. The explanation relies on the "independent felonious purpose test," but the stem doesn't specify this standard. While this is the primary test for merger taught in casebooks, adding it to the stem ensures students know exactly which legal framework to apply, satisfying the pedagogical principle against rote jurisdictional memorization.
<check 6>: pass. Does not bleed into excluded topics.
<check 7>: pass. Grounded in Ch 14 (`merger-independent-purpose`).
Recommended fix: Change "Assume Dominic is convicted of felony murder" to "Assume Dominic is charged with felony murder". Additionally, clarify the stem to prompt the specific doctrine: "Under the independent felonious purpose test, does the underlying felony (armed extortion/robbery) merge with the homicide..."
-->

## Issue 2 — edge-case

**Q11.** Assume Dominic is convicted of felony murder for Victor's death. Does the underlying felony (armed extortion/robbery) merge with the homicide, preventing a felony murder conviction?

(a) Yes, it merges, because the robbery involved the threat of physical violence, making it an integral part of the resulting homicide rather than an independent felonious act.
(b) No, it does not merge, because the robbery had an independent felonious purpose—obtaining the cash—separate and distinct from the physical act of killing the restaurant owner. <!-- correct -->
(c) Yes, it merges, because the shooting occurred in the exact same location and time as the robbery, eliminating any meaningful temporal break between the two distinct crimes.
(d) No, it does not merge, because all crimes committed with firearms are statutorily exempt from the merger doctrine under modern felony murder reform rules in most jurisdictions.
(e) Yes, it merges, because Dominic only fired his weapon after the robbery attempt had already failed, meaning the two events are legally indistinguishable acts under the merger doctrine.

**Answer:** (b)

**Explanation:** Under the merger doctrine (independent felonious purpose test), an underlying felony does not merge with the homicide if it has an independent purpose separate from the killing. Armed robbery and extortion have the independent purpose of acquiring property, so they can serve as valid predicate offenses for felony murder. (a) is incorrect because the threat of violence in a robbery is a means to acquire property, not an intent to commit the homicide itself. (c) is incorrect because temporal and spatial proximity are required for the felony murder rule to apply in the first place; they do not trigger merger. (d) is incorrect because there is no blanket statutory exemption for all firearm crimes from the merger doctrine. (e) is incorrect because a death occurring during the immediate flight or failure of a robbery is still considered part of the continuous transaction.

**Tags:** chapters: [14], topics: [felony murder, merger doctrine, independent purpose], difficulty: medium, cognitive: application

**Grounding:** Merger doctrine; Independent felonious purpose test

<!-- edge-case-audit: SHOULD FIX
1. Fact Pattern Booby Traps: pass
2. Cross-Doctrine Clashes: pass
3. Cross-Question Spoilers: The prompt contains a logical contradiction that accidentally acts as a spoiler for Q10. It asks to "Assume Dominic is convicted of felony murder", but then asks if the merger doctrine "prevents a felony murder conviction". If he is convicted, it obviously didn't prevent it. Furthermore, assuming a conviction spoils Q10 (which evaluates whether felony murder applies). 
Recommended fix: Change the opening sentence to: "Assume Dominic is charged with felony murder for Victor's death."
-->
