# Fix Guidance for q11

The QA pipeline flagged this question. Rewrite `q11.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q11.** Assume Arthur and Silas are charged with conspiracy to distribute a Schedule I controlled substance. They argue they lacked the specific intent for conspiracy because Arthur believed the substance was a legal "nootropic." Does Arthur's mistake of law negate the conspiracy charge?

(a) Yes, because conspiracy is a specific intent crime that requires actual knowledge that the planned conduct directly violates the specific provisions of the penal law.
(b) Yes, because under the *Lauria* doctrine, a supplier of goods cannot be held liable for conspiracy unless they explicitly research the legality of the venture.
(c) No, because conspiracy only requires the purpose to commit the factual elements of the target offense, and ignorance of the penal law is generally no excuse. <!-- correct -->
(d) No, because the Model Penal Code applies absolute strict liability to all drug conspiracies involving Schedule I substances, rendering Arthur's mental state legally irrelevant.
(e) No, because Silas's knowledge of the specialized glassware purchases automatically overrides Arthur's genuine but mistaken belief about the underlying legality of the chemical compound.

**Answer:** (c)

**Explanation:** Conspiracy requires the intent to agree and the purpose to commit the object crime. However, the traditional rule that "ignorance of the law is no excuse" applies; the defendants intended to distribute the exact chemical structure they synthesized. Ignorance that this structure is classified as a Schedule I substance under penal law does not negate their purpose to commit the factual elements of the offense. (a) is wrong because while conspiracy is a specific intent crime, it requires specific intent to commit the acts constituting the offense, not knowledge of the penal code itself. (b) is wrong because *Lauria* deals with suppliers of legal goods to known criminal operations, whereas Arthur directly produced an illegal substance. (d) is wrong because the MPC requires purpose for conspiracy and does not impose strict liability. (e) is wrong because one co-conspirator's knowledge does not legally override another's mens rea; each is evaluated independently.

**Tags:** chapters: [10, 19], topics: [conspiracy, mens rea, mistake of law], difficulty: hard, cognitive: analysis

**Grounding:** Chapter 19, mens-rea-purpose; Chapter 10, mol-traditional-rule

<!-- audit: MUST FIX
check 1: pass (under the assumption that the unstated facts apply, the doctrine is applied correctly per the traditional rule).
check 2: pass (distractors are generally weak, but only because the stem attempts to stipulate it is a "mistake of law").
check 3: MUST FIX (the explanation explicitly relies on facts—"the defendants intended to distribute the exact chemical structure they synthesized"—that are completely absent from the stem).
check 4: MUST FIX (the stem is missing critical facts: it does not state that the defendants synthesized the substance, nor does it mention the "specialized glassware purchases" referenced in option E. It appears to be an orphan question separated from a broader, multi-part fact pattern. Without knowing Arthur synthesized the specific structure, a student could reasonably assume he simply bought a product labeled "nootropic" without knowing its true chemical identity, which would actually be a mistake of fact negating the mens rea for distributing a controlled substance).
check 5: pass
check 6: pass
check 7: pass
Recommended fix: Add the missing factual premise to the stem: "Arthur and Silas used specialized glassware to synthesize a specific chemical compound. They are charged with conspiracy to distribute a Schedule I controlled substance. Arthur argues he lacked the specific intent for conspiracy because, while he knew the exact chemical structure they were distributing, he believed the substance was a legal 'nootropic'."
-->
