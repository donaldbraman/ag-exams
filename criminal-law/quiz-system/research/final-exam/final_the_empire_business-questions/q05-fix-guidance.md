# Fix Guidance for q05

The QA pipeline flagged this question. Rewrite `q05.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

<!-- audit: MUST FIX -->

**Safety Block Triggered.** The previous version of this question was blocked by Gemini's safety filters as unsafe. Please rewrite the fact pattern to reduce the risk of unsafe content blocking.

Error: Model returned empty or blocked response.

## Issue 2 — argpass-sonnet

**Q5.** Did Dominic "use" a firearm under 18 U.S.C. § 924(c) when he acquired the AR-15 rifles in exchange for the narcotics?

(a) No, because a defendant who trades drugs to receive a firearm does not "use" the firearm during a drug trafficking crime under the statute. <!-- correct -->
(b) Yes, because receiving firearms as consideration in a drug transaction constitutes active employment of the weapons in interstate commerce.
(c) No, because the AR-15 rifles were unregistered, meaning they did not qualify as legally recognized firearms under the federal statute.
(d) Yes, because both parties to a drugs-for-guns transaction equally utilize the firearms as a medium of exchange to facilitate the drug deal.
(e) No, because Dominic did not explicitly brandish or discharge the AR-15 rifles during the course of the underlying narcotics trafficking transaction.

**Answer:** (a)

**Explanation:** Under *Watson v. United States*, a defendant who trades drugs to acquire a gun does not "use" a firearm under § 924(c). Only the party tendering the gun uses it as consideration; a "seller does not 'use' a buyer's consideration." (b) is wrong because the Supreme Court expressly rejected this exact interpretation in *Watson*. (c) is wrong because registration status is irrelevant to whether an object is a firearm under § 924(c). (d) is wrong because *Watson* expressly held that the transaction is asymmetrical regarding "use." (e) is wrong because while brandishing would qualify, *Smith* established that trading a gun for drugs *is* "using" it; Dominic's charge fails because he was the one receiving the gun, not because he didn't brandish it.

**Tags:** chapters: [15], topics: [924c, use-of-firearm], difficulty: intermediate, cognitive: application

**Grounding:** Chapter 15 - Watson v. United States

<!-- argument-pass: SHOULD FIX
(a) Argument-for: Under *Watson v. United States*, 552 U.S. 74 (2007), a person who trades drugs for a gun does not "use" the firearm within the meaning of 18 U.S.C. § 924(c). The Supreme Court held that the ordinary meaning of "use" does not encompass receiving an item as consideration. Therefore, Dominic, as the receiver of the firearm, is correctly exonerated from the "use" prong.
(b) Argument-for: A student could draw on the broad definition of "use" articulated in *Smith v. United States*, arguing that bringing a firearm into a drug transaction as consideration fundamentally alters the nature of the crime. Under this view, receiving the weapon is an active employment of it in commerce because it facilitates the drug sale, making it a plausible interpretation of statutory text prior to *Watson*.
(c) Argument-for: A student might conflate the definitional requirements of 18 U.S.C. § 924(c) with the National Firearms Act (NFA), which relies heavily on registration. They could argue that for a firearm to trigger federal statutory enhancements under this specific provision, it must be part of the legally recognized (i.e., registered) commercial market, and an unregistered weapon falls outside this definition.
(d) Argument-for: Drawing on contract principles of mutual consideration, a student could argue that in a barter transaction, both parties simultaneously "use" both pieces of exchanged property. Justice Ginsburg’s concurrence in *Watson* noted the anomaly of holding only one party liable for "using" the gun, suggesting a student could plausibly believe the law treats both sides of the drugs-for-guns exchange symmetrically.
(e) Argument-for: Following *Bailey v. United States*, which narrowed "use" to "active employment," a student could argue that mere receipt of a firearm is passive. By pointing out that Dominic did not brandish or discharge the weapons, the student can accurately describe his passive conduct. Thus, they might conclude that the absence of these explicit violent acts is the legal reason his conduct falls short of statutory "use."

Head-to-head: Option (a) is the decisively correct answer under *Watson v. United States*, which explicitly established that receiving a firearm in a drug trade is not "use." Distractors (b) and (d) are factually falsifiable because the Supreme Court expressly rejected the theories that receiving a gun constitutes "active employment" or that barter transactions entail mutual, equal "use" of the firearm. Distractor (c) presents an explicitly false legal claim, as 18 U.S.C. § 921(a)(3) defines a firearm by its physical characteristics, not its registration status. Distractor (e) identifies the correct outcome but its rationale implicitly relies on the false premise that brandishing or discharging are the *only* ways to "use" a firearm (omitting that trading a gun for drugs is "use" under *Smith*). Because (e) does not lock this false premise with an absolute word like "unless" or "solely," it relies on an implicit omission rather than an explicit false legal claim, making it a close-call vulnerability.

Falsifiable claim per distractor:
- (b): "receiving firearms as consideration ... constitutes active employment" — wrong because *Watson* expressly held that receiving a firearm does not constitute active employment ("use").
- (c): "unregistered, meaning they did not qualify as legally recognized firearms" — wrong because registration status has no bearing on the statutory definition of a firearm under federal law.
- (d): "both parties ... equally utilize the firearms as a medium of exchange" — wrong because *Watson* established an asymmetrical rule where only the party supplying the gun "uses" it.
- (e): "because Dominic did not explicitly brandish or discharge" — wrong because it implies these are the only ways to establish "use" (ignoring that giving a gun in barter is also "use" under *Smith*), but it lacks an absolute term to make the claim strictly falsifiable.

Recommended fix: In (e), add an absolute word to lock the false legal claim. Change to: "No, solely because a firearm is not 'used' under the statute unless the defendant explicitly brandishes or discharges it during the crime."
-->

## Issue 3 — argpass-opus

**Q5.** Did Dominic "use" a firearm under 18 U.S.C. § 924(c) when he acquired the AR-15 rifles in exchange for the narcotics?

(a) No, because a defendant who trades drugs to receive a firearm does not "use" the firearm during a drug trafficking crime under the statute. <!-- correct -->
(b) Yes, because receiving firearms as consideration in a drug transaction constitutes active employment of the weapons in interstate commerce.
(c) No, because the AR-15 rifles were unregistered, meaning they did not qualify as legally recognized firearms under the federal statute.
(d) Yes, because both parties to a drugs-for-guns transaction equally utilize the firearms as a medium of exchange to facilitate the drug deal.
(e) No, because Dominic did not explicitly brandish or discharge the AR-15 rifles during the course of the underlying narcotics trafficking transaction.

**Answer:** (a)

**Explanation:** Under *Watson v. United States*, a defendant who trades drugs to acquire a gun does not "use" a firearm under § 924(c). Only the party tendering the gun uses it as consideration; a "seller does not 'use' a buyer's consideration." (b) is wrong because the Supreme Court expressly rejected this exact interpretation in *Watson*. (c) is wrong because registration status is irrelevant to whether an object is a firearm under § 924(c). (d) is wrong because *Watson* expressly held that the transaction is asymmetrical regarding "use." (e) is wrong because while brandishing would qualify, *Smith* established that trading a gun for drugs *is* "using" it; Dominic's charge fails because he was the one receiving the gun, not because he didn't brandish it.

**Tags:** chapters: [15], topics: [924c, use-of-firearm], difficulty: intermediate, cognitive: application

**Grounding:** Chapter 15 - Watson v. United States

<!-- argument-pass: SHOULD FIX
(a) Argument-for: Under *Watson v. United States*, the Supreme Court held that a person who trades drugs to receive a firearm does not "use" the firearm within the meaning of 18 U.S.C. § 924(c). Applying ordinary English meaning, the Court reasoned that a seller does not "use" a buyer's consideration. Since Dominic acquired the AR-15s as payment for narcotics, he falls squarely within the *Watson* safe harbor and did not "use" the weapons.
(b) Argument-for: *Smith v. United States* established that treating a firearm as a medium of exchange in a drug transaction is a form of "use." A student could argue that by accepting firearms as consideration, Dominic actively employed the prospect of acquiring the weapons to facilitate his drug distribution. Under a broad reading of "active employment," bringing the weapons into the core commercial terms of the deal uses them to execute the interstate commerce transaction.
(c) Argument-for: Federal firearms statutes, such as the National Firearms Act, heavily regulate specific weapons through strict registration requirements. A student might argue that to trigger severe federal mandatory minimums under § 924(c), the weapon must meet formal, legally recognized statutory criteria, which for certain tactical rifles implies registration. Therefore, an unregistered, illicit weapon falls outside the legal definition required to sustain the specific enhancement.
(d) Argument-for: In any bilateral contract or barter arrangement, both parties rely on the exchanged goods to consummate the deal. *Smith* established that bartering a gun is "using" it. A student could argue that since a drugs-for-guns trade cannot occur without both parties utilizing the firearm as the foundational medium of exchange, the statute logically applies symmetrically, meaning both the buyer and the seller "use" the gun to facilitate the drug deal.
(e) Argument-for: *Bailey v. United States* narrowed the definition of "use" to require "active employment" of the firearm, rejecting mere possession. A student could argue that since Dominic merely received the weapons passively as payment, he lacked the requisite active physical employment of the guns as weapons or tools of intimidation. Because he did not brandish, discharge, or otherwise physically employ the AR-15s during the deal, the "use" standard is unmet.

Head-to-head: Option (a) is definitively correct under *Watson v. United States*. Options (b) and (d) represent the exact legal positions rejected by the Supreme Court in *Watson*, which held that receiving a gun is not "active employment" and that the barter transaction is legally asymmetrical regarding "use." Option (c) relies on a blatant misstatement of statutory definitions, as § 921(a)(3) defines a firearm by its physical ability to expel a projectile, totally independent of registration. Option (e) reaches the correct conclusion ("No") but relies on an under-inclusive rationale (lack of brandishing/discharging), ignoring that trading a gun *for* drugs is "use" under *Smith* even without brandishing. However, (e) lacks an absolute word to strictly lock in its falsifiable legal claim, making it a slight implicit omission rather than an explicitly false universal rule.

Falsifiable claim per distractor:
- (b): "receiving firearms as consideration... constitutes active employment" — wrong because *Watson* expressly held that receiving a firearm in a drug trade is *not* active employment or "use."
- (c): "meaning they did not qualify as legally recognized firearms" — wrong because registration status is categorically irrelevant to the definition of a firearm under Title 18.
- (d): "both parties... equally utilize the firearms as a medium of exchange" — wrong because *Watson* explicitly held the transaction is asymmetrical; only the party tendering the gun "uses" it.
- (e): "because Dominic did not explicitly brandish or discharge" — wrong because it implies a false rule that these are the only ways to use a firearm (ignoring *Smith*), but it currently lacks absolute framing to strictly lock the falsifiability.

Recommended fix: Edit (e) to lock in the false legal premise with absolute language. Change (e) to: "No, because a firearm is 'used' under the statute solely when it is explicitly brandished or discharged during the transaction."
-->
