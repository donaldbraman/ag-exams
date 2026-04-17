# Fix Guidance for q10

The QA pipeline flagged this question. Rewrite `q10.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

<!-- audit: MUST FIX -->

**Safety Block Triggered.** The previous version of this question was blocked by Gemini's safety filters as unsafe. Please rewrite the fact pattern to reduce the risk of unsafe content blocking.

Error: Model returned empty or blocked response.

## Issue 2 — edge-case

**Q10.** Assume Bex is charged with felony murder predicated on the fentanyl distribution. In a jurisdiction that recognizes the felony-murder duress exception, can Bex successfully invoke it?

(a) Yes, because Alba brandished a weapon and forced Bex to participate in the events that directly caused Cody's ultimate death.
(b) Yes, because the exception applies retroactively to any predicate felony if the defendant experiences duress before the victim actually dies.
(c) No, because the exception only applies when the defendant is physically forced to commit the act that directly causes death.
(d) No, because Bex voluntarily entered the predicate distribution conspiracy before any coercive threat was ever made by her partner Alba. <!-- correct -->
(e) No, because the exception is categorically unavailable for any felony involving the distribution of a Schedule I controlled substance.

**Answer:** (d)

**Explanation:** (d) is correct because the felony-murder duress exception requires the underlying predicate felony to have been committed under duress; here, Bex voluntarily entered the distribution conspiracy before Alba threatened her. (a) is wrong because the coercion occurred during the cover-up and homicide phase, not during the commission of the predicate felony. (b) is wrong because the duress must cause the participation in the predicate felony; it cannot be applied retroactively to an offense already voluntarily committed. (c) is wrong because the exception operates to break the chain of liability for the underlying felony, not merely for the lethal act. (e) is wrong because the exception generally applies to any predicate felony, provided the participation was genuinely coerced.

**Tags:** chapters: [21, 14], topics: [duress, felony murder, felony murder exception], difficulty: hard, cognitive: analysis

**Grounding:** Chapter 21, felony-murder-duress-exception

<!-- edge-case-audit: SHOULD FIX
1. Fact Pattern Booby Traps: pass
2. Cross-Doctrine Clashes: Minor mismatch in wording. The stem specifies the felony murder is "predicated on the fentanyl distribution" (the substantive crime), but option (d) refers to the "predicate distribution conspiracy." A sharp student might eliminate (d) on the technicality that conspiracy is rarely a felony murder predicate compared to the substantive distribution offense, or simply because it contradicts the stem.
3. Cross-Question Spoilers: pass
Recommended fix: Change option (d) to read: "No, because Bex voluntarily participated in the predicate fentanyl distribution before any coercive threat was ever made by her partner Alba." and update the explanation similarly.
-->
