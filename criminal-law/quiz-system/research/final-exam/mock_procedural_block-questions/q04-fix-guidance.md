# Fix Guidance for q04

The QA pipeline flagged this question. Rewrite `q04.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

<!-- audit: MUST FIX -->

**Safety Block Triggered.** The previous version of this question was blocked by Gemini's safety filters as unsafe. Please rewrite the fact pattern to reduce the risk of unsafe content blocking.

Error: Model returned empty or blocked response.

## Issue 2 — argpass-opus

**Q4.** At trial, Sal admits to transporting the fentanyl but attempts to raise an affirmative defense. He argues that he only transported the drugs because Leo threatened that his family would "pay the price tomorrow" if he failed. Does Sal have a valid duress defense for transporting the fentanyl?

(a) Yes, because Leo's position as a high-level manager in a violent cartel made the threat to Sal's family objectively credible and overwhelming.
(b) Yes, because the law allows couriers to claim duress whenever they act under orders from superiors who have access to their families.
(c) No, because Leo's threat that Sal's family would pay the price "tomorrow" fails to satisfy the strict requirement of an imminent threat. <!-- correct -->
(d) No, because duress is completely unavailable as an affirmative defense for any drug trafficking offense carrying a potential sentence of ten years.
(e) No, because Sal failed to independently verify whether Leo actually had the logistical capability to harm his family the following day.

**Answer:** (c)

**Explanation:** A valid duress defense requires a threat of immediate or imminent death or serious bodily injury. Leo's threat that Sal's family would "pay the price tomorrow" fails this strict imminence requirement, rendering the defense legally unavailable. (a) is wrong because the objective credibility of a threat does not cure the lack of imminence. (b) fails because the law does not categorically grant duress defenses to couriers based solely on their superiors' general capabilities. (d) is incorrect because duress is generally available for drug trafficking offenses; it is traditionally barred only for intentional homicide. (e) is wrong because the defense fails fundamentally on the imminence element, regardless of whether Sal attempted to verify the logistics of the threat.

**Tags:** chapters: [21], topics: [duress, imminent-threat], difficulty: easy, cognitive: application

**Grounding:** Chapter 21 (Necessity and Duress) - Imminence Requirement

<!-- argument-pass: SHOULD FIX
(a) Argument-for: A student could argue that modern penal codes (like the Model Penal Code) have relaxed the strict common-law "imminence" requirement in favor of evaluating whether a "person of reasonable firmness in his situation would have been unable to resist." Under this framework, a highly credible, overwhelming threat from a cartel boss could fulfill the duress requirements even if the harm is scheduled for "tomorrow," since escaping the cartel's reach is practically impossible. Thus, (a) would be correct under a formulation that prioritizes objective credibility and severity over strict temporal imminence.
(b) Argument-for: A student might argue that (b) is correct by misapplying policy exceptions regarding structural coercion in organized crime. They might believe the law categorically protects vulnerable low-level actors trapped in drug syndicates. The argument asserts that couriers are legally granted a duress defense "whenever" they act under superiors with access to their families, overriding standard imminence or reasonable alternative requirements because of the inherent ongoing danger.
(c) Argument-for: This relies on the traditional common-law rule. Duress requires a threat of present, imminent, and impending death or serious bodily injury. A threat to harm someone "tomorrow" is a future threat, which theoretically provides the defendant time to seek help from law enforcement or escape. Therefore, the imminence element is strictly failed, making (c) the correct application of black-letter law.
(d) Argument-for: A student might argue that certain jurisdictions or federal statutes categorically bar duress for severe offenses, just as it is barred for intentional homicide. The argument would rely on the premise that a potential sentence of ten years reflects a legislative intent to preclude affirmative excuses for dangerous narcotics distribution. Therefore, they would conclude duress is "completely unavailable" for high-level drug trafficking offenses.
(e) Argument-for: A student could argue that duress requires a reasonable belief that the threat will be carried out, which inherently demands some level of diligence from the defendant. If a defendant makes no effort to investigate a future threat's logistics when they have the time (since the threat is for "tomorrow"), their belief in its immediate necessity cannot be objectively reasonable. Thus, (e) correctly identifies a mandatory legal duty to "independently verify" as the fatal flaw in the defense.

Head-to-head: 
Option (c) correctly states the traditional common-law requirement for duress: the threat must be of immediate/imminent harm, and a threat for "tomorrow" legally operates as a future threat, defeating the defense. Option (a) attempts to argue that credibility and severity overcome the imminence defect, but it lacks the absolute phrasing required by the close-call standard to lock down its falsifiable claim. Option (b) makes a wildly inaccurate categorical claim about couriers ("whenever"). Option (d) invents a non-existent categorical bar for drug trafficking ("completely unavailable... for any"). Option (e) invents a specific, non-existent legal duty to "independently verify" logistical capability. Because (a) lacks an absolute qualifier, it relies on an implicit assumption that credibility overrides imminence, making it technically weaker as a strict distractor under the pipeline's standards.

Falsifiable claim per distractor:
- (a): "Yes, because Leo's position... made the threat to Sal's family objectively credible and overwhelming" — wrong because objective credibility alone does not legally excuse the lack of temporal imminence (though it lacks an absolute word to firmly lock this legal error).
- (b): "allows couriers to claim duress whenever they act under orders" — wrong because there is no categorical "whenever" exception for couriers.
- (d): "completely unavailable as an affirmative defense for any drug trafficking offense" — wrong because duress is generally available for drug trafficking; the categorical bar applies to intentional murder.
- (e): "because Sal failed to independently verify whether Leo actually had the logistical capability" — wrong because the law of duress imposes no strict duty to "independently verify" a threat's logistical capability.

Recommended fix: Edit (a) to include an absolute word to explicitly lock the false legal claim. Change (a) to: "Yes, because an objectively credible threat of serious harm from a cartel manager categorically satisfies the duress defense, regardless of whether the threat is imminent."
-->
