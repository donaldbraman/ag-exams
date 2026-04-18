# Fix Guidance for q04

The QA pipeline flagged this question. Rewrite `q04.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

<!-- audit: MUST FIX -->

**Safety Block Triggered.** The previous version of this question was blocked by Gemini's safety filters as unsafe. Please rewrite the fact pattern to reduce the risk of unsafe content blocking.

Error: Model returned empty or blocked response.

## Issue 2 — argpass-sonnet

**Q4.** Assume that, whether or not Marcus is liable for the first two months, he asserts a duress defense for routing the trucks during the subsequent four months after Carmine's threat to put him in a compactor. Will Marcus's duress defense likely succeed?

(a) Yes, because Carmine's violent threat to put him in a compactor would cause a person of reasonable firmness to yield and commit the crime.
(b) Yes, because Marcus was forced to commit the ongoing logistical acts under a credible and severe threat of imminent serious bodily harm or death.
(c) No, because the affirmative defense of duress is categorically unavailable for any federal offenses involving the commercial distribution of controlled substances.
(d) No, because the threat to put him in a compactor was not sufficiently imminent during the four full months he continued routing the trucks. <!-- correct -->
(e) No, because Marcus voluntarily assumed the risk of coercion and violence when he knowingly took a managerial job at the Pinnacle Waste front operation.

**Answer:** (d)

**Explanation:** To succeed on a duress defense, the defendant must face an imminent threat of death or serious bodily harm. Carmine's threat to put Marcus in a compactor was made once, and Marcus continued routing the trucks for four months without seeking help. A threat extending over four months lacks the strict imminence required to justify continuous criminal conduct. (a) is wrong because it addresses the severity of the threat but ignores the failure of the imminence requirement. (b) is wrong because the lengthy time period defeats the claim that he was forced by an immediate, unavoidable threat. (c) is wrong because duress is generally available for drug offenses; it is typically only barred for intentional murder. (e) is wrong because taking a legitimate managerial job does not constitute voluntary assumption of the risk of organized crime coercion.

**Tags:** chapters: [21], topics: [duress, imminence], difficulty: easy, cognitive: application

**Grounding:** Chapter 21, Duress requirements

<!-- argument-pass: SHOULD FIX
(a) Argument-for: Under the Model Penal Code, duress requires a threat that a person of reasonable firmness would be unable to resist. Carmine's threat to put Marcus in a compactor is an extreme threat of unlawful physical force. A student could argue that this severe threat squarely meets the "reasonable firmness" test, making the defense successful under the MPC's broader formulation.
(b) Argument-for: Duress generally requires an imminent threat of severe harm. A student could argue that a threat from a powerful organized crime figure is continuously "imminent" because Carmine has the means to execute it at any moment. Therefore, Marcus acted under a continuous threat of imminent death or serious bodily injury for the entire four months.
(c) Argument-for: Duress is traditionally unavailable as a defense to intentional murder. A student might incorrectly assume that public policy creates a similar categorical bar for major federal offenses involving commercial drug distribution. Under this logic, Congress would have intended to prevent cartel subordinates from routinely escaping punishment by claiming coercion, making the defense categorically unavailable.
(d) Argument-for: Duress requires that the threat of death or serious bodily injury be imminent, leaving no reasonable alternative but to comply. Over a continuous four-month period, Marcus had numerous opportunities to seek help from law enforcement or flee the jurisdiction. Because he failed to pursue any reasonable avenue of escape over this extended timeframe, the threat lacked the requisite strict imminence, rendering the defense invalid.
(e) Argument-for: Under the Model Penal Code, the duress defense is unavailable if the defendant recklessly placed himself in a situation where coercion was probable. A student could interpret the phrase "knowingly took a managerial job at the Pinnacle Waste front operation" to mean Marcus actually knew the business was a criminal front. Under that reading, he voluntarily assumed the risk of mob violence, which would legally defeat his duress claim.

Head-to-head: (d) is the strongest and keyed answer because it correctly applies the requirement that a threat must be sufficiently imminent to justify continuing criminal acts, and a four-month delay with avenues for escape defeats this. (a) correctly states the MPC severity standard but ignores the fatal timeframe, making it an implicit omission rather than an explicit falsity. (b) contains a factually false claim that an ongoing four-month threat remains "imminent." (c) relies on a fabricated categorical rule. (e) is tricky because "knowingly took... at the... front operation" is ambiguous; if it implies Marcus knew it was a criminal front, it might actually be legally correct under the MPC's reckless placement rule, contradicting the explanation that the job was "legitimate."

Falsifiable claim per distractor:
- (a): "Yes, because Carmine's violent threat... would cause a person of reasonable firmness to yield" — wrong because it concludes the defense succeeds based solely on the severity, implicitly omitting the failure of the timeframe/escape element.
- (b): "threat of imminent serious bodily harm" — wrong because an ongoing four-month threat is not legally "imminent."
- (c): "categorically unavailable for any federal offenses involving the commercial distribution of controlled substances" — wrong because no such categorical exception exists for drug offenses.
- (e): "voluntarily assumed the risk of coercion... when he knowingly took a managerial job" — wrong because taking a legitimate job does not constitute assumption of the risk, although the word "knowingly" creates problematic ambiguity.

Recommended fix: Lock (a) to fix the implicit omission: "Yes, because the severity of Carmine's threat automatically establishes the defense, regardless of the four months Marcus continued the crimes." Clarify (e) to eliminate the ambiguity of "knowingly": "No, because Marcus automatically assumed the risk of violent coercion solely by accepting a legitimate managerial job that turned out to be a front."
-->

## Issue 3 — argpass-opus

**Q4.** Assume that, whether or not Marcus is liable for the first two months, he asserts a duress defense for routing the trucks during the subsequent four months after Carmine's threat to put him in a compactor. Will Marcus's duress defense likely succeed?

(a) Yes, because Carmine's violent threat to put him in a compactor would cause a person of reasonable firmness to yield and commit the crime.
(b) Yes, because Marcus was forced to commit the ongoing logistical acts under a credible and severe threat of imminent serious bodily harm or death.
(c) No, because the affirmative defense of duress is categorically unavailable for any federal offenses involving the commercial distribution of controlled substances.
(d) No, because the threat to put him in a compactor was not sufficiently imminent during the four full months he continued routing the trucks. <!-- correct -->
(e) No, because Marcus voluntarily assumed the risk of coercion and violence when he knowingly took a managerial job at the Pinnacle Waste front operation.

**Answer:** (d)

**Explanation:** To succeed on a duress defense, the defendant must face an imminent threat of death or serious bodily harm. Carmine's threat to put Marcus in a compactor was made once, and Marcus continued routing the trucks for four months without seeking help. A threat extending over four months lacks the strict imminence required to justify continuous criminal conduct. (a) is wrong because it addresses the severity of the threat but ignores the failure of the imminence requirement. (b) is wrong because the lengthy time period defeats the claim that he was forced by an immediate, unavoidable threat. (c) is wrong because duress is generally available for drug offenses; it is typically only barred for intentional murder. (e) is wrong because taking a legitimate managerial job does not constitute voluntary assumption of the risk of organized crime coercion.

**Tags:** chapters: [21], topics: [duress, imminence], difficulty: easy, cognitive: application

**Grounding:** Chapter 21, Duress requirements

<!-- argument-pass: SHOULD FIX
(a) Argument-for: Under Model Penal Code § 2.09, strict imminence is not an absolute requirement; the test is whether a person of reasonable firmness in the actor's situation would have been unable to resist. A student could argue that Carmine's horrific, mob-style threat satisfies this standard, excusing conduct over the next four months because the profound fear never dissipated.
(b) Argument-for: A student might argue that because Carmine represents organized crime, his threat is continuously imminent. Since mobsters can strike at any time and monitor their victims, Marcus was arguably under a constant, credible, and severe threat of imminent death for the entire four months.
(c) Argument-for: A student might recall that duress is categorically barred as a defense to intentional murder. Extending this logic, they might argue that major federal felonies—such as the commercial distribution of controlled substances—similarly bar the defense due to strong public policy against excusing large-scale drug trafficking.
(d) Argument-for: Under common law and federal standards, duress requires a strictly imminent threat of death or serious bodily injury, with no reasonable opportunity to escape. Four months of continuous truck routing provides ample time to contact law enforcement or flee. Thus, the threat was not sufficiently imminent to justify a continuous four-month crime spree.
(e) Argument-for: Duress is unavailable if the defendant recklessly or negligently placed himself in a situation where coercion was probable. A student could argue that by knowingly taking a managerial job at Pinnacle Waste—a known front for organized crime—Marcus voluntarily assumed the risk of mob violence, thereby forfeiting the defense.

Head-to-head: Option (d) is the strongest and clearly correct because a four-month delay fatally undermines the core imminence requirement of a duress defense. Option (c) is easily rejected due to a robust falsifiable claim that duress is "categorically unavailable" for drug offenses. However, under the strict close-call standard, options (a), (b), and (e) rely primarily on faulty factual applications or implicit omissions rather than explicitly false legal propositions locked with absolute terms. Option (a) implicitly omits the escape requirement but lacks an absolute legal falsehood. Option (b) falsely characterizes a four-month period as "imminent" but does not contain a false rule of law. Option (e) concludes assumption of risk solely from taking a job, which is a factual leap rather than a locked legal error.

Falsifiable claim per distractor:
- (a): "would cause a person of reasonable firmness to yield" — wrong because it is a faulty factual application of the MPC standard that ignores the four-month window to escape, but it lacks an explicit false legal claim.
- (b): "under a credible and severe threat of imminent serious bodily harm" — wrong because characterizing a four-month ongoing threat as strictly "imminent" fails both legally and factually, though it lacks absolute locking words.
- (c): "categorically unavailable for any federal offenses involving the commercial distribution of controlled substances" — wrong because duress is generally available for drug offenses (it is typically only barred for intentional murder).
- (e): "voluntarily assumed the risk of coercion and violence when he knowingly took a managerial job" — wrong because taking a legitimate-seeming managerial job does not legally constitute reckless placement into a coercive situation unless he knew of the enterprise's inherently coercive nature.

Recommended fix: Lock the distractors with absolute legal claims to satisfy the close-call standard.
Change (a) to: "Yes, because a severe threat of death automatically satisfies the duress defense regardless of the time elapsed or opportunities to escape."
Change (b) to: "Yes, because an unretracted threat of death from an organized crime figure is categorically classified as legally imminent indefinitely."
Change (e) to: "No, because accepting employment at a commercial enterprise automatically constitutes a voluntary assumption of the risk of coercion."
-->
