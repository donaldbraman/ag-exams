# Fix Guidance for q10

The QA pipeline flagged this question. Rewrite `q10.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q10.** Assume the DA instead charges Stringer with conspiracy to manufacture illicit drugs. Under the *Lauria* standard for establishing the mens rea of conspiracy for a merchant who supplies goods for illicit use, is Stringer guilty?

(a) Yes, because knowledge of the illicit use of goods automatically converts a merchant into a co-conspirator under the prevailing federal judicial standards.
(b) Yes, because the Acetone-FX is an industrial chemical, which creates a mandatory presumption of purposeful intent to actively join the illicit conspiracy.
(c) No, because Stringer did not charge an inflated price, provide specialized services, or have a stake in the venture, so his mere knowledge does not establish purpose. <!-- correct -->
(d) No, because a merchant cannot be legally charged with conspiracy unless they explicitly agree in writing to participate in the illicit distribution scheme.
(e) No, because the bilateral agreement requirement strictly demands that the supplier and the buyer share the exact same motive for participating in the transaction.

**Answer:** (c)

**Explanation:** Under *Lauria*, a supplier of lawful goods to an illicit enterprise is only guilty of conspiracy if their intent to participate can be inferred. This requires more than mere knowledge; it requires a "stake in the venture" (e.g., inflated prices, specialized services, or disproportionate sales volume) to elevate knowledge to purpose. (a) fails because *Lauria* explicitly rejects the idea that knowledge equals purpose for conspiracy. (b) fails because there is no mandatory presumption of intent based merely on the industrial nature of the chemical. (d) fails because conspiracy agreements are routinely tacit or implicit rather than written. (e) fails because co-conspirators can have different motives so long as they share a purpose to commit the target offense.

**Tags:** chapters: [19], topics: [conspiracy, mens rea, Lauria inferences], difficulty: medium, cognitive: application

**Grounding:** Chapter 19 (lauria-knowledge-vs-purpose; lauria-three-inferences)

<!-- audit: MUST FIX
check 1: pass
check 2: pass
check 3: pass
check 4: fails. The stem relies on an external/shared fact pattern (implied by "instead charges Stringer" and the reference to "the Acetone-FX"). Standing alone, the question lacks the necessary facts regarding Stringer's pricing, sales volume, or business practices to determine whether he met any of the Lauria inferences.
check 5: pass
check 6: pass
check 7: pass
Recommended fix: Briefly recapitulate the operative facts in the stem (e.g., "Assume Stringer sold the Acetone-FX at normal market prices in standard retail volumes. If the DA instead charges Stringer...") so the item is self-contained and definitively points to option C.
-->
