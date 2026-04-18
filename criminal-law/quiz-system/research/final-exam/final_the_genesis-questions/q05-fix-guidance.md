# Fix Guidance for q05

The QA pipeline flagged this question. Rewrite `q05.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q5.** Can Avon be convicted personally under the strict-liability municipal safety ordinance for the lack of a certificate?

(a) Guilty, because as the corporate CEO, he stands in a responsible relation to the violation and had authority to prevent it. <!-- correct -->
(b) Guilty, because the prosecution can prove he had actual, personal knowledge of the missing safety inspection certificate.
(c) Not guilty, because criminal liability requires proof that he personally participated in the daily operations of the warehouse.
(d) Not guilty, because he explicitly delegated all local logistics and operational decisions to his manager, Marlowe.
(e) Not guilty, because the corporate veil shields officers from individual criminal liability for municipal code violations.

**Answer:** (a)

**Explanation:** (a) is correct because under the *Park* doctrine, a corporate officer who stands in a "responsible relation" to a public welfare violation can be convicted without personal knowledge, provided they had the authority to prevent or correct it. (b) fails because the facts do not show Avon had actual knowledge of the certificate issue. (c) fails because the *Park* doctrine expressly dispenses with the requirement of personal participation. (d) fails because delegation is not a defense under *Park*; executives must ensure compliance. (e) fails because public welfare offenses pierce the corporate veil to hold responsible officers personally liable.

**Tags:** chapters: [11], topics: [park doctrine, responsible corporate officer, corporate liability], difficulty: medium, cognitive: application

**Grounding:** Chapter 11 - Public Welfare Offenses (Park Doctrine — Foresight and Vigilance)

<!-- audit: MUST FIX
<check 1>: pass
<check 2>: pass
<check 3>: pass
<check 4>: FAILURE. The question stem is completely unmoored from a fact pattern. It introduces Avon, Marlowe, a warehouse, and a delegation without establishing any of these facts in the text. If this relies on a shared master vignette, it must explicitly say "Based on the facts above...". If it is standalone, it requires a factual setup.
<check 5>: FAILURE. A well-prepared student could argue that the *Park* doctrine is a federal standard rooted in the congressional intent of the FDCA. A "municipal safety ordinance" does not automatically incorporate the Responsible Corporate Officer (RCO) doctrine unless the specific state/municipality has adopted it. Applying federal *Park* doctrine to a local ordinance without stipulation invites a jurisdictional challenge.
<check 6>: pass
<check 7>: pass
Recommended fix: Provide the missing facts in the stem. Furthermore, to insulate against jurisdictional challenges, either change "municipal safety ordinance" to "federal safety statute" OR add a stipulation: "...assuming the jurisdiction has adopted the federal *Park* doctrine for public welfare offenses."
-->

## Issue 2 — edge-case

**Q5.** Can Avon be convicted personally under the strict-liability municipal safety ordinance for the lack of a certificate?

(a) Guilty, because as the corporate CEO, he stands in a responsible relation to the violation and had authority to prevent it. <!-- correct -->
(b) Guilty, because the prosecution can prove he had actual, personal knowledge of the missing safety inspection certificate.
(c) Not guilty, because criminal liability requires proof that he personally participated in the daily operations of the warehouse.
(d) Not guilty, because he explicitly delegated all local logistics and operational decisions to his manager, Marlowe.
(e) Not guilty, because the corporate veil shields officers from individual criminal liability for municipal code violations.

**Answer:** (a)

**Explanation:** (a) is correct because under the *Park* doctrine, a corporate officer who stands in a "responsible relation" to a public welfare violation can be convicted without personal knowledge, provided they had the authority to prevent or correct it. (b) fails because the facts do not show Avon had actual knowledge of the certificate issue. (c) fails because the *Park* doctrine expressly dispenses with the requirement of personal participation. (d) fails because delegation is not a defense under *Park*; executives must ensure compliance. (e) fails because public welfare offenses pierce the corporate veil to hold responsible officers personally liable.

**Tags:** chapters: [11], topics: [park doctrine, responsible corporate officer, corporate liability], difficulty: medium, cognitive: application

**Grounding:** Chapter 11 - Public Welfare Offenses (Park Doctrine — Foresight and Vigilance)

<!-- edge-case-audit: SHOULD FIX
1. Fact Pattern Booby Traps: The explicit directive from Avon to "keep it completely off the books" creates a trap. If the warehouse is completely off the corporate books, Barksdale Logistics (the corporation) may not actually be operating it in a legal sense, which weakens the application of the *Park* doctrine (which relies on a corporate officer's vicarious liability for a *corporate* violation). Furthermore, ordering an operation to be "off the books" is functionally a direct command to avoid filing official municipal registration paperwork, making Avon a direct principal/accomplice in the regulatory evasion rather than merely lacking knowledge as the explanation claims.
2. Cross-Doctrine Clashes: Direct Accomplice/Co-Conspirator Liability vs. *Park* Doctrine. Avon's direct command to conceal the warehouse triggers direct participation liability, which conceptually clashes with the *Park* doctrine's core premise of holding an otherwise uninvolved executive liable due to a failure to supervise. 
3. Cross-Question Spoilers: pass
Recommended fix: Clarify that the warehouse was officially leased by Barksdale Logistics (or a corporate subsidiary) to firmly anchor the corporate liability element. Alternatively, change Avon's dialogue so he doesn't explicitly command the evasion of official paperwork (e.g., have him simply say, "Set up the new warehouse, I'm leaving the logistics entirely to you").
-->

## Issue 3 — argpass-sonnet

**Q5.** Can Avon be convicted personally under the strict-liability municipal safety ordinance for the lack of a certificate?

(a) Guilty, because as the corporate CEO, he stands in a responsible relation to the violation and had authority to prevent it. <!-- correct -->
(b) Guilty, because the prosecution can prove he had actual, personal knowledge of the missing safety inspection certificate.
(c) Not guilty, because criminal liability requires proof that he personally participated in the daily operations of the warehouse.
(d) Not guilty, because he explicitly delegated all local logistics and operational decisions to his manager, Marlowe.
(e) Not guilty, because the corporate veil shields officers from individual criminal liability for municipal code violations.

**Answer:** (a)

**Explanation:** (a) is correct because under the *Park* doctrine, a corporate officer who stands in a "responsible relation" to a public welfare violation can be convicted without personal knowledge, provided they had the authority to prevent or correct it. (b) fails because the facts do not show Avon had actual knowledge of the certificate issue. (c) fails because the *Park* doctrine expressly dispenses with the requirement of personal participation. (d) fails because delegation is not a defense under *Park*; executives must ensure compliance. (e) fails because public welfare offenses pierce the corporate veil to hold responsible officers personally liable.

**Tags:** chapters: [11], topics: [park doctrine, responsible corporate officer, corporate liability], difficulty: medium, cognitive: application

**Grounding:** Chapter 11 - Public Welfare Offenses (Park Doctrine — Foresight and Vigilance)

<!-- argument-pass: SHOULD FIX
(a) Argument-for: Under the *United States v. Park* doctrine, a corporate officer can be held liable for strict-liability public welfare offenses if they stand in a "responsible relation" to the violation. This standard requires only that the officer possessed the authority and responsibility to prevent or correct the violation, not that they had actual knowledge. As the CEO, Avon holds ultimate authority over the corporation's municipal safety compliance, making him personally culpable under this doctrine.
(b) Argument-for: A student might choose this option if they believe traditional mens rea is always required or that the question implies guilt through actual awareness. They could argue that proving actual, personal knowledge is the safest, most traditional basis for an officer's criminal conviction, assuming the prosecution can easily infer or prove this fact against a CEO.
(c) Argument-for: Generally, an individual is not criminally liable for the acts of a corporation unless they personally committed, directed, or participated in the offense. A student could apply this baseline rule of corporate criminal liability to conclude that Avon's lack of daily operational involvement insulates him, making the argument that "personal participation is required" seem like a legally sound defense against vicarious liability.
(d) Argument-for: In many areas of law, reasonable delegation of duties to a competent subordinate severs the chain of proximate cause or negates the required mental state. A student might argue that by explicitly delegating local logistics to Marlowe, Avon successfully transferred his "responsible relation" and authority over the warehouse, thereby establishing a valid defense to personal criminal liability.
(e) Argument-for: The primary feature of the corporate form is limited liability, which protects officers and shareholders from individual responsibility for corporate actions. A student could argue that this structural protection extends to municipal code violations committed by the business entity. Without facts suggesting fraud or alter-ego liability, they would conclude the corporate veil categorically shields Avon.

Head-to-head: Option (a) correctly identifies the elements of the *Park* doctrine (responsible relation and authority to prevent) that permit a corporate officer's conviction for strict-liability public welfare offenses. Options (c), (d), and (e) are strong distractors because they each assert an explicit, falsifiable legal rule that fundamentally misstates corporate liability under *Park* (claiming personal participation is required, delegation is a total defense, and the corporate veil offers absolute protection, respectively). However, Option (b) is flawed under the close-call standard because it relies entirely on a factual assumption ("the prosecution can prove...") rather than positing a false legal claim. It fails on the facts rather than testing the student's legal understanding of the knowledge requirement. 

Falsifiable claim per distractor:
- (b): "because the prosecution can prove he had actual, personal knowledge" — wrong because it relies on a factual misstatement unsupported by the premise, rather than containing an explicit, identifiable false legal claim.
- (c): "criminal liability requires proof that he personally participated" — wrong because the *Park* doctrine expressly dispenses with the requirement of an officer's personal participation for public welfare offenses.
- (d): "because he explicitly delegated all local logistics" — wrong because delegation of duties does not legally sever the "responsible relation" or absolve a CEO of liability under the *Park* doctrine.
- (e): "corporate veil shields officers from individual criminal liability for municipal code violations" — wrong because the corporate form does not protect responsible corporate officers from personal criminal liability for their own omissions under public welfare statutes.

Recommended fix: Revise (b) to contain an explicit, falsifiable legal claim regarding the strict-liability knowledge requirement. For example: "(b) Not guilty, because securing a personal conviction for a strict-liability public welfare offense categorically requires proof of the officer's actual knowledge."
-->

## Issue 4 — argpass-opus

**Q5.** Can Avon be convicted personally under the strict-liability municipal safety ordinance for the lack of a certificate?

(a) Guilty, because as the corporate CEO, he stands in a responsible relation to the violation and had authority to prevent it. <!-- correct -->
(b) Guilty, because the prosecution can prove he had actual, personal knowledge of the missing safety inspection certificate.
(c) Not guilty, because criminal liability requires proof that he personally participated in the daily operations of the warehouse.
(d) Not guilty, because he explicitly delegated all local logistics and operational decisions to his manager, Marlowe.
(e) Not guilty, because the corporate veil shields officers from individual criminal liability for municipal code violations.

**Answer:** (a)

**Explanation:** (a) is correct because under the *Park* doctrine, a corporate officer who stands in a "responsible relation" to a public welfare violation can be convicted without personal knowledge, provided they had the authority to prevent or correct it. (b) fails because the facts do not show Avon had actual knowledge of the certificate issue. (c) fails because the *Park* doctrine expressly dispenses with the requirement of personal participation. (d) fails because delegation is not a defense under *Park*; executives must ensure compliance. (e) fails because public welfare offenses pierce the corporate veil to hold responsible officers personally liable.

**Tags:** chapters: [11], topics: [park doctrine, responsible corporate officer, corporate liability], difficulty: medium, cognitive: application

**Grounding:** Chapter 11 - Public Welfare Offenses (Park Doctrine — Foresight and Vigilance)

<!-- argument-pass: SHOULD FIX
(a) Argument-for: Under the *Park* doctrine, corporate officers can be held personally and criminally liable for strict-liability public welfare offenses if they have a "responsible relation" to the violation. This standard dictates that an officer with the authority and responsibility to prevent or correct the violation is liable even without personal knowledge or participation. As CEO, Avon possessed this authority, making him guilty under the ordinance.
(b) Argument-for: A student might argue that even if *Park* applies, a conviction is strongest when actual knowledge is present. If they infer from Avon's role as CEO that he must have known about the missing certificate, they would select this option. Actual knowledge would guarantee a conviction, rendering the strict-liability *Park* analysis a fallback rather than the primary theory of guilt.
(c) Argument-for: Generally, criminal liability disfavors vicarious liability and requires an *actus reus*—a voluntary act or personal participation by the defendant. A student could argue that without proof of Avon's personal involvement in the warehouse's daily operations, the foundational requirements for criminal blameworthiness are absent, precluding a personal conviction.
(d) Argument-for: While corporate officers have broad authority, a student might reason that reasonable, good-faith delegation to a competent manager (Marlowe) legally severs the officer's direct responsibility. By explicitly delegating local logistics, Avon arguably lacked the immediate power or duty to prevent this specific local violation, making him not guilty.
(e) Argument-for: The corporate veil is a fundamental doctrine that protects officers and shareholders from personal liability for the corporation's infractions. A student could plausibly argue that for a municipal code violation, the entity itself is the proper defendant, and the corporate veil strictly shields the CEO from individual criminal liability unless fraud or alter-ego exceptions apply.

Head-to-head: Option (a) correctly states the legal standard for responsible corporate officer liability under the *Park* doctrine. Options (c), (d), and (e) present legally false claims regarding the *Park* doctrine, specifically regarding personal participation, delegation, and the corporate veil. Option (b), however, relies on a purely factual assertion ("the prosecution can prove he had actual, personal knowledge") that contradicts the implied facts of the question. Because (b) lacks an explicit, falsifiable *legal* claim and functions purely as a factual misstatement, it fails the close-call standard for high-quality distractors.

Falsifiable claim per distractor:
- (b): "the prosecution can prove he had actual, personal knowledge" — wrong because this is a factual misstatement rather than an explicit, falsifiable legal proposition, violating the requirement to lock distractors with false legal claims.
- (c): "criminal liability requires proof that he personally participated" — wrong because the *Park* doctrine explicitly dispenses with the requirement of personal participation for public welfare offenses.
- (d): "because he explicitly delegated all local logistics and operational decisions" — wrong because legal delegation does not sever liability or act as a defense under the *Park* doctrine.
- (e): "the corporate veil shields officers from individual criminal liability for municipal code violations" — wrong because the *Park* doctrine specifically allows responsible officers to be held personally liable for public welfare offenses, bypassing the traditional corporate veil.

Recommended fix: Edit (b) to contain a false, locked legal proposition rather than a factual mismatch. For example: "(b) Guilty, solely because corporate executives are automatically liable for any code violation committed by an employee, regardless of whether the executive had the authority to prevent it." Also, consider locking (d) with an absolute word (e.g., "...because explicitly delegating all local logistics categorically severs his responsible relation").
-->
