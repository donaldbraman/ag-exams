# Fix Guidance for q11

The QA pipeline flagged this question. Rewrite `q11.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

<!-- audit: MUST FIX -->

**Safety Block Triggered.** The previous version of this question was blocked by Gemini's safety filters as unsafe. Please rewrite the fact pattern to reduce the risk of unsafe content blocking.

Error: Model returned empty or blocked response.

## Issue 2 — edge-case

**Q11.** The prosecution seeks to charge Avon Commercial Properties Inc. under the Racketeer Influenced and Corrupt Organizations Act (RICO). Avon argues that the company is a legitimate real estate business that holds board meetings and processes real rent checks. Can the company constitute a RICO "enterprise"?

(a) Yes, because an enterprise broadly includes any legal entity, such as a corporation, even if it conducts both legitimate and illegitimate activities. <!-- correct -->
(b) Yes, because any business entity that generates more than $10,000 in illicit revenue is statutorily classified as a corrupt enterprise under federal law.
(c) No, because a RICO enterprise must be a wholly illegitimate association-in-fact with absolutely no lawful commercial operations or legitimate board meetings.
(d) No, because a formally registered corporation cannot form the requisite criminal intent to be designated as an enterprise under federal racketeering statutes.
(e) No, because the government must definitively prove that the legitimate real estate activities were explicitly authorized by the illicit drug network.

**Answer:** (a)

**Explanation:** RICO's definition of an "enterprise" is extremely broad and includes any individual, partnership, corporation, association, or other legal entity. An enterprise can be a completely legitimate business that is used to facilitate racketeering activity. (b) fails because there is no specific statutory dollar threshold required to establish an enterprise. (c) fails because RICO was specifically designed to target the infiltration of legitimate businesses by organized crime, so an enterprise need not be wholly illegitimate. (d) fails because corporations are legal entities expressly included in the statutory definition and can be criminally liable. (e) fails because the illicit network uses the legitimate activities as a shield; explicit authorization from the network is not an element.

**Tags:** chapters: [20], topics: [RICO, enterprise liability, corporate enterprise], difficulty: easy, cognitive: recall

**Grounding:** Chapter 20 (corporate-enterprise)

<!-- edge-case-audit: SHOULD FIX
1. Fact Pattern Booby Traps: The prompt states the prosecution seeks to charge the corporation itself under RICO, then asks if it can be the enterprise. Under 18 U.S.C. § 1962(c), the defendant "person" must be distinct from the "enterprise." Charging the corporation as the defendant and naming it as the enterprise inadvertently raises the RICO distinctness problem, which distracts from the intended rule (that legitimate businesses can serve as enterprises).
2. Cross-Doctrine Clashes: pass
3. Cross-Question Spoilers: pass
Recommended fix: Change the first sentence to: "The prosecution charges CEO Avon under the Racketeer Influenced and Corrupt Organizations Act (RICO), alleging that Avon Commercial Properties Inc. is the required 'enterprise'."
-->
