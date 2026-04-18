# Fix Guidance for q08

The QA pipeline flagged this question. Rewrite `q08.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

<!-- audit: MUST FIX -->

**Safety Block Triggered.** The previous version of this question was blocked by Gemini's safety filters as unsafe. Please rewrite the fact pattern to reduce the risk of unsafe content blocking.

Error: Model returned empty or blocked response.

## Issue 2 — argpass-sonnet

**Q8.** Assume that, whether or not Marcus satisfies the elements of attempted arson, he raises the defense of voluntary abandonment because he ran away after hearing the police sirens. Will the defense succeed?

(a) The defense fails because abandoning a crime due to the fear of immediate police apprehension is motivated by unexpected resistance, not a genuine change of heart. <!-- correct -->
(b) The defense fails because the doctrine of voluntary abandonment is completely unrecognized in any jurisdiction that has adopted the Model Penal Code framework.
(c) The defense succeeds because Marcus subjectively believed that continuing the crime was impossible once he heard the sirens approaching the immediate area.
(d) The defense succeeds because running away fully physically prevented the completion of the target offense before any substantial harm could actually occur.
(e) The defense succeeds because Marcus completely severed his ties with the conspiracy prior to arriving at the target location and deploying the accelerants.

**Answer:** (a)

**Explanation:** (a) is correct. The defense of voluntary abandonment (or renunciation) requires a complete and voluntary renunciation of criminal purpose, representing a genuine change of heart. The defense is statutorily defeated if the abandonment is motivated in whole or in part by circumstances that increase the probability of detection or apprehension—such as hearing police sirens. (b) is wrong because the MPC explicitly recognizes and codified the voluntary abandonment defense. (c) is wrong because if the abandonment is motivated by a perceived impossibility or heightened risk of arrest, it is legally defined as involuntary. (d) is wrong because the defense evaluates the psychological voluntariness of the withdrawal, not merely whether the defendant physically succeeded in preventing the target harm. (e) is wrong because severing ties due to the immediate threat of police capture does not qualify as the legally voluntary, internally motivated change of heart required by the doctrine.

**Tags:** chapters: [17], topics: [voluntary abandonment], difficulty: medium, cognitive: application
**Grounding:** Chapter 17, Voluntary Abandonment Doctrine

<!-- argument-pass: SHOULD FIX
(a) Argument-for: Under the MPC and common law, voluntary abandonment requires a complete and voluntary renunciation of criminal purpose. If the abandonment is triggered by external circumstances that increase the risk of apprehension (like police sirens), it is legally involuntary. A student would correctly deduce that Marcus lacked a genuine change of heart, making this the correct choice.
(b) Argument-for: A student might recall that under traditional common law, once a "substantial step" was taken, the crime of attempt was complete and could not be abandoned. If the student falsely assumes the Model Penal Code maintained this strict, unforgiving common-law approach without exception, they would choose this option.
(c) Argument-for: A student could argue that a subjective belief in impossibility terminates the mens rea to continue. If Marcus thought completing the arson was impossible due to the sirens, a student might incorrectly conclude that this subjective realization validates his withdrawal and successfully satisfies the requirements for abandonment.
(d) Argument-for: This option appeals to the utilitarian policy rationale behind the abandonment defense: incentivizing actors to stop before harm occurs. A student might argue that because Marcus physically prevented the substantive offense of arson from occurring, the law prioritizes this actual prevention of harm over the psychological purity of his motives.
(e) Argument-for: A student might conflate the doctrine of voluntary abandonment in attempt with the rules for withdrawal from a conspiracy. By focusing on Marcus "completely severing his ties" prior to the ultimate act (deploying accelerants), a student could argue he met the threshold for effectively withdrawing from the criminal enterprise before the point of no return.

Head-to-head: 
Option (a) correctly identifies that the defense fails due to a lack of a genuine change of heart, though its phrasing awkwardly conflates "fear of immediate police apprehension" with "unexpected resistance" (sirens increase the risk of apprehension, but "resistance" usually refers to physical difficulty or victim opposition). Option (b) contains an excellent, highly falsifiable claim about the MPC. Options (c), (d), and (e) correctly present false legal applications (claiming the defense succeeds when it legally fails), but they lack the absolute locking words required by the strict close-call standard, leaving them as mere misapplications rather than locked, categorically false doctrinal claims. Additionally, (e) introduces "conspiracy," which is a distinct crime not mentioned in the prompt.

Falsifiable claim per distractor:
- (b): "completely unrecognized in any jurisdiction that has adopted the Model Penal Code framework" — wrong because MPC § 5.01(4) explicitly created and codified the voluntary abandonment defense.
- (c): "The defense succeeds because Marcus subjectively believed..." — wrong because an abandonment motivated by the belief that apprehension is imminent is legally involuntary, meaning the defense categorically fails.
- (d): "The defense succeeds because running away fully physically prevented the completion..." — wrong because physical prevention alone is insufficient; the defense requires a legally voluntary motive.
- (e): "The defense succeeds because Marcus completely severed his ties with the conspiracy..." — wrong because severing ties due to an increased risk of police capture is legally involuntary.

Recommended fix: 
1. Refine (a) to fix the "unexpected resistance" phrasing: "(a) The defense fails because abandoning a crime due to the fear of immediate police apprehension negates the voluntariness requirement, as it does not reflect a genuine change of heart."
2. Add absolute lock words to the distractors to meet the close-call standard. For example:
- (c): "...succeeds solely because Marcus subjectively believed..."
- (d): "...succeeds automatically because running away fully physically prevented..."
- (e): "...succeeds because physically withdrawing prior to deploying accelerants categorically guarantees an abandonment defense regardless of motive."
-->

## Issue 3 — argpass-opus

**Q8.** Assume that, whether or not Marcus satisfies the elements of attempted arson, he raises the defense of voluntary abandonment because he ran away after hearing the police sirens. Will the defense succeed?

(a) The defense fails because abandoning a crime due to the fear of immediate police apprehension is motivated by unexpected resistance, not a genuine change of heart. <!-- correct -->
(b) The defense fails because the doctrine of voluntary abandonment is completely unrecognized in any jurisdiction that has adopted the Model Penal Code framework.
(c) The defense succeeds because Marcus subjectively believed that continuing the crime was impossible once he heard the sirens approaching the immediate area.
(d) The defense succeeds because running away fully physically prevented the completion of the target offense before any substantial harm could actually occur.
(e) The defense succeeds because Marcus completely severed his ties with the conspiracy prior to arriving at the target location and deploying the accelerants.

**Answer:** (a)

**Explanation:** (a) is correct. The defense of voluntary abandonment (or renunciation) requires a complete and voluntary renunciation of criminal purpose, representing a genuine change of heart. The defense is statutorily defeated if the abandonment is motivated in whole or in part by circumstances that increase the probability of detection or apprehension—such as hearing police sirens. (b) is wrong because the MPC explicitly recognizes and codified the voluntary abandonment defense. (c) is wrong because if the abandonment is motivated by a perceived impossibility or heightened risk of arrest, it is legally defined as involuntary. (d) is wrong because the defense evaluates the psychological voluntariness of the withdrawal, not merely whether the defendant physically succeeded in preventing the target harm. (e) is wrong because severing ties due to the immediate threat of police capture does not qualify as the legally voluntary, internally motivated change of heart required by the doctrine.

**Tags:** chapters: [17], topics: [voluntary abandonment], difficulty: medium, cognitive: application
**Grounding:** Chapter 17, Voluntary Abandonment Doctrine

<!-- argument-pass: SHOULD FIX
(a) Argument-for: Under the MPC § 5.01(4), the defense of voluntary abandonment fails if the withdrawal is motivated by circumstances that increase the probability of detection or apprehension. Hearing police sirens falls exactly into this category. Thus, a student would rightly conclude that Marcus’s withdrawal was externally coerced by the threat of arrest, legally negating the requirement for an internally motivated "genuine change of heart." 
(b) Argument-for: A student might recall that under strict traditional common law, abandonment was often not recognized as a defense once an attempt crossed the line of mere preparation. Conflating this historical strictness with the MPC, they could erroneously argue that the MPC outright rejects voluntary abandonment across all jurisdictions to maximize deterrence.
(c) Argument-for: A student could argue that if Marcus subjectively believed completing the arson was rendered impossible by the approaching police, he no longer possessed the requisite continuing intent or ability to act. They might wrongly conclude that this subjective belief in impossibility legally satisfies the abandonment defense because he voluntarily chose to yield to that impossibility.
(d) Argument-for: Relying on the public policy rationale of the defense—which aims to incentivize offenders to halt their criminal conduct before harm is done—a student could argue that physical prevention of the crime is the paramount requirement. Since Marcus ran away before any substantial harm occurred, they might conclude this physical withdrawal alone automatically guarantees the defense's success.
(e) Argument-for: Assuming Marcus was operating within a conspiracy, a student might focus on the actus reus of withdrawal. They could argue that by leaving the scene prior to deploying any accelerants, Marcus successfully and completely severed his ties to the target offense, thereby fulfilling the requirements for the abandonment defense.

Head-to-head: 
Option (a) correctly concludes the defense fails and captures the core rationale: external pressures defeat the "genuine change of heart" requirement. However, (a) contains slightly inaccurate phrasing by equating police sirens with "unexpected resistance"; statutorily, sirens are "circumstances increasing the risk of apprehension," whereas "resistance" generally implies a physical impediment to accomplishment (e.g., a victim fighting back). The distractors all contain solid, falsifiable errors. Option (b) makes a categorically false claim about the Model Penal Code. Options (c), (d), and (e) all explicitly reach the wrong legal conclusion ("The defense succeeds") while relying on falsifiable legal reasoning, such as physical prevention or subjective impossibility overriding the requirement for an internally motivated withdrawal. 

Falsifiable claim per distractor:
- (b): "completely unrecognized in any jurisdiction that has adopted the Model Penal Code framework" — wrong because MPC § 5.01(4) explicitly codifies and recognizes the affirmative defense of renunciation of criminal purpose.
- (c): "The defense succeeds because Marcus subjectively believed that continuing the crime was impossible" — wrong because an abandonment motivated by the perceived impossibility of completion due to an external threat (police) makes the abandonment legally involuntary.
- (d): "The defense succeeds because running away fully physically prevented the completion" — wrong because physical prevention alone is legally insufficient; the doctrine strictly requires the psychological component of a completely voluntary, uncoerced change of heart.
- (e): "The defense succeeds because Marcus completely severed his ties" — wrong because severing ties in response to an immediate threat of police capture does not meet the legal threshold for a voluntary abandonment.

Recommended fix: Adjust the terminology in (a) to precisely match the statutory categories. Change (a) to: "The defense fails because abandoning a crime due to the fear of immediate police apprehension is motivated by an increased risk of detection, not a genuine change of heart."
-->
