# Fix Guidance for q11

The QA pipeline flagged this question. Rewrite `q11.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — grounding

**Q11.** Under the Supreme Court's decision in *McDonnell v. United States*, does Governor Hayes's pressure on the Attorney General constitute an "official act" for the purposes of honest-services fraud?

(a) Yes, because holding a private meeting with a constituent is universally recognized by the courts as a formal and criminalized exercise of governmental power.
(b) Yes, because threatening to reassign the lead investigator constitutes a formal exercise of governmental power on a specific, pending matter before the state agency. <!-- correct -->
(c) No, because the Attorney General ultimately refused to drop the case, meaning the Governor's pressure did not result in a finalized governmental action.
(d) No, because the Supreme Court limits official acts exclusively to voting on legislation or signing executive orders, which did not occur in this situation.
(e) No, because the Governor was acting in his capacity as a political party leader managing a Super PAC rather than executing his official gubernatorial duties.

**Answer:** (b)

**Explanation:** In *McDonnell v. United States*, the Supreme Court narrowed the definition of an "official act" to require a formal exercise of governmental power on a specific, pending matter (a "question, matter, cause, suit, proceeding or controversy"). Threatening to use state power to reassign a lead investigator on the pending Vance case satisfies this standard (Fact 9). (b) is correct. (a) is wrong because *McDonnell* explicitly held that merely hosting a meeting or event does not constitute an official act. (c) is wrong because the official act is the formal exercise of pressure itself; the bribery statute does not require the corrupt pressure to successfully achieve its end goal. (d) is wrong because official acts encompass actions like formally reassigning personnel on a specific case, not just voting on legislation. (e) is wrong because leveraging state executive power over an investigator is a gubernatorial act, regardless of his political roles.

**Tags:** chapters: [8], topics: [honest-services-fraud, mcdonnell, official-act], difficulty: hard, cognitive: application

**Grounding:** McDonnell v. United States, 579 U.S. 550 (2016)

<!-- GROUNDING-FAIL: honest-services fraud / McDonnell v. United States is not in any chapter map. The closest taught doctrines are: none. Correct answer must rely on one of those instead. -->

## Issue 2 — audit

**Q11.** Under the Supreme Court's decision in *McDonnell v. United States*, does Governor Hayes's pressure on the Attorney General constitute an "official act" for the purposes of honest-services fraud?

(a) Yes, because holding a private meeting with a constituent is universally recognized by the courts as a formal and criminalized exercise of governmental power.
(b) Yes, because threatening to reassign the lead investigator constitutes a formal exercise of governmental power on a specific, pending matter before the state agency. <!-- correct -->
(c) No, because the Attorney General ultimately refused to drop the case, meaning the Governor's pressure did not result in a finalized governmental action.
(d) No, because the Supreme Court limits official acts exclusively to voting on legislation or signing executive orders, which did not occur in this situation.
(e) No, because the Governor was acting in his capacity as a political party leader managing a Super PAC rather than executing his official gubernatorial duties.

**Answer:** (b)

**Explanation:** In *McDonnell v. United States*, the Supreme Court narrowed the definition of an "official act" to require a formal exercise of governmental power on a specific, pending matter (a "question, matter, cause, suit, proceeding or controversy"). Threatening to use state power to reassign a lead investigator on the pending Vance case satisfies this standard (Fact 9). (b) is correct. (a) is wrong because *McDonnell* explicitly held that merely hosting a meeting or event does not constitute an official act. (c) is wrong because the official act is the formal exercise of pressure itself; the bribery statute does not require the corrupt pressure to successfully achieve its end goal. (d) is wrong because official acts encompass actions like formally reassigning personnel on a specific case, not just voting on legislation. (e) is wrong because leveraging state executive power over an investigator is a gubernatorial act, regardless of his political roles.

**Tags:** chapters: [8], topics: [honest-services-fraud, mcdonnell, official-act], difficulty: hard, cognitive: application

**Grounding:** McDonnell v. United States, 579 U.S. 550 (2016)

<!-- audit: MUST FIX
Check 1: pass (the legal standard in the correct answer accurately reflects McDonnell)
Check 2: pass
Check 3: pass
Check 4: MUST FIX (The stem does not provide the facts needed to answer. It asks about "Governor Hayes's pressure" and the explanation refers to "Fact 9" and "the pending Vance case", but there is no overarching fact pattern provided. A student cannot determine the correct answer without knowing what the pressure actually was.)
Check 5: pass
Check 6: pass
Check 7: pass
Check 8: pass (options are highly symmetrical; 24-26 words each)
Recommended fix: Integrate the necessary facts into the stem. For example: "If Governor Hayes threatened to use his state power to reassign a lead investigator on a pending state case unless the Attorney General dropped it, does this pressure constitute an 'official act'..."
-->

## Issue 3 — argpass-sonnet

**Q11.** Under the Supreme Court's decision in *McDonnell v. United States*, does Governor Hayes's pressure on the Attorney General constitute an "official act" for the purposes of honest-services fraud?

(a) Yes, because holding a private meeting with a constituent is universally recognized by the courts as a formal and criminalized exercise of governmental power.
(b) Yes, because threatening to reassign the lead investigator constitutes a formal exercise of governmental power on a specific, pending matter before the state agency. <!-- correct -->
(c) No, because the Attorney General ultimately refused to drop the case, meaning the Governor's pressure did not result in a finalized governmental action.
(d) No, because the Supreme Court limits official acts exclusively to voting on legislation or signing executive orders, which did not occur in this situation.
(e) No, because the Governor was acting in his capacity as a political party leader managing a Super PAC rather than executing his official gubernatorial duties.

**Answer:** (b)

**Explanation:** In *McDonnell v. United States*, the Supreme Court narrowed the definition of an "official act" to require a formal exercise of governmental power on a specific, pending matter (a "question, matter, cause, suit, proceeding or controversy"). Threatening to use state power to reassign a lead investigator on the pending Vance case satisfies this standard (Fact 9). (b) is correct. (a) is wrong because *McDonnell* explicitly held that merely hosting a meeting or event does not constitute an official act. (c) is wrong because the official act is the formal exercise of pressure itself; the bribery statute does not require the corrupt pressure to successfully achieve its end goal. (d) is wrong because official acts encompass actions like formally reassigning personnel on a specific case, not just voting on legislation. (e) is wrong because leveraging state executive power over an investigator is a gubernatorial act, regardless of his political roles.

**Tags:** chapters: [8], topics: [honest-services-fraud, mcdonnell, official-act], difficulty: hard, cognitive: application

**Grounding:** McDonnell v. United States, 579 U.S. 550 (2016)

<!-- argument-pass: SHOULD FIX
(a) Argument-for: A student might choose (a) if they believe that any official meeting arranged by a governor inherently constitutes a formal exercise of power. Prior to *McDonnell*, prosecutors often argued that selling access (like private meetings) was a corrupt official act, and a student relying on this broader, historical view might think such meetings are universally recognized as criminalized official acts.
(b) Argument-for: A student would select (b) because it perfectly matches the *McDonnell* test. The Supreme Court required a formal exercise of governmental power on a specific, pending matter ("question, matter, cause, suit, proceeding or controversy"). Threatening to reassign an investigator on an ongoing case is a direct and formal use of executive authority over a specific administrative proceeding.
(c) Argument-for: A student might choose (c) by mistaking the elements of bribery. They could reason that since the Attorney General refused to drop the case, the governor's pressure was merely an unsuccessful attempt rather than a completed official act, leading to the logical (though legally incorrect) conclusion that without a finalized governmental action, there is no honest-services fraud.
(d) Argument-for: A student could select (d) by over-applying the limitations introduced by *McDonnell*. Because the Court explicitly excluded informal actions like setting up meetings, a student might mistakenly believe the definition was narrowed exclusively to textbook formal acts—such as voting on legislation or signing executive orders—thereby excluding personnel threats.
(e) Argument-for: A student might choose (e) by focusing on the governor's concurrent political roles. *McDonnell* requires the exercise of official state power; a student could incorrectly categorize the governor's pressure as pure political maneuvering tied to his Super PAC rather than his official gubernatorial duties, concluding the conduct falls outside the statute's scope.

Head-to-head: Option (b) is the clear and correct application of the *McDonnell* standard, correctly identifying that threatening to reassign a lead investigator is a formal exercise of power on a specific pending matter. Distractors (a) and (d) contain explicitly false legal claims locked by strong language ("universally recognized" and "exclusively to"). However, distractors (c) and (e) fail the close-call standard because they lack explicit, identifiable false legal claims. Option (c) relies on an implicit omission (that an official act requires a successfully finalized action), and option (e) relies on a factual characterization of the governor's capacity rather than asserting an absolute, falsifiable legal rule. 

Falsifiable claim per distractor:
- (a): "universally recognized by the courts as a formal and criminalized exercise of governmental power" — wrong because McDonnell explicitly ruled that merely hosting a meeting is not an official act.
- (c): "meaning the Governor's pressure did not result in a finalized governmental action" — wrong implicitly, but fails the strict standard because it lacks an absolute, falsifiable legal proposition (e.g., that honest-services fraud categorically requires a successfully completed end-result).
- (d): "limits official acts exclusively to voting on legislation or signing executive orders" — wrong because McDonnell also encompasses other formal exercises of power, such as administrative decisions or personnel reassignments on specific matters.
- (e): "because the Governor was acting in his capacity as a political party leader... rather than executing his official gubernatorial duties" — wrong factually according to the prompt's premise, but lacks an explicit false legal claim about dual-capacity actors shielding themselves from liability.

Recommended fix: Edit (c) to: "No, because an 'official act' categorically requires that the corrupt pressure successfully dictate a finalized governmental outcome." Edit (e) to: "No, because political pressure exerted by a party leader automatically falls outside the scope of honest-services fraud, regardless of whether state executive power is leveraged."
-->

## Issue 4 — argpass-opus

**Q11.** Under the Supreme Court's decision in *McDonnell v. United States*, does Governor Hayes's pressure on the Attorney General constitute an "official act" for the purposes of honest-services fraud?

(a) Yes, because holding a private meeting with a constituent is universally recognized by the courts as a formal and criminalized exercise of governmental power.
(b) Yes, because threatening to reassign the lead investigator constitutes a formal exercise of governmental power on a specific, pending matter before the state agency. <!-- correct -->
(c) No, because the Attorney General ultimately refused to drop the case, meaning the Governor's pressure did not result in a finalized governmental action.
(d) No, because the Supreme Court limits official acts exclusively to voting on legislation or signing executive orders, which did not occur in this situation.
(e) No, because the Governor was acting in his capacity as a political party leader managing a Super PAC rather than executing his official gubernatorial duties.

**Answer:** (b)

**Explanation:** In *McDonnell v. United States*, the Supreme Court narrowed the definition of an "official act" to require a formal exercise of governmental power on a specific, pending matter (a "question, matter, cause, suit, proceeding or controversy"). Threatening to use state power to reassign a lead investigator on the pending Vance case satisfies this standard (Fact 9). (b) is correct. (a) is wrong because *McDonnell* explicitly held that merely hosting a meeting or event does not constitute an official act. (c) is wrong because the official act is the formal exercise of pressure itself; the bribery statute does not require the corrupt pressure to successfully achieve its end goal. (d) is wrong because official acts encompass actions like formally reassigning personnel on a specific case, not just voting on legislation. (e) is wrong because leveraging state executive power over an investigator is a gubernatorial act, regardless of his political roles.

**Tags:** chapters: [8], topics: [honest-services-fraud, mcdonnell, official-act], difficulty: hard, cognitive: application

**Grounding:** McDonnell v. United States, 579 U.S. 550 (2016)

<!-- argument-pass: SHOULD FIX
(a) Argument-for: A student might choose this option if they recall that the underlying conduct in *McDonnell* involved setting up meetings and organizing events. Because the Governor's overall scheme involved illicitly trading access for gifts, a student could mistakenly conclude that the meetings themselves are the core criminalized official acts under the statute, provided there is corrupt intent. Furthermore, they could argue that arranging such a meeting to exert influence is inherently an exercise of the office's power.
(b) Argument-for: This is the correct application of *McDonnell*. The Court held that an "official act" involves a formal exercise of governmental power on a specific, pending matter. A pending state investigation is a specific matter under the law. Threatening to use gubernatorial power to reassign the lead investigator constitutes a formal exercise of state power to decide or act on that matter, cleanly meeting the Court's narrowed definition.
(c) Argument-for: A student could defend this by arguing that an attempt to influence another official that ultimately fails doesn't ripen into an "official act." Since the Attorney General refused to drop the case, the student might reason that no actual, finalized governmental decision was made. Therefore, they could conclude this puts the Governor's conduct outside the strict *McDonnell* definition of a formalized decision or action.
(d) Argument-for: A student might select this by remembering that *McDonnell* severely narrowed the definition of an "official act" to prevent the criminalization of everyday political favors. They might over-read this narrowing to mean that only the most formal, explicit, and legally binding actions qualify. Consequently, a student could believe that actions must be as codified as voting on a bill or signing an executive order to be deemed "official."
(e) Argument-for: A student could justify this if they view the Governor's pressure as primarily political arm-twisting rather than an exercise of formal executive power. If the Governor is acting under his political hat to protect a donor via his Super PAC role, the student might argue the conduct is merely political networking. They might conclude that because the motivation and context were political, the threat fell outside his official administrative duties.

Head-to-head: Option (b) correctly applies the *McDonnell* standard, as threatening to reassign a state investigator is a formal exercise of state power concerning a specific, pending matter. Distractor (a) contains an explicit false claim because *McDonnell* specifically excluded mere meetings from the definition of an official act. Distractor (d) is easily falsifiable due to its absolutist phrasing ("exclusively to voting on legislation"). Distractor (e) asserts a false factual and legal characterization, as leveraging authority over a state investigator is inherently an executive duty, regardless of the political motive. Distractor (c) implies a false legal requirement—that an official act must succeed or result in a finalized governmental action—but lacks the absolute wording ("always," "categorically") required to make this an unassailable, explicit false legal claim, making it the weakest distractor structurally.

Falsifiable claim per distractor:
- (a): "universally recognized by the courts as a formal and criminalized exercise of governmental power" — wrong because *McDonnell* explicitly held that setting up meetings or hosting events does not, by itself, constitute an official act.
- (c): "meaning the Governor's pressure did not result in a finalized governmental action" — wrong because the bribery statute and *McDonnell* do not require the corrupt pressure to succeed; exerting pressure on another official regarding a specific, pending matter is itself an official act.
- (d): "limits official acts exclusively to voting on legislation or signing executive orders" — wrong because official acts also encompass administrative decisions, such as exerting formal pressure on pending agency investigations.
- (e): "rather than executing his official gubernatorial duties" — wrong because threatening to reassign a state agency's lead investigator inherently relies on official state executive authority, not just political party leadership.

Recommended fix: Change (c) to: "No, because an official act categorically requires a successful and finalized governmental action, which did not occur here since the Attorney General refused to drop the case."
-->
