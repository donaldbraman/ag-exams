# Fix Guidance for q08

The QA pipeline flagged this question. Rewrite `q08.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q8.** Assume all four men are charged with conspiracy to manufacture a controlled substance. Which of the following accurately describes their liability under the general common law and statutory requirements for conspiracy?

(a) They are guilty because they formed a mutual agreement to commit an unlawful act and completed an overt act by renting the industrial warehouse. <!-- correct -->
(b) They are guilty because the mere act of meeting in the local diner to discuss the potential drug operation fully satisfied the bilateral agreement requirement.
(c) They are not guilty because the actual manufacturing of the synthetic opioids was definitively thwarted by the reactor malfunction and the subsequent police intervention.
(d) They are not guilty because Dante maintained exclusive possession of the safe's key, demonstrating that there was no genuine meeting of the minds among them.
(e) They are not guilty because criminal conspiracy strictly requires the completion of the target offense to properly merge the preparatory agreement into the substantive crime.

**Answer:** (a)

**Explanation:** A criminal conspiracy requires an agreement between two or more persons to commit an unlawful act, plus (in most modern jurisdictions) an overt act in furtherance of the agreement. The four men explicitly agreed to manufacture drugs, and pooling money/renting the warehouse constitutes an overt act. (b) is incorrect because while meeting at a diner might establish an agreement, virtually all modern statutes require an overt act beyond mere discussion. (c) is incorrect because conspiracy is an inchoate crime that is complete the moment the agreement and overt act occur; failure of the target offense is irrelevant. (d) is incorrect because division of labor (Dante holding the key) does not negate the existence of a mutual agreement to operate the lab together. (e) is incorrect because conspiracy does not merge with the completed target offense; a defendant can be convicted of both the conspiracy and the completed substantive crime.

**Tags:** chapters: [19], topics: [conspiracy, agreement, overt act, inchoate offenses], difficulty: easy, cognitive: application

**Grounding:** Chapter 19: agreement-inference, overt-act-minimal

<!-- audit: MUST FIX
check 1: pass
check 2: pass
check 3: pass
check 4: MUST FIX. The question refers to "all four men," "renting the industrial warehouse," and a "reactor malfunction," but these facts are completely absent from the stem. If this question is drawn from a broader fact pattern, those facts must be included in the stem for the question to stand alone.
check 5: SHOULD FIX. Asking for liability under "the general common law and statutory requirements" conflates two regimes that actually differ: strict common law does not require an overt act, whereas modern statutes generally do. Specify "majority modern rule" or "modern statutory requirements" to avoid ambiguity and clearly invalidate (b).
check 6: pass
check 7: pass
check 8: pass
Recommended fix: Provide the missing factual scenario in the stem so students know who the four men are and what they did. Change the jurisdictional framing to "majority modern rule" rather than combining common law and statutory requirements.
-->
