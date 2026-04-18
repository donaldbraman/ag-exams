# Fix Guidance for q04

The QA pipeline flagged this question. Rewrite `q04.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q4.** George is charged with attempted murder. How would his conduct be analyzed under the common law dangerous proximity test versus the MPC substantial step test?

(a) He is guilty of attempt under both tests. Driving a vehicle with a loaded weapon is universally recognized as the dangerous commencement of any violent criminal offense.
(b) He is not guilty of attempt under either test. Because he had not yet spotted a victim, completing the crime was factually impossible and therefore not punishable.
(c) He is guilty under the proximity test but not the MPC. Being armed satisfies the proximity requirement, but the MPC requires a physical strike to corroborate his criminal intent.
(d) He is guilty under the MPC but likely not under proximity. Searching for a victim is a substantial step, but being three blocks away is not dangerously near completion. <!-- correct -->
(e) He is guilty under proximity but not under the MPC. Three blocks is a short physical distance, but the MPC categorically excludes any acts involving a motor vehicle.

**Answer:** (d)

**Explanation:** Under the MPC substantial step test, searching for a victim while armed strongly corroborates criminal purpose and crosses the attempt threshold. Under the common law dangerous proximity test (*Rizzo*), cruising three blocks away without spotting a victim is merely preparatory and not dangerously near completion. (a) is wrong because driving with a weapon does not satisfy the strict dangerous proximity test. (b) is wrong because failing to find a victim is not factual impossibility; it is an incomplete attempt. (c) is wrong because it inverses the outcomes of the two tests. (e) is wrong because the MPC does not categorically exclude acts involving motor vehicles.

**Tags:** chapters: [17], topics: [attempt actus reus, substantial step, dangerous proximity], difficulty: medium, cognitive: analysis

**Grounding:** Chapter 17 - Actus Reus: Proximity vs. Substantial Step (*People v. Rizzo*, MPC § 5.01)

<!-- audit: MUST FIX
Check 1: pass
Check 2: pass
Check 3: pass
Check 4: The stem completely lacks a fact pattern. It states "George is charged with attempted murder" but does not describe his conduct. The answers and explanation refer to facts (driving a vehicle, having a loaded weapon, searching for a victim, being three blocks away) that are never stated in the question stem.
Check 5: pass
Check 6: pass
Check 7: pass
Check 8: pass
Recommended fix: Add the missing fact pattern to the stem (e.g., "George plans to kill his rival. He loads a weapon, gets into his car, and drives to the rival's neighborhood, actively searching for him. Police stop George three blocks away before he spots his target.").
-->

## Issue 2 — argpass-sonnet

**Q4.** George is charged with attempted murder. How would his conduct be analyzed under the common law dangerous proximity test versus the MPC substantial step test?

(a) He is guilty of attempt under both tests. Driving a vehicle with a loaded weapon is universally recognized as the dangerous commencement of any violent criminal offense.
(b) He is not guilty of attempt under either test. Because he had not yet spotted a victim, completing the crime was factually impossible and therefore not punishable.
(c) He is guilty under the proximity test but not the MPC. Being armed satisfies the proximity requirement, but the MPC requires a physical strike to corroborate his criminal intent.
(d) He is guilty under the MPC but likely not under proximity. Searching for a victim is a substantial step, but being three blocks away is not dangerously near completion. <!-- correct -->
(e) He is guilty under proximity but not under the MPC. Three blocks is a short physical distance, but the MPC categorically excludes any acts involving a motor vehicle.

**Answer:** (d)

**Explanation:** Under the MPC substantial step test, searching for a victim while armed strongly corroborates criminal purpose and crosses the attempt threshold. Under the common law dangerous proximity test (*Rizzo*), cruising three blocks away without spotting a victim is merely preparatory and not dangerously near completion. (a) is wrong because driving with a weapon does not satisfy the strict dangerous proximity test. (b) is wrong because failing to find a victim is not factual impossibility; it is an incomplete attempt. (c) is wrong because it inverses the outcomes of the two tests. (e) is wrong because the MPC does not categorically exclude acts involving motor vehicles.

**Tags:** chapters: [17], topics: [attempt actus reus, substantial step, dangerous proximity], difficulty: medium, cognitive: analysis

**Grounding:** Chapter 17 - Actus Reus: Proximity vs. Substantial Step (*People v. Rizzo*, MPC § 5.01)

<!-- argument-pass: MUST FIX
(a) Argument-for: A student reading the options would infer that George was driving with a loaded weapon to commit murder. The student might argue that arming oneself and mobilizing toward the target shows an irrevocable commitment to the crime. Relying on this, they could mistakenly conclude that both tests treat vehicular mobilization with a deadly weapon as crossing the threshold into attempt, satisfying both the MPC and the common law.
(b) Argument-for: Based on the facts inferred from the option, George had not yet spotted his victim. A student could conceptualize the absence of the victim as an insurmountable factual barrier to committing the murder at that exact moment. Confusing the nuances of factual and legal impossibility, the student might erroneously conclude that since he could not physically kill a victim who wasn't there, the attempt was factually impossible and therefore unpunishable under any test.
(c) Argument-for: A student might argue that being armed in the vicinity of a target creates an immediate, severe risk of harm, thereby satisfying the common law dangerous proximity test. At the same time, they might misunderstand the Model Penal Code's "substantial step" requirement, assuming it is a stricter standard that requires an overt, violent act against the victim's person. Under this flawed assumption, they would conclude George is guilty under proximity but falls short of the MPC's requirements.
(d) Argument-for: Assuming the facts implied by the options, George was driving around searching for a victim but was intercepted three blocks away. Under the MPC, "searching for or following the contemplated victim of the crime" is explicitly defined as a substantial step (§ 5.01(2)(a)). However, under the common law dangerous proximity test—as famously established in *People v. Rizzo*—driving around looking for a victim who has not been located is merely preparatory and not "dangerously close" to success, meaning he is only guilty under the MPC.
(e) Argument-for: A student could argue that being merely three blocks away is geographically close enough to satisfy the spatial requirements of the dangerous proximity test. For the MPC analysis, the student might invent or misremember a rule, incorrectly believing the code contains a specific categorical exclusion for preparatory acts involving motor vehicles (e.g., cruising). Based on this false premise, George's conduct would be actionable under common law but insulated from MPC attempt liability.

Head-to-head: The keyed option (d) correctly states the divergent outcomes of the MPC and common law (*Rizzo*) tests. However, the question stem completely omits the fact pattern—it simply states "George is charged," meaning there is no actual "conduct" described to analyze. A student must guess the operative facts (George is driving, armed, searching for a victim, three blocks away) entirely from the answer choices. This makes the question unanswerable as written, mandating a MUST FIX verdict. That said, the distractors themselves are exceptionally well-crafted, successfully locking in explicitly falsifiable legal claims using absolute language.

Falsifiable claim per distractor:
- (a): "universally recognized as the dangerous commencement" — wrong because common law jurisdictions (like New York in *Rizzo*) frequently hold that driving around looking for a victim is merely preparatory.
- (b): "completing the crime was factually impossible and therefore not punishable" — wrong because factual impossibility is categorically not a defense to attempt under the MPC or modern common law.
- (c): "the MPC requires a physical strike to corroborate his criminal intent" — wrong because the MPC explicitly lists non-striking acts (like searching for a victim or possessing materials) as sufficient substantial steps.
- (e): "the MPC categorically excludes any acts involving a motor vehicle" — wrong because there is no such categorical exclusion in the MPC.

Recommended fix: Insert the missing fact pattern into the question stem. For example: "George decided to murder his rival. He loaded a handgun, got into his car, and drove toward the rival's neighborhood. George was slowly driving around searching for the rival when police pulled him over three blocks away. He had not yet spotted the victim. George is charged with attempted murder. How would his conduct be analyzed..."
-->

## Issue 3 — argpass-opus

**Q4.** George is charged with attempted murder. How would his conduct be analyzed under the common law dangerous proximity test versus the MPC substantial step test?

(a) He is guilty of attempt under both tests. Driving a vehicle with a loaded weapon is universally recognized as the dangerous commencement of any violent criminal offense.
(b) He is not guilty of attempt under either test. Because he had not yet spotted a victim, completing the crime was factually impossible and therefore not punishable.
(c) He is guilty under the proximity test but not the MPC. Being armed satisfies the proximity requirement, but the MPC requires a physical strike to corroborate his criminal intent.
(d) He is guilty under the MPC but likely not under proximity. Searching for a victim is a substantial step, but being three blocks away is not dangerously near completion. <!-- correct -->
(e) He is guilty under proximity but not under the MPC. Three blocks is a short physical distance, but the MPC categorically excludes any acts involving a motor vehicle.

**Answer:** (d)

**Explanation:** Under the MPC substantial step test, searching for a victim while armed strongly corroborates criminal purpose and crosses the attempt threshold. Under the common law dangerous proximity test (*Rizzo*), cruising three blocks away without spotting a victim is merely preparatory and not dangerously near completion. (a) is wrong because driving with a weapon does not satisfy the strict dangerous proximity test. (b) is wrong because failing to find a victim is not factual impossibility; it is an incomplete attempt. (c) is wrong because it inverses the outcomes of the two tests. (e) is wrong because the MPC does not categorically exclude acts involving motor vehicles.

**Tags:** chapters: [17], topics: [attempt actus reus, substantial step, dangerous proximity], difficulty: medium, cognitive: analysis

**Grounding:** Chapter 17 - Actus Reus: Proximity vs. Substantial Step (*People v. Rizzo*, MPC § 5.01)

<!-- argument-pass: MUST FIX
(a) Argument-for: A student might assume that being armed in a vehicle with intent to murder is an inherently dangerous act that triggers attempt liability uniformly across jurisdictions. The argument relies on the premise that the overt act of driving with a loaded weapon crosses the line from mere preparation to perpetration everywhere. This would make it a universal rule of attempt, leading to guilt under both the MPC and common law.
(b) Argument-for: A student could argue that without a victim present, George's actions are legally insufficient for attempt due to impossibility. They might reason that if the victim cannot be found, the crime cannot be committed, rendering it factually impossible. Under rigid, older interpretations, the absence of the target might preclude liability, leading to no guilt under either test.
(c) Argument-for: A student might mistakenly believe the MPC actus reus requirement is narrower than the common law. They could argue that the MPC requires a more concrete act—such as a "physical strike"—to conclusively demonstrate intent, whereas the common law might accept simply being armed in public as creating "dangerous proximity" to a breach of the peace or murder.
(d) Argument-for: Under the MPC (§ 5.01), searching for a victim while armed is specifically listed as a "substantial step" that strongly corroborates criminal purpose, making George guilty. However, under the common law dangerous proximity test (as famously established in *People v. Rizzo*), driving around searching for a victim without actually spotting them is mere preparation, not an act dangerously near to success. Thus, George is guilty under the MPC but not under proximity.
(e) Argument-for: A student could argue that "three blocks" is objectively a short distance, thus satisfying the spatial requirement of the dangerous proximity test. To justify the MPC outcome, they might rely on a fabricated exception, believing the MPC expressly excludes driving from the definition of a substantial step to avoid over-criminalizing everyday behavior.

Head-to-head: Option (d) correctly maps the specific facts to the divergent outcomes of the MPC and common law proximity tests (*Rizzo*). All four distractors feature clearly falsifiable legal errors, effectively utilizing absolute language ("universally recognized," "requires a physical strike," "categorically excludes") to ensure they are demonstrably false. However, the question stem completely omits the actual fact pattern detailing George's conduct. Without facts in the prompt, the student must reverse-engineer the scenario from the options, which is a critical structural flaw that requires a MUST FIX verdict.

Falsifiable claim per distractor:
- (a): "universally recognized as the dangerous commencement of any violent criminal offense" — wrong because common law (e.g., *Rizzo*) explicitly classifies this conduct as mere preparation, not commencement.
- (b): "factually impossible and therefore not punishable" — wrong because factual impossibility is well-established as *not* being a valid defense to attempt in either jurisdiction.
- (c): "the MPC requires a physical strike to corroborate his criminal intent" — wrong because MPC § 5.01 explicitly lists non-striking acts (like searching or lying in wait) as sufficient.
- (e): "the MPC categorically excludes any acts involving a motor vehicle" — wrong because there is no such exclusion anywhere in the Model Penal Code.

Recommended fix: Add the missing fact pattern to the question stem. For example: "George, armed with a loaded weapon, drives around his neighborhood searching for his enemy to kill him. He is three blocks away from the enemy's expected location but has not yet spotted his intended victim."
-->
