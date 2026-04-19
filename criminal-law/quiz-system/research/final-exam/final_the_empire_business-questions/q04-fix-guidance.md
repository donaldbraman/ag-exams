# Fix Guidance for q04

The QA pipeline flagged this question. Rewrite `q04.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q4.** Based on the October 1 transaction, the government charges Kevin with "using" a firearm during and in relation to a drug trafficking crime under 18 U.S.C. § 924(c). Is Kevin guilty of this specific charge?

(a) Guilty, because firearms traded as currency in a narcotics transaction fall squarely within the Supreme Court's definition of active employment of a weapon.
(b) Not guilty, because Kevin received the firearm as consideration for drugs, and a seller of drugs does not "use" the buyer's firearm under the statute. <!-- correct -->
(c) Guilty, because Kevin's subsequent continuous possession of the loaded weapon after the trade satisfies the statutory requirement for carrying during a drug crime.
(d) Not guilty, because the 9mm handgun was never actually brandished, fired, or explicitly threatened during the execution of the October 1 cocaine transaction.
(e) Guilty, because both parties in a drugs-for-weapons barter exchange are deemed to have mutually "used" the firearm to facilitate the illegal commerce transaction.

**Answer:** (b)

**Explanation:** The correct answer is (b). Under *Watson v. United States*, a defendant who trades drugs to acquire a gun does not "use" the firearm under § 924(c); only the party tendering the gun uses it as currency. (a) is wrong because while *Smith* held that trading a gun for drugs constitutes "use," Kevin was on the receiving end, which *Watson* explicitly distinguishes. (c) is wrong because the question specifically asks if he is guilty of "using" the firearm based on the transaction, not a distinct carrying charge. (d) is wrong because brandishing or firing is not strictly required for "use" if the gun is employed as currency (by the person tendering it). (e) is wrong because *Watson* rejected this exact mutual-use symmetry, holding that a "seller does not 'use' a buyer's consideration."

**Tags:** chapters: [15], topics: [Section 924(c), use of a firearm, Watson limitation], difficulty: medium, cognitive: application

**Grounding:** Chapter 15, "Using" a Firearm Under § 924(c) (use-924c-trading-drugs-for-gun; Watson v. United States)

<!-- audit: MUST FIX
Check 1: pass (accurately reflects the holding in Watson v. United States)
Check 2: pass
Check 3: pass
Check 4: Fail. The stem relies on facts external to the question ("the October 1 transaction"). Without the accompanying fact pattern, students have to blindly infer the scenario from the answer choices. 
Check 5: pass
Check 6: pass
Check 7: pass
Check 8: pass
Recommended fix: Integrate the necessary facts into the stem so it functions as a standalone question. For example: "On October 1, Kevin sold cocaine to a buyer, and accepted a 9mm handgun as payment instead of cash. Based on this transaction, the government charges Kevin..."
-->
