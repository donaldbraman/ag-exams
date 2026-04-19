# Fix Guidance for q05

The QA pipeline flagged this question. Rewrite `q05.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — grounding

**Q5.** Assume that it is legally established that both men constructively possessed the narcotics. Can an intent to distribute be inferred against them for the five kilograms of cocaine?

(a) An intent to distribute can be inferred because the discovery of five kilograms of packaged cocaine far exceeds the quantity that would be consistent with standard personal use. <!-- correct -->
(b) An intent to distribute can only be established if law enforcement explicitly observes an actual hand-to-hand transaction or discovers specific financial ledgers documenting the underlying narcotics sales.
(c) An intent to distribute is defeated because the cocaine was strictly locked away in a private office, legally indicating an intent to hoard rather than to actively disseminate.
(d) An intent to distribute cannot apply to Steve because his primary role in the enterprise was providing logistical legal services rather than personally handling the actual physical narcotics.
(e) An intent to distribute requires strict proof of an explicit agreement with a verified buyer, which is absent since no customers were present during the law enforcement raid.

**Answer:** (a)

**Explanation:** The intent to distribute narcotics can be reliably inferred from circumstantial evidence, such as possessing a quantity of drugs that far exceeds an amount consistent with personal use. Five kilograms of packaged cocaine easily satisfies this threshold, making (a) correct. (b) is incorrect because direct observational evidence or financial ledgers are not strictly required to infer distribution intent. (c) is incorrect because locking drugs in an office does not legally overcome the strong inference drawn from massive commercial quantities. (d) is incorrect because an individual who constructively possesses bulk narcotics can share the intent to distribute regardless of their primary corporate role. (e) is incorrect because the state does not need to prove an explicit agreement with a verified buyer to charge distribution intent.

**Tags:** chapters: [10], topics: [intent to distribute, circumstantial evidence], difficulty: easy, cognitive: application

**Grounding:** Intent to distribute may be inferred circumstantially from the bulk quantity, packaging, and high street value of the narcotics, which here far exceeds amounts plausible for individual personal use.

<!-- GROUNDING-FAIL: Intent to distribute is not in any chapter map. The closest taught doctrines are: none (meta-map artifact and focus maps are missing from the prompt). Correct answer must rely on one of those instead. -->

## Issue 2 — audit

**Q5.** Assume that it is legally established that both men constructively possessed the narcotics. Can an intent to distribute be inferred against them for the five kilograms of cocaine?

(a) An intent to distribute can be inferred because the discovery of five kilograms of packaged cocaine far exceeds the quantity that would be consistent with standard personal use. <!-- correct -->
(b) An intent to distribute can only be established if law enforcement explicitly observes an actual hand-to-hand transaction or discovers specific financial ledgers documenting the underlying narcotics sales.
(c) An intent to distribute is defeated because the cocaine was strictly locked away in a private office, legally indicating an intent to hoard rather than to actively disseminate.
(d) An intent to distribute cannot apply to Steve because his primary role in the enterprise was providing logistical legal services rather than personally handling the actual physical narcotics.
(e) An intent to distribute requires strict proof of an explicit agreement with a verified buyer, which is absent since no customers were present during the law enforcement raid.

**Answer:** (a)

**Explanation:** The intent to distribute narcotics can be reliably inferred from circumstantial evidence, such as possessing a quantity of drugs that far exceeds an amount consistent with personal use. Five kilograms of packaged cocaine easily satisfies this threshold, making (a) correct. (b) is incorrect because direct observational evidence or financial ledgers are not strictly required to infer distribution intent. (c) is incorrect because locking drugs in an office does not legally overcome the strong inference drawn from massive commercial quantities. (d) is incorrect because an individual who constructively possesses bulk narcotics can share the intent to distribute regardless of their primary corporate role. (e) is incorrect because the state does not need to prove an explicit agreement with a verified buyer to charge distribution intent.

**Tags:** chapters: [10], topics: [intent to distribute, circumstantial evidence], difficulty: easy, cognitive: application

**Grounding:** Intent to distribute may be inferred circumstantially from the bulk quantity, packaging, and high street value of the narcotics, which here far exceeds amounts plausible for individual personal use.

<!-- audit: MUST FIX
Check 1: pass
Check 2: pass
Check 3: pass
Check 4: fail: The question is entirely missing its master fact pattern. The stem refers to "both men," "Steve," "a private office," and "logistical legal services," none of which are established in the provided text.
Check 5: pass
Check 6: pass
Check 7: pass
Check 8: pass
Recommended fix: Integrate the relevant facts from the missing master fact pattern directly into the stem so students know who Steve is, what the enterprise is, and the context of the private office.
-->
