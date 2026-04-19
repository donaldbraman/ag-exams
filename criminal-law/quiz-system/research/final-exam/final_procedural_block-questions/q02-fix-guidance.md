# Fix Guidance for q02

The QA pipeline flagged this question. Rewrite `q02.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — grounding

**Q2.** Jurisdictions split on the mens rea for accomplice liability. Under the majority purpose standard (e.g., *Peoni*), is Steve guilty as an accomplice to the underlying narcotics distribution?

(a) Yes, because providing specific logistical assistance to a known criminal operation inherently demonstrates a legal purpose to actively promote and facilitate the completion of the underlying crime.
(b) Yes, because Steve acted entirely voluntarily when he affirmatively drafted the evasive routes at Kevin's specific explicit direction to effectively avoid the regional state weigh stations.
(c) No, because Steve merely knew about the criminal activity but lacked a true stake in the venture's success, acting only to maintain his standard legitimate legal fees. <!-- correct -->
(d) No, because outside corporate counsel absolutely cannot be held criminally liable for providing standard logistical or legal advice to a legitimately incorporated commercial waste management corporate entity.
(e) No, because the mere act of drafting corporate trucking routes is a strictly lawful activity and therefore cannot ever legally constitute the required actus reus for accomplice liability.

**Answer:** (c)

**Explanation:** The common law purpose standard, exemplified by *Peoni*, requires an accomplice to have a "stake in the venture" and a true purpose to facilitate the crime. Steve drafted the routes purely for legitimate compensation without a vested interest in the narcotics ring, making (c) correct. (a) is incorrect because providing assistance with mere knowledge is insufficient under the purpose standard. (b) is incorrect because voluntary action with knowledge does not automatically elevate to purposive intent. (d) is incorrect because corporate counsel can be liable if they genuinely share the illicit purpose. (e) is incorrect because otherwise lawful acts can constitute the actus reus for accomplice liability if coupled with the requisite criminal mens rea.

**Tags:** chapters: [13], topics: [accomplice liability, purpose vs knowledge, Peoni], difficulty: medium, cognitive: analysis

**Grounding:** United States v. Peoni establishes that mere knowledge of illicit activity by a provider of routine goods or services is insufficient for accomplice liability without a specific purpose to promote or facilitate the crime (a "stake in the venture").

<!-- GROUNDING-FAIL: Accomplice liability purpose standard (Peoni) is not in any chapter map. The closest taught doctrines are: none (chapter map corpus is missing from the prompt). Correct answer must rely on one of those instead. -->

## Issue 2 — audit

**Q2.** Jurisdictions split on the mens rea for accomplice liability. Under the majority purpose standard (e.g., *Peoni*), is Steve guilty as an accomplice to the underlying narcotics distribution?

(a) Yes, because providing specific logistical assistance to a known criminal operation inherently demonstrates a legal purpose to actively promote and facilitate the completion of the underlying crime.
(b) Yes, because Steve acted entirely voluntarily when he affirmatively drafted the evasive routes at Kevin's specific explicit direction to effectively avoid the regional state weigh stations.
(c) No, because Steve merely knew about the criminal activity but lacked a true stake in the venture's success, acting only to maintain his standard legitimate legal fees. <!-- correct -->
(d) No, because outside corporate counsel absolutely cannot be held criminally liable for providing standard logistical or legal advice to a legitimately incorporated commercial waste management corporate entity.
(e) No, because the mere act of drafting corporate trucking routes is a strictly lawful activity and therefore cannot ever legally constitute the required actus reus for accomplice liability.

**Answer:** (c)

**Explanation:** The common law purpose standard, exemplified by *Peoni*, requires an accomplice to have a "stake in the venture" and a true purpose to facilitate the crime. Steve drafted the routes purely for legitimate compensation without a vested interest in the narcotics ring, making (c) correct. (a) is incorrect because providing assistance with mere knowledge is insufficient under the purpose standard. (b) is incorrect because voluntary action with knowledge does not automatically elevate to purposive intent. (d) is incorrect because corporate counsel can be liable if they genuinely share the illicit purpose. (e) is incorrect because otherwise lawful acts can constitute the actus reus for accomplice liability if coupled with the requisite criminal mens rea.

**Tags:** chapters: [13], topics: [accomplice liability, purpose vs knowledge, Peoni], difficulty: medium, cognitive: analysis

**Grounding:** United States v. Peoni establishes that mere knowledge of illicit activity by a provider of routine goods or services is insufficient for accomplice liability without a specific purpose to promote or facilitate the crime (a "stake in the venture").

<!-- audit: MUST FIX
check 1: pass (assuming the missing facts support the correct answer)
check 2: pass
check 3: pass
check 4: FAIL - The stem is completely missing the fact pattern. There are no facts detailing who Steve and Kevin are, the waste management company, the trucking routes, or Steve's compensation structure.
check 5: pass
check 6: pass
check 7: pass
check 8: pass
Recommended fix: Insert the missing scenario/fact pattern detailing Steve's role, Kevin's directions, and the fee structure before the question stub.
-->

## Issue 3 — edge-case

**Q2.** Jurisdictions split on the mens rea for accomplice liability. Under the majority purpose standard (e.g., *Peoni*), is Steve guilty as an accomplice to the underlying narcotics distribution?

(a) Yes, because providing specific logistical assistance to a known criminal operation inherently demonstrates a legal purpose to actively promote and facilitate the completion of the underlying crime.
(b) Yes, because Steve acted entirely voluntarily when he affirmatively drafted the evasive routes at Kevin's specific explicit direction to effectively avoid the regional state weigh stations.
(c) No, because Steve merely knew about the criminal activity but lacked a true stake in the venture's success, acting only to maintain his standard legitimate legal fees. <!-- correct -->
(d) No, because outside corporate counsel absolutely cannot be held criminally liable for providing standard logistical or legal advice to a legitimately incorporated commercial waste management corporate entity.
(e) No, because the mere act of drafting corporate trucking routes is a strictly lawful activity and therefore cannot ever legally constitute the required actus reus for accomplice liability.

**Answer:** (c)

**Explanation:** The common law purpose standard, exemplified by *Peoni*, requires an accomplice to have a "stake in the venture" and a true purpose to facilitate the crime. Steve drafted the routes purely for legitimate compensation without a vested interest in the narcotics ring, making (c) correct. (a) is incorrect because providing assistance with mere knowledge is insufficient under the purpose standard. (b) is incorrect because voluntary action with knowledge does not automatically elevate to purposive intent. (d) is incorrect because corporate counsel can be liable if they genuinely share the illicit purpose. (e) is incorrect because otherwise lawful acts can constitute the actus reus for accomplice liability if coupled with the requisite criminal mens rea.

**Tags:** chapters: [13], topics: [accomplice liability, purpose vs knowledge, Peoni], difficulty: medium, cognitive: analysis

**Grounding:** United States v. Peoni establishes that mere knowledge of illicit activity by a provider of routine goods or services is insufficient for accomplice liability without a specific purpose to promote or facilitate the crime (a "stake in the venture").

<!-- edge-case-audit: MUST FIX
1. Fact Pattern Booby Traps: pass
2. Cross-Doctrine Clashes: pass
3. Cross-Question Spoilers: Fact 4 establishes that Steve is storing 5 kilograms of packaged cocaine in his locked private office cabinet. This massive act of physical assistance to the drug ring strongly suggests he IS an accomplice to the distribution operation, spoiling the intended negative answer for this question which was meant to evaluate only his route-drafting.
Recommended fix: Add a limiting phrase to the question stem to isolate the tested conduct. For example: "Based solely on his act of drafting the evasive routes, is Steve guilty..."
-->

## Issue 4 — argpass-sonnet

**Q2.** Jurisdictions split on the mens rea for accomplice liability. Under the majority purpose standard (e.g., *Peoni*), is Steve guilty as an accomplice to the underlying narcotics distribution?

(a) Yes, because providing specific logistical assistance to a known criminal operation inherently demonstrates a legal purpose to actively promote and facilitate the completion of the underlying crime.
(b) Yes, because Steve acted entirely voluntarily when he affirmatively drafted the evasive routes at Kevin's specific explicit direction to effectively avoid the regional state weigh stations.
(c) No, because Steve merely knew about the criminal activity but lacked a true stake in the venture's success, acting only to maintain his standard legitimate legal fees. <!-- correct -->
(d) No, because outside corporate counsel absolutely cannot be held criminally liable for providing standard logistical or legal advice to a legitimately incorporated commercial waste management corporate entity.
(e) No, because the mere act of drafting corporate trucking routes is a strictly lawful activity and therefore cannot ever legally constitute the required actus reus for accomplice liability.

**Answer:** (c)

**Explanation:** The common law purpose standard, exemplified by *Peoni*, requires an accomplice to have a "stake in the venture" and a true purpose to facilitate the crime. Steve drafted the routes purely for legitimate compensation without a vested interest in the narcotics ring, making (c) correct. (a) is incorrect because providing assistance with mere knowledge is insufficient under the purpose standard. (b) is incorrect because voluntary action with knowledge does not automatically elevate to purposive intent. (d) is incorrect because corporate counsel can be liable if they genuinely share the illicit purpose. (e) is incorrect because otherwise lawful acts can constitute the actus reus for accomplice liability if coupled with the requisite criminal mens rea.

**Tags:** chapters: [13], topics: [accomplice liability, purpose vs knowledge, Peoni], difficulty: medium, cognitive: analysis

**Grounding:** United States v. Peoni establishes that mere knowledge of illicit activity by a provider of routine goods or services is insufficient for accomplice liability without a specific purpose to promote or facilitate the crime (a "stake in the venture").

<!-- argument-pass: SHOULD FIX
(a) Argument-for: Under the purpose standard, a provider of services can sometimes be held liable if their services are highly customized to the criminal enterprise. A student could argue that providing "specific logistical assistance" like evasive routes to a "known criminal operation" goes beyond the generic sales in *Peoni*. They might conclude that such tailored assistance inherently demonstrates a purpose to actively promote the completion of the crime.
(b) Argument-for: Accomplice liability requires an affirmative act paired with the requisite mens rea. Steve drafted evasive routes at the principal's explicit direction. A student might argue that acting voluntarily to draft routes specifically designed to avoid law enforcement shows he shared the illicit goal. This voluntary, affirmative adaptation of his services to aid evasion could arguably satisfy the requirement of purposeful facilitation.
(c) Argument-for: The *Peoni* standard distinguishes between those who merely know of a crime and those who have a "stake in the venture." Steve was acting solely to maintain his standard legitimate legal fees, meaning he did not share in the profits of the narcotics ring. Without this purposive stake, mere knowledge and provision of services do not meet the strict mens rea for accomplice liability.
(d) Argument-for: Legal counsel often provides advice that could be misused by clients. A student could argue that policy protections for attorneys shield them from accomplice liability when offering standard logistical or legal advice to legitimately incorporated entities. Under this view, corporate counsel absolutely cannot be held criminally liable for rendering such standard advice, regardless of the client's underlying conduct.
(e) Argument-for: The actus reus for accomplice liability generally requires aiding, abetting, or counseling the crime. Drafting corporate trucking routes is, on its face, a strictly lawful commercial activity. A student could argue that engaging in an independently lawful act cannot ever legally constitute the actus reus for accomplice liability, as the act itself must be inherently wrongful.

Head-to-head:
Option (c) perfectly tracks the *Peoni* "stake in the venture" requirement, correctly concluding that Steve is not liable. Option (a) incorrectly claims that logistical assistance "inherently" demonstrates purpose. Option (b) attempts to equate voluntary compliance with explicit directions to purposive intent, but fails to include an absolute legal falsifier, making it rely on an implicit omission. Option (d) incorrectly asserts an absolute immunity for outside corporate counsel. Option (e) relies on the explicitly false legal premise that lawful acts "cannot ever" constitute an actus reus for accomplice liability. Because (b) relies on an implicit omission of the purpose requirement rather than stating an explicitly false legal rule locked by an absolute word, it falls short of the close-call standard and requires a fix.

Falsifiable claim per distractor:
- (a): "inherently demonstrates a legal purpose" — wrong because providing logistical assistance with mere knowledge does not inherently equate to a purpose to promote the crime under *Peoni*.
- (b): "Yes, because Steve acted entirely voluntarily..." — wrong because voluntary action with knowledge does not legally equate to purposive intent, but the option lacks an absolute word to firmly lock the false rule.
- (d): "absolutely cannot be held criminally liable" — wrong because attorneys can be accomplices if they share the criminal purpose.
- (e): "cannot ever legally constitute the required actus reus" — wrong because lawful acts can form the actus reus if paired with the correct mens rea.

Recommended fix: Edit (b) to lock the false legal claim with an absolute word: "(b) Yes, because acting entirely voluntarily to draft evasive routes at a principal's explicit direction automatically satisfies the purpose standard for accomplice liability."
-->
