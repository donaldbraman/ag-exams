# Fix Guidance for q16

The QA pipeline flagged this question. Rewrite `q16.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q16.** Silas is charged with possession of the 500 grams of fentanyl found in the lockbox in his girlfriend's trunk. Based on the elements of constructive possession, is there sufficient evidence to convict him?

(a) Yes, because his mere physical presence in a vehicle containing narcotics automatically establishes constructive possession as a matter of law.
(b) Yes, because his admission of knowledge, combined with his sole occupancy of the vehicle, allows a jury to infer he had the power to control it. <!-- correct -->
(c) No, because he did not have the key on his person, which legally precludes him from exercising the requisite dominion and control over the drugs.
(d) No, because the vehicle was registered to his girlfriend, meaning only she could be legally charged with constructive possession of items hidden inside it.
(e) Yes, because strict liability applies to Schedule I narcotics, rendering the specific elements of awareness and physical control legally irrelevant to the final charge.

**Answer:** (b)

**Explanation:** Constructive possession requires the prosecution to prove the defendant had both awareness of the contraband and the power and intent to exercise control over it. Silas's explicit admission of knowledge, combined with his sole occupancy of the vehicle, allows a jury to infer he had the requisite power to control the lockbox, even if he lacked the key at that exact moment. (a) is wrong because mere presence is insufficient without proof of knowledge and control. (c) is wrong because physical possession of a key is not an absolute legal requirement for controlling a box (e.g., he could carry the box away). (d) is wrong because legal ownership of the vehicle is not required to possess items inside it. (e) is wrong because strict liability does not eliminate the foundational possession elements.

**Tags:** chapters: [15], topics: [constructive possession, drugs], difficulty: medium, cognitive: application

**Grounding:** Chapter 15 (Drugs and Guns), cp-awareness-control refinement.

<!-- audit: MUST FIX
check 1: fail - The correct answer is factually unsupported by the stem, rendering it unpickable for a careful student.
check 2: pass - No other option becomes doctrinally defensible, but a smart student would rightly challenge the entire question. 
check 3: fail - The explanation references "explicit admission of knowledge" and "sole occupancy," which do not appear in the stem.
check 4: fail - The stem completely lacks the necessary facts. It never states that Silas was the sole occupant of the vehicle, nor does it mention that he admitted knowledge of the fentanyl. Option (b) and the explanation rely entirely on these phantom facts.
check 5: pass
check 6: pass
check 7: pass
Recommended fix: Add the missing facts to the stem. For example: "Silas is pulled over while driving his girlfriend's car alone. He admits to police that he knew there was 500 grams of fentanyl in a lockbox in the trunk, though he does not have the key. He is charged with possession..."
-->
