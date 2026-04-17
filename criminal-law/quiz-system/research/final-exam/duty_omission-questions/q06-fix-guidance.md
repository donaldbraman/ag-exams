# Fix Guidance for q06

The QA pipeline flagged this question. Rewrite `q06.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — edge-case

**Q6.** In a jurisdiction applying the federal Pinkerton doctrine, can Alex be held liable for Dana's burglary of the veterinary clinic?

(a) Yes, if the burglary was committed in furtherance of the drug conspiracy and was a reasonably foreseeable consequence of the conspiracy's operations. <!-- correct -->
(b) Yes, because any crime committed by a co-conspirator during the timeframe of the conspiracy is automatically attributed to all members.
(c) No, because Pinkerton liability requires that the defendant intentionally assisted or encouraged the specific target offense.
(d) No, because burglary is a crime of violence, and the target of the conspiracy was solely non-violent drug distribution.
(e) No, because the federal system explicitly rejected the Pinkerton doctrine, requiring proof of purposeful aid for all co-conspirator crimes.

**Answer:** (a)

**Explanation:** Under the Pinkerton doctrine, a conspirator is liable for the substantive offenses of co-conspirators if the offenses are committed in furtherance of the conspiracy and are reasonably foreseeable. Dana breaking in to get a stimulant to save the operation fits this test. (b) is wrong because Pinkerton is not absolute; it requires the acts to be foreseeable and in furtherance of the conspiracy. (c) is wrong because intentional assistance defines accomplice liability, whereas Pinkerton extends liability without specific intent for the collateral crime. (d) is wrong because violent crimes can be foreseeable consequences of drug conspiracies. (e) is wrong because the federal system uses Pinkerton; it is the MPC that rejected it.

**Tags:** chapters: [19], topics: [pinkerton-doctrine, conspiracy], difficulty: medium, cognitive: application

**Grounding:** Chapter 19, Pinkerton Doctrine

<!-- edge-case-audit: SHOULD FIX
1. Fact Pattern Booby Traps: pass
2. Cross-Doctrine Clashes: If Dana's necessity defense (tested in Q7) successfully justifies the break-in, there is no substantive crime of burglary for Alex to inherit via Pinkerton. 
3. Cross-Question Spoilers: By asking about Pinkerton liability for Dana's acts, Q6 inherently premises that Dana is a co-conspirator. This acts as a spoiler for Q12, which specifically tests whether her premium pricing actually established a conspiratorial agreement in the first place.
Recommended fix: Revise the stem to include a conditional assumption isolating the doctrine: "Assuming Dana is deemed a co-conspirator and her break-in constitutes an unjustified criminal burglary, can Alex be held liable for Dana's burglary of the veterinary clinic?"
-->

## Issue 2 — argpass-opus

**Q6.** In a jurisdiction applying the federal Pinkerton doctrine, can Alex be held liable for Dana's burglary of the veterinary clinic?

(a) Yes, if the burglary was committed in furtherance of the drug conspiracy and was a reasonably foreseeable consequence of the conspiracy's operations. <!-- correct -->
(b) Yes, because any crime committed by a co-conspirator during the timeframe of the conspiracy is automatically attributed to all members.
(c) No, because Pinkerton liability requires that the defendant intentionally assisted or encouraged the specific target offense.
(d) No, because burglary is a crime of violence, and the target of the conspiracy was solely non-violent drug distribution.
(e) No, because the federal system explicitly rejected the Pinkerton doctrine, requiring proof of purposeful aid for all co-conspirator crimes.

**Answer:** (a)

**Explanation:** Under the Pinkerton doctrine, a conspirator is liable for the substantive offenses of co-conspirators if the offenses are committed in furtherance of the conspiracy and are reasonably foreseeable. Dana breaking in to get a stimulant to save the operation fits this test. (b) is wrong because Pinkerton is not absolute; it requires the acts to be foreseeable and in furtherance of the conspiracy. (c) is wrong because intentional assistance defines accomplice liability, whereas Pinkerton extends liability without specific intent for the collateral crime. (d) is wrong because violent crimes can be foreseeable consequences of drug conspiracies. (e) is wrong because the federal system uses Pinkerton; it is the MPC that rejected it.

**Tags:** chapters: [19], topics: [pinkerton-doctrine, conspiracy], difficulty: medium, cognitive: application

**Grounding:** Chapter 19, Pinkerton Doctrine

<!-- argument-pass: SHOULD FIX
(a) Argument-for: Option (a) accurately captures the precise legal test established in *Pinkerton v. United States*. It correctly notes that vicarious liability for a co-conspirator's substantive offense applies if the collateral crime was committed in furtherance of the conspiracy and was a reasonably foreseeable consequence of the agreement. This makes it the strongest and most legally grounded answer for determining a conspirator's liability under federal doctrine.
(b) Argument-for: Option (b) presents a plausible but overly broad interpretation of agency theory in conspiracy. A student might argue that since conspiracy acts as a partnership in crime, the temporal bounds of the conspiracy are the only necessary limits for attribution of liability. Under this rationale, any acts committed during the partnership's lifespan are automatically attributable to all members as mutual agents.
(c) Argument-for: Option (c) correctly states the strict standard for traditional accomplice liability (purposeful assistance or encouragement of the target offense). A student might argue that this option is correct if they confuse *Pinkerton* liability with traditional complicity, believing that modern courts strictly require specific intent or active encouragement to hold a defendant liable for a co-conspirator's substantive crime.
(d) Argument-for: Option (d) focuses heavily on the foreseeability prong, arguing that a violent property crime like burglary cannot stem from a non-violent drug distribution agreement. A student could argue that the drastic shift in the nature of the crime—from selling drugs to committing a violent break-in—inherently breaks the causal chain. Thus, under this factual application, the act would be fundamentally unforeseeable to a non-violent conspirator.
(e) Argument-for: Option (e) asserts that the federal system rejected *Pinkerton* in favor of the Model Penal Code's approach. A student might defend this by recalling the MPC's famous rejection of conspiracy as a standalone basis for substantive liability and mistakenly concluding that federal courts eventually adopted this reform. Therefore, they would assume proof of purposeful aid is always required.

Head-to-head: 
Option (a) is the clear winner as it perfectly articulates the federal *Pinkerton* rule. Option (b) is easily falsified by its use of "automatically," since foreseeability and furtherance are mandatory constraints, not strict liability. Option (c) is explicitly falsified by claiming *Pinkerton* requires intentional assistance, which actually defines traditional accomplice liability. Option (e) contains a blatantly false jurisdictional claim that the federal system rejected the doctrine, when in fact federal courts established it. Option (d), however, relies on an implicit assumption that violent crimes aren't foreseeable from non-violent drug conspiracies; while federal courts routinely hold violence foreseeable in drug rings, the distractor lacks an absolute, explicitly false legal rule, making it somewhat weaker structurally.

Falsifiable claim per distractor:
- (b): "automatically attributed" — wrong because Pinkerton liability is not strict liability based solely on timing; the collateral acts must still be foreseeable and in furtherance of the conspiracy.
- (c): "Pinkerton liability requires that the defendant intentionally assisted or encouraged" — wrong because Pinkerton explicitly extends liability precisely when the intentional assistance required for accomplice liability is absent.
- (d): "because burglary is a crime of violence, and the target of the conspiracy was solely non-violent drug distribution" — wrong because violence can be legally foreseeable in drug conspiracies, but this distractor lacks an explicit absolute word to lock down the false rule.
- (e): "the federal system explicitly rejected the Pinkerton doctrine" — wrong because the federal system is the very jurisdiction that created and actively uses the Pinkerton doctrine.

Recommended fix: Change (d) to include an absolute phrase locking the false legal premise, such as: "No, because a violent property crime is categorically unforeseeable as a matter of law when a conspiracy's target is solely non-violent drug distribution."
-->
