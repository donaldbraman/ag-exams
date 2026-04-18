# Fix Guidance for q02

The QA pipeline flagged this question. Rewrite `q02.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q2.** Assume Marcus is prosecuted in a jurisdiction that follows the rule of *United States v. Dingwall* or *United States v. Contento-Pachon* regarding duress. Will Vance's threat of a midnight execution satisfy the imminence requirement for duress?

(a) The defense fails categorically because the threat was scheduled for midnight, meaning Vance was not physically present to enforce it during the arson.
(b) The defense may survive because strict physical proximity is not required if Marcus reasonably believed reporting to corrupt police was futile. <!-- correct -->
(c) The defense fails categorically because duress is never available to excuse the deliberate destruction of another person's private property.
(d) The defense may survive because the threat targeted Marcus's family, which automatically waives the traditional imminence requirement for all subsequent crimes.
(e) The defense fails categorically because Marcus could have relocated his family to a safehouse before the midnight deadline ultimately expired.

**Answer:** (b)

**Explanation:** Under the traditional rule, imminence requires the threat to be immediate and physically present. However, modern jurisdictions following cases like *Dingwall* or *Contento-Pachon* recognize that a continuous threat, combined with a reasonable belief that authorities are corrupt and cannot help, can satisfy the imminence requirement even if the threat is hours away and the coercer is not physically present. (a) is wrong because modern majority circuits reject the strict physical proximity test. (c) is wrong because duress is a defense to property crimes like arson. (d) is wrong because targeting family does not automatically waive the imminence requirement; it satisfies the target scope element. (e) is wrong because his belief in the futility of seeking help due to police corruption creates a jury question on reasonable alternatives.

**Tags:** chapters: [21], topics: [duress, imminence], difficulty: hard, cognitive: application

**Grounding:** Chapter 21 (Necessity and Duress), duress-imminence-proximity and duress-corrupt-authorities refinements.

<!-- audit: MUST FIX
check 1: pass
check 2: pass
check 3: pass
check 4: MUST FIX. The stem entirely lacks the factual scenario relied upon by the options and the explanation. It fails to state when the arson occurs relative to midnight, that the threat was against Marcus's family, or that Marcus believed the police were corrupt. Students cannot evaluate the application of the law without these facts present in the stem.
check 5: pass
check 6: pass
check 7: pass
Recommended fix: Provide the missing factual scenario in the stem. For example: "At noon, Vance orders Marcus to commit arson, threatening to execute Marcus's family at midnight if he refuses. Vance is not physically present during the arson. Marcus complies because he reasonably believes the local police are on Vance's payroll and reporting the threat would be futile." Modify the options to test the application of the doctrine to these facts rather than introducing the facts as hypotheticals.
-->

## Issue 2 — argpass-opus

**Q2.** Assume Marcus is prosecuted in a jurisdiction that follows the rule of *United States v. Dingwall* or *United States v. Contento-Pachon* regarding duress. Will Vance's threat of a midnight execution satisfy the imminence requirement for duress?

(a) The defense fails categorically because the threat was scheduled for midnight, meaning Vance was not physically present to enforce it during the arson.
(b) The defense may survive because strict physical proximity is not required if Marcus reasonably believed reporting to corrupt police was futile. <!-- correct -->
(c) The defense fails categorically because duress is never available to excuse the deliberate destruction of another person's private property.
(d) The defense may survive because the threat targeted Marcus's family, which automatically waives the traditional imminence requirement for all subsequent crimes.
(e) The defense fails categorically because Marcus could have relocated his family to a safehouse before the midnight deadline ultimately expired.

**Answer:** (b)

**Explanation:** Under the traditional rule, imminence requires the threat to be immediate and physically present. However, modern jurisdictions following cases like *Dingwall* or *Contento-Pachon* recognize that a continuous threat, combined with a reasonable belief that authorities are corrupt and cannot help, can satisfy the imminence requirement even if the threat is hours away and the coercer is not physically present. (a) is wrong because modern majority circuits reject the strict physical proximity test. (c) is wrong because duress is a defense to property crimes like arson. (d) is wrong because targeting family does not automatically waive the imminence requirement; it satisfies the target scope element. (e) is wrong because his belief in the futility of seeking help due to police corruption creates a jury question on reasonable alternatives.

**Tags:** chapters: [21], topics: [duress, imminence], difficulty: hard, cognitive: application

**Grounding:** Chapter 21 (Necessity and Duress), duress-imminence-proximity and duress-corrupt-authorities refinements.

<!-- argument-pass: SHOULD FIX
(a) Argument-for: Under the traditional common law rule, duress requires the threat to be immediate and the coercer to be physically present at the time of the offense. Option (a) accurately channels this strict requirement, asserting that a threat scheduled for "midnight" lacks the requisite immediacy. A student could argue that even in modern jurisdictions, a timeline extending hours into the future provides too much temporal distance. Therefore, the lack of physical presence means the defense must fail categorically as a matter of law.
(b) Argument-for: *United States v. Contento-Pachon* established that the imminence requirement can be satisfied by a continuous threat if the defendant reasonably believes that seeking law enforcement help is futile. Option (b) correctly tracks this modern rule, noting that strict physical proximity is not required under these circumstances. Because Marcus reasonably believed the corrupt police would not help him, his failure to report the threat does not defeat the imminence element. This properly leaves the question of imminence and reasonable alternatives to the jury.
(c) Argument-for: Duress is historically circumscribed by the severity of the crime committed, most notably being unavailable as a defense to intentional murder. A student could argue that the deliberate destruction of private property (such as arson) carries such grave risks to human life and public order that it is similarly excluded. By stating the defense is "never available" for such intentional property destruction, option (c) appeals to the notion that public policy strictly forbids this conduct. Thus, the defense categorically fails.
(d) Argument-for: Modern duress doctrine explicitly expands the scope of the defense to cover threats directed against a defendant’s immediate family. Option (d) asserts that because the threat targeted Marcus's family, the traditional imminence requirement is "automatically waived." A student could interpret the overwhelming policy weight given to family protection as entirely superseding temporal requirements, reasoning that any threat to loved ones is inherently coercive. This would mean the traditional imminence hurdle vanishes.
(e) Argument-for: To successfully claim duress, a defendant must lack any reasonable, legal alternative to committing the crime. Option (e) posits that the time gap before the "midnight deadline" provided a clear window to relocate his family to a safehouse. A student could argue that the mere existence of this time gap establishes, as a matter of law, that Marcus failed to exhaust his legal alternatives. Therefore, the defense fails categorically because a reasonable alternative was objectively available.

Head-to-head: Option (b) is the clear correct answer because it accurately applies the *Contento-Pachon* standard, where a continuous threat combined with a reasonable belief in police futility creates a jury question regarding imminence. Distractor (a) contains a falsifiable legal error by stating the defense fails "categorically" due to a lack of physical presence, directly contradicting the specified jurisdictions' rules. Distractor (c) relies on the objectively false legal proposition that duress is "never available" for deliberate destruction of property. Distractor (d) offers the extreme, falsifiable legal claim that a threat to family "automatically waives" the imminence requirement for "all subsequent crimes." Distractor (e) asserts the defense fails "categorically," but it grounds this failure in a presumed factual conclusion ("because Marcus could have relocated") rather than stating a pure, falsifiable legal rule about time gaps. It should be revised to contain a purely explicit legal error.

Falsifiable claim per distractor:
- (a): "fails categorically because... Vance was not physically present" — wrong because *Contento-Pachon* explicitly rejects the strict physical proximity requirement.
- (c): "never available to excuse the deliberate destruction of another person's private property" — wrong because duress is generally available for property crimes, including arson.
- (d): "automatically waives the traditional imminence requirement for all subsequent crimes" — wrong because targeting family satisfies the target scope element but does not waive the temporal imminence requirement.
- (e): "fails categorically because Marcus could have relocated his family" — wrong because it improperly treats a disputed factual inference as a categorical legal bar.

Recommended fix: Change (e) to: "The defense fails categorically because a multi-hour delay before a deadline automatically establishes that the defendant had a reasonable legal alternative."
-->
