# Fix Guidance for q06

The QA pipeline flagged this question. Rewrite `q06.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q6.** Assume Marlowe is charged with an omission-based offense for failing to call 911 when the fire broke out. Did he have a legal duty to act?

(a) Duty, because every citizen has a general legal obligation to rescue individuals who are in imminent physical danger.
(b) Duty, because by ordering the chemical processing that sparked the fire, he contributed to the creation of the peril. <!-- correct -->
(c) Duty, because a formal contractual relationship existed between the employer and employee regarding warehouse safety standards.
(d) No duty, because he did not possess the specific intent to start the chemical fire or harm his employee.
(e) No duty, because the immediate cause of the fire was Wallace's involuntary convulsion rather than Marlowe's direct actions.

**Answer:** (b)

**Explanation:** (b) is correct because one of the established common law exceptions to the no-duty-to-act rule is the creation of peril. Because Marlowe's directions initiated the chemical processing that ultimately caused the fire, he had a legal duty to intervene or call for help. (a) fails because there is no general good-samaritan duty to rescue in American criminal law. (c) fails because standard employment does not automatically create a specific contractual duty of rescue. (d) fails because the creation of peril exception triggers a duty regardless of whether the initial act was intentional or accidental. (e) fails because Marlowe still initiated the chain of events, establishing his contribution to the peril.

**Tags:** chapters: [9], topics: [omissions, creation of peril, duty to act], difficulty: medium, cognitive: application

**Grounding:** Chapter 9 - Omissions (Creation of Peril Category)

<!-- audit: MUST FIX
<check 1>: pass on the doctrine, but impossible to verify accuracy without the missing facts.
<check 2>: pass.
<check 3>: pass.
<check 4>: FAIL. The stem is entirely missing the fact pattern needed to answer the question. It refers to "the fire" but omits any details about Marlowe ordering chemical processing, an employee named Wallace, an involuntary convulsion, or the employer/employee relationship. It appears this question was separated from a master fact pattern.
<check 5>: pass.
<check 6>: pass.
<check 7>: pass (maps to `creation-of-peril-category` in Ch 9).
Recommended fix: Add a brief factual scenario to the stem so it is self-contained. For example: "Marlowe, a warehouse manager, ordered his employee Wallace to begin chemical processing. Wallace suffered an involuntary convulsion that knocked over a beaker, starting a fire. Marlowe stood by and failed to call 911. Assume Marlowe is charged with an omission-based offense..."
-->

## Issue 2 — argpass-sonnet

**Q6.** Assume Marlowe is charged with an omission-based offense for failing to call 911 when the fire broke out. Did he have a legal duty to act?

(a) Duty, because every citizen has a general legal obligation to rescue individuals who are in imminent physical danger.
(b) Duty, because by ordering the chemical processing that sparked the fire, he contributed to the creation of the peril. <!-- correct -->
(c) Duty, because a formal contractual relationship existed between the employer and employee regarding warehouse safety standards.
(d) No duty, because he did not possess the specific intent to start the chemical fire or harm his employee.
(e) No duty, because the immediate cause of the fire was Wallace's involuntary convulsion rather than Marlowe's direct actions.

**Answer:** (b)

**Explanation:** (b) is correct because one of the established common law exceptions to the no-duty-to-act rule is the creation of peril. Because Marlowe's directions initiated the chemical processing that ultimately caused the fire, he had a legal duty to intervene or call for help. (a) fails because there is no general good-samaritan duty to rescue in American criminal law. (c) fails because standard employment does not automatically create a specific contractual duty of rescue. (d) fails because the creation of peril exception triggers a duty regardless of whether the initial act was intentional or accidental. (e) fails because Marlowe still initiated the chain of events, establishing his contribution to the peril.

**Tags:** chapters: [9], topics: [omissions, creation of peril, duty to act], difficulty: medium, cognitive: application

**Grounding:** Chapter 9 - Omissions (Creation of Peril Category)

<!-- argument-pass: MUST FIX
(a) Argument-for: A student could argue that modern criminal law imposes a universal baseline duty to notify authorities (e.g., calling 911) in extreme life-or-death scenarios. By conflating moral obligations with legal ones, they might believe that the severity of "imminent physical danger" overrides the general no-duty-to-act rule, creating an absolute obligation for any citizen present.
(b) Argument-for: This relies on the orthodox "creation of peril" exception to omissions. Under this doctrine, when a defendant's actions—even if lawful or innocent—set in motion the forces that lead to a perilous situation, the law imposes an affirmative duty to mitigate the harm or summon help. By ordering the chemical processing, Marlowe initiated the causal chain, triggering this duty.
(c) Argument-for: A student could argue that the employer-employee relationship inherently acts as a formal contract governing workplace safety (e.g., implied OSHA compliance). Because contractual duty is a recognized exception to the no-duty-to-act rule, the student might conclude that this specific employment contract explicitly covered warehouse safety standards, legally obligating Marlowe to rescue.
(d) Argument-for: A student might argue that criminal liability generally requires a culpable *mens rea* tied to the duty-triggering event. They could reason that for the "creation of peril" doctrine to impose criminal omission liability, the defendant must have culpably (with specific intent) created the danger. Since Marlowe lacked specific intent, he didn't culpably create the peril.
(e) Argument-for: A student could convincingly argue that the "creation of peril" doctrine requires the defendant's acts to be the proximate, direct cause of the danger. Wallace's unforeseeable, involuntary convulsion serves as an intervening superseding cause that severs the causal chain. Because Marlowe merely ordered a standard task and Wallace's seizure was the true immediate cause, Marlowe did not "create" the peril in the direct legal sense required to trigger a duty.

Head-to-head: The question pits the "creation of peril" doctrine (b) against causation defenses (e) and *mens rea* defenses (d). Option (b) is the intended key, but (e) presents a highly viable, potentially superior legal argument. In strict criminal causation, if an independent involuntary act (Wallace's convulsion) is the direct, immediate cause of the peril, an employer merely ordering a standard, legal task may not satisfy the *actus reus* of "creating the peril." Thus, (e) could be legally correct in many jurisdictions. Furthermore, (c) relies on a factual assumption ("a formal contractual relationship existed") rather than presenting a legally false claim, and (e) lacks an absolute locking word, failing the close-call standard. 

Falsifiable claim per distractor:
- (a): "every citizen has a general legal obligation" — wrong because American common law categorically rejects a general duty to rescue or intervene.
- (c): "a formal contractual relationship existed" — wrong because it is an unsupported factual assertion rather than a false legal rule. If assumed true, the legal conclusion would arguably be correct. It lacks a falsifiable legal absolute.
- (d): "because he did not possess the specific intent" — wrong because the creation of peril exception triggers a duty regardless of whether the initial act creating the danger was intentional, reckless, or entirely innocent.
- (e): "rather than Marlowe's direct actions" — wrong (intended) because indirect contribution can trigger the duty, but this distractor fails to explicitly state a universally false legal rule using absolute terms (e.g., "categorically requires direct physical action"). 

Recommended fix: 
1. Rewrite (c) to contain a false legal absolute: "Duty, because standard employment relationships categorically create a formal contractual obligation to rescue."
2. Rewrite (e) to make its legal premise absolutely and explicitly false, thereby preserving (b) as the unambiguous key: "No duty, because the creation of peril exception categorically applies solely when the defendant's direct physical actions are the immediate and only cause of the danger."
-->

## Issue 3 — argpass-opus

**Q6.** Assume Marlowe is charged with an omission-based offense for failing to call 911 when the fire broke out. Did he have a legal duty to act?

(a) Duty, because every citizen has a general legal obligation to rescue individuals who are in imminent physical danger.
(b) Duty, because by ordering the chemical processing that sparked the fire, he contributed to the creation of the peril. <!-- correct -->
(c) Duty, because a formal contractual relationship existed between the employer and employee regarding warehouse safety standards.
(d) No duty, because he did not possess the specific intent to start the chemical fire or harm his employee.
(e) No duty, because the immediate cause of the fire was Wallace's involuntary convulsion rather than Marlowe's direct actions.

**Answer:** (b)

**Explanation:** (b) is correct because one of the established common law exceptions to the no-duty-to-act rule is the creation of peril. Because Marlowe's directions initiated the chemical processing that ultimately caused the fire, he had a legal duty to intervene or call for help. (a) fails because there is no general good-samaritan duty to rescue in American criminal law. (c) fails because standard employment does not automatically create a specific contractual duty of rescue. (d) fails because the creation of peril exception triggers a duty regardless of whether the initial act was intentional or accidental. (e) fails because Marlowe still initiated the chain of events, establishing his contribution to the peril.

**Tags:** chapters: [9], topics: [omissions, creation of peril, duty to act], difficulty: medium, cognitive: application

**Grounding:** Chapter 9 - Omissions (Creation of Peril Category)

<!-- argument-pass: SHOULD FIX
(a) Argument-for: A student might argue that modern law reflects a growing moral consensus requiring citizens to assist others in emergencies. Some minority jurisdictions have enacted statutory "duty to rescue" laws that penalize the failure to call 911 when witnessing serious peril. Relying on these statutes, a student could conclude that every citizen now bears a general legal obligation to rescue individuals in imminent danger. Therefore, Marlowe had a duty to act simply by being a citizen aware of the fire.
(b) Argument-for: Under the common law of criminal omissions, a legal duty to act arises when the defendant creates the peril, even if the initial creation was innocent or accidental. Here, Marlowe ordered the chemical processing that ultimately sparked the fire. By initiating the dangerous sequence of events, he became factually responsible for the employee's peril. Consequently, the creation of peril doctrine legally obligated him to call 911 or intervene once the fire broke out.
(c) Argument-for: The common law recognizes specific status relationships, including the master-servant (employer-employee) relationship, as exceptions to the general no-duty-to-act rule. Employers have implied and statutory duties to maintain a safe working environment and to assist injured employees. A student could reasonably argue that Marlowe owed a duty based on this special relationship. By characterizing the employment as a formal contractual relationship regarding safety, this option strongly appeals to the recognized contract and status exceptions for omissions.
(d) Argument-for: Criminal liability generally requires a culpable mental state (mens rea) to accompany the actus reus. A student might argue that if the fire was a purely accidental result of a chemical process, Marlowe lacked the specific intent to create the peril. Without a culpable mental state tied to the fire's ignition, the act of "creating the peril" cannot be criminally attributed to him. Thus, absent specific intent to cause the harm, no criminal duty to rescue arises.
(e) Argument-for: For a duty to arise under the creation of peril doctrine, the defendant must be the direct cause of the danger. A student could argue that Wallace's involuntary convulsion acts as a superseding, intervening cause that breaks the chain of causation between Marlowe's order and the fire. Because the immediate cause was an unforeseeable bodily movement by another person rather than Marlowe's direct action, Marlowe is shielded from liability. Therefore, he did not legally "create" the peril and has no duty to act.

Head-to-head:
Option (b) correctly identifies the "creation of peril" exception, which triggers a duty to act when a defendant's conduct—even if innocent—contributes to a dangerous situation. Option (a) relies on a blatantly false legal premise, as American common law famously rejects a universal duty to rescue. Option (d) incorrectly grafts a specific intent requirement onto the creation of peril doctrine, which applies even to accidental conduct. Option (e) falsely assumes that an intervening involuntary act entirely absolves the initial actor from a duty to mitigate the peril they helped set in motion. Option (c) is the most problematic distractor; while standard employment does not automatically form a rescue contract, the employer-employee dynamic *is* a recognized special relationship that can trigger a duty to act. Because (c) lacks a universally falsifiable lock (e.g., "automatically", "always") and relies on an assumed factual premise, it competes too closely with (b) as a valid alternative theory of liability.

Falsifiable claim per distractor:
- (a): "every citizen has a general legal obligation" — wrong because American criminal law categorically rejects a universal Good Samaritan duty to rescue.
- (c): "a formal contractual relationship existed" — lacks an explicit legal falsehood; it relies on an unstated factual premise and brushes dangerously close to the valid "master-servant" status exception without using a falsifiable absolute word.
- (d): "because he did not possess the specific intent" — wrong because the creation of peril exception triggers a duty regardless of whether the defendant intentionally or accidentally caused the danger.
- (e): "the immediate cause of the fire was Wallace's involuntary convulsion rather than Marlowe's direct actions" — wrong because a defendant need not be the sole immediate cause to have contributed to the peril's creation.

Recommended fix: Edit (c) to include an explicitly false, locked legal proposition. Change to: "(c) Duty, because every standard employment relationship automatically imposes a strict contractual duty to rescue employees from all hazards."
-->
