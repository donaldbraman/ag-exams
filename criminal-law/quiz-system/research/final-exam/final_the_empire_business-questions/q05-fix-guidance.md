# Fix Guidance for q05

The QA pipeline flagged this question. Rewrite `q05.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — argpass-sonnet

**Q5.** The investigation uncovered Dominic's drug-for-guns trade. Assume Dominic is charged under 18 U.S.C. § 924(c) with "using" a firearm during a drug trafficking crime. Is he guilty?

(a) Guilty, because acquiring weapons to arm an extortion crew constitutes the active employment of a firearm during the commission of a federal drug trafficking crime.
(b) Not guilty, because a defendant who trades drugs to acquire a gun does not "use" the firearm; only the party tendering the weapon actually uses it. <!-- correct -->
(c) Guilty, because trading drugs for a firearm inherently involves firearms in a drug trafficking crime, making both sides of the transaction equally liable under the law.
(d) Not guilty, because Dominic did not brandish or fire the AR-15 rifles during the specific exchange of the narcotics with the illicit weapons supplier.
(e) Guilty, because Dominic constructively possessed the firearms as soon as the trade was complete, which is legally synonymous with using them under the federal statute.

**Answer:** (b)

**Explanation:** Under Watson v. United States, a defendant who trades drugs to acquire a firearm does not "use" the firearm within the meaning of 18 U.S.C. § 924(c). The Supreme Court held that receiving a gun as payment is not "using" it; only the person tendering the gun uses it as currency. (a) is incorrect because Watson expressly rejected the idea that receiving a gun to arm a crew constitutes "use" during the trade itself. (c) is incorrect because the Court in Watson explicitly broke the symmetry of the transaction, distinguishing the buyer from the seller. (d) is incorrect because while brandishing is a form of use, the primary doctrinal reason the charge fails here is the Supreme Court's categorical rule about receiving weapons in trades. (e) is incorrect because constructive possession is a distinct legal concept from "using" under the active employment requirement of § 924(c).

**Tags:** chapters: [15], topics: [firearms, Section 924(c), using a firearm], difficulty: easy, cognitive: application

**Grounding:** Watson v. United States

<!-- argument-pass: SHOULD FIX
(a) Argument-for: *Smith v. United States* established that treating a firearm as an item of barter constitutes "use" under § 924(c). A student could argue that when Dominic trades drugs to acquire weapons specifically to arm a crew, the acquisition of the guns is the primary driver of the drug transaction, thereby integrating the firearm actively into the scheme and meeting the active employment standard of *Bailey*.
(b) Argument-for: This relies squarely on the Supreme Court's holding in *Watson v. United States*. The Court drew a sharp textual distinction between trading a gun for drugs (which is "use" under *Smith*) and trading drugs to receive a gun. The person receiving the firearm is merely acquiring it, not actively employing it as a weapon or as currency during the transaction.
(c) Argument-for: A student could argue that under a plain reading of "uses a firearm during and in relation to any... drug trafficking crime", a barter transaction is a single, symmetrical event. Since the firearm is the *sine qua non* of the transaction, both the buyer and seller are participating in an exchange where a firearm is actively employed, making them equally liable as a matter of law.
(d) Argument-for: Under *Bailey v. United States*, "use" requires active employment of the firearm. A student could argue that since Dominic only received the gun and did not brandish or fire it during the exchange, he is not guilty because he did not actively employ the weapon in a traditional sense.
(e) Argument-for: Before *Bailey*, several circuits held that mere possession during a drug crime was sufficient for "use". Furthermore, the statute now penalizes possession in furtherance of a drug crime. A student might confuse the newer possession prong with the older "use" prong, arguing that constructive possession upon completing the trade is legally synonymous with using them under the statute.

Head-to-head: (b) is the clear, correct application of *Watson v. United States*. Distractors (a), (c), and (e) feature explicit, falsifiable legal errors regarding the definitions of "active employment," transaction symmetry, and "constructive possession" respectively. However, (d) relies on an implicit omission rather than a strict false claim. While it is factually true that Dominic did not brandish or fire the weapon, stating he is not guilty "because" he didn't do those things implicitly (but not explicitly) suggests those are the *only* ways to use a firearm (ignoring *Smith*). To survive the close-call standard, (d) needs an absolute word to lock in the false rule of law.

Falsifiable claim per distractor:
- (a): "acquiring weapons... constitutes the active employment" — wrong because *Watson* expressly holds acquiring a weapon in a trade is not active employment.
- (c): "making both sides of the transaction equally liable" — wrong because *Watson* explicitly distinguishes the liability of the receiver from the tenderer.
- (d): "because Dominic did not brandish or fire" — wrong because it relies on the implicit, unstated premise that brandishing or firing are the only ways to "use" a firearm under the statute; lacks an absolute falsifiable claim.
- (e): "constructively possessed... is legally synonymous with using them" — wrong because *Bailey* explicitly distinguishes possession from "use".

Recommended fix: Add absolute wording to (d) to make its legal premise explicitly false. Change (d) to: "Not guilty, solely because a defendant cannot be convicted of "using" a firearm under § 924(c) unless they brandish or fire it during the exchange."
-->

## Issue 2 — argpass-opus

**Q5.** The investigation uncovered Dominic's drug-for-guns trade. Assume Dominic is charged under 18 U.S.C. § 924(c) with "using" a firearm during a drug trafficking crime. Is he guilty?

(a) Guilty, because acquiring weapons to arm an extortion crew constitutes the active employment of a firearm during the commission of a federal drug trafficking crime.
(b) Not guilty, because a defendant who trades drugs to acquire a gun does not "use" the firearm; only the party tendering the weapon actually uses it. <!-- correct -->
(c) Guilty, because trading drugs for a firearm inherently involves firearms in a drug trafficking crime, making both sides of the transaction equally liable under the law.
(d) Not guilty, because Dominic did not brandish or fire the AR-15 rifles during the specific exchange of the narcotics with the illicit weapons supplier.
(e) Guilty, because Dominic constructively possessed the firearms as soon as the trade was complete, which is legally synonymous with using them under the federal statute.

**Answer:** (b)

**Explanation:** Under Watson v. United States, a defendant who trades drugs to acquire a firearm does not "use" the firearm within the meaning of 18 U.S.C. § 924(c). The Supreme Court held that receiving a gun as payment is not "using" it; only the person tendering the gun uses it as currency. (a) is incorrect because Watson expressly rejected the idea that receiving a gun to arm a crew constitutes "use" during the trade itself. (c) is incorrect because the Court in Watson explicitly broke the symmetry of the transaction, distinguishing the buyer from the seller. (d) is incorrect because while brandishing is a form of use, the primary doctrinal reason the charge fails here is the Supreme Court's categorical rule about receiving weapons in trades. (e) is incorrect because constructive possession is a distinct legal concept from "using" under the active employment requirement of § 924(c).

**Tags:** chapters: [15], topics: [firearms, Section 924(c), using a firearm], difficulty: easy, cognitive: application

**Grounding:** Watson v. United States

<!-- argument-pass: SHOULD FIX
(a) Argument-for: A student could rely on the "active employment" standard from *Bailey v. United States*. They might argue that deliberately orchestrating a drug transaction to acquire specific firearms for an extortion crew constitutes the active employment of those weapons in the drug trade. Under this view, acquiring the guns is the very purpose of the drug trafficking crime, making it equivalent to "use" of the firearm.
(b) Argument-for: This is the correct application of *Watson v. United States*. A student would recognize that the Supreme Court explicitly distinguished the act of receiving a gun for drugs from trading a gun for drugs (*Smith v. United States*). The person tendering the drugs "uses" the drugs, while the person tendering the gun "uses" the gun as a medium of exchange; receiving the firearm does not constitute "use" under 18 U.S.C. § 924(c).
(c) Argument-for: A student could draw upon the holding in *Smith v. United States* (that trading guns for drugs is "use") and argue for transactional symmetry. They might reason that a barter exchange inherently requires the active employment of both commodities by both parties to complete the deal. Therefore, anyone involved in a drugs-for-guns swap is purportedly "using" the firearm to facilitate the transaction.
(d) Argument-for: A student might recall that *Bailey v. United States* defined "use" as "active employment," giving examples like brandishing, displaying, bartering, striking with, or firing. Focusing only on the physical acts typically associated with firearms, the student could argue that Dominic's passive receipt of the rifles lacked the physical manifestation of "use" like brandishing or firing, reaching the correct conclusion via an incomplete rationale.
(e) Argument-for: A student might conflate the "use" and "possession" prongs of 18 U.S.C. § 924(c). They could argue that since Congress amended the statute to include "possesses in furtherance of" after *Bailey*, the concept of constructive possession upon completing the trade is legally synonymous with satisfying the "use" requirement charged in the fact pattern.

Head-to-head: 
Option (b) correctly states the holding of *Watson v. United States*, distinguishing the receipt of a firearm from its "use" as a medium of exchange. Option (a) makes a falsifiable legal claim that acquiring weapons constitutes active employment, which *Watson* explicitly rejected. Option (c) relies on a false claim of transactional symmetry, which the Supreme Court broke by separating the buyer from the seller. Option (e) relies on an explicit legal falsehood by equating constructive possession with "use," collapsing two distinct statutory terms. Option (d) arrives at the correct conclusion ("Not guilty"), but its rationale relies on an implicit omission—implying that brandishing or firing is required for "use." However, (d) lacks an absolute word to lock this into an explicit, identifiable false legal claim, allowing a student to argue the statement is technically true (he didn't brandish it) even if legally insufficient on its own.

Falsifiable claim per distractor:
- (a): "acquiring weapons to arm an extortion crew constitutes the active employment of a firearm" — wrong because *Watson* held that receiving a firearm in a drug trade does not constitute "use" or active employment.
- (c): "making both sides of the transaction equally liable under the law" — wrong because *Watson* expressly rejected this symmetry; the seller uses the gun, but the receiver does not.
- (d): "because Dominic did not brandish or fire the AR-15 rifles" — wrong because it implicitly implies brandishing or firing is strictly required to prove "use" (contradicting *Smith*), but it lacks absolute words to firmly lock this as an explicitly false legal claim.
- (e): "which is legally synonymous with using them under the federal statute" — wrong because *Bailey* and subsequent statutory amendments clearly maintain that "use" (active employment) is a distinct legal concept from "possession."

Recommended fix: Add absolute locking words to (d) to make its legal rationale explicitly false. Change (d) to: "Not guilty, solely because "using" a firearm categorically requires brandishing or firing the weapon during the specific exchange of narcotics."
-->
