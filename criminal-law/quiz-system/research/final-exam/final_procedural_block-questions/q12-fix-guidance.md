# Fix Guidance for q12

The QA pipeline flagged this question. Rewrite `q12.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — grounding

**Q12.** Evaluating Kevin's actions regarding Marco, is Kevin guilty of attempted murder under the Model Penal Code's "substantial step" framework?

(a) Kevin is guilty of attempted murder because hiring the hitman, providing the address, and the hitman's drive to the neighborhood collectively constitute a substantial step strongly corroborating the criminal purpose. <!-- correct -->
(b) Kevin is guilty of attempted murder because the explicit exchange of monetary funds automatically transforms any preliminary criminal discussion into a fully completed attempt under the Model Penal Code.
(c) Kevin is not guilty of attempted murder because the hitman's arrest for an entirely unrelated traffic warrant legally serves as a valid voluntary abandonment of the attempted assassination.
(d) Kevin is not guilty of attempted murder because a criminal attempt cannot be legally charged unless the immediate perpetrator comes within physical striking distance of the intended victim.
(e) Kevin is not guilty of attempted murder because he was not physically present in the vehicle with the hitman when the alleged substantial step toward completion was actually taken.

**Answer:** (a)

**Explanation:** Under the Model Penal Code, attempt liability requires a substantial step that strongly corroborates the actor's criminal purpose. Kevin paying the hitman, providing the address, and the hitman's drive to the target's neighborhood collectively satisfy this requirement, making (a) correct. (b) is incorrect because merely exchanging funds is an act of preparation or solicitation that does not automatically constitute a fully completed attempt without further action. (c) is incorrect because an arrest by law enforcement is an involuntary interruption, which legally defeats any claim of voluntary abandonment. (d) is incorrect because the MPC substantial step test explicitly discarded the restrictive requirement that a perpetrator must reach physical striking distance. (e) is incorrect because a solicitor can be held liable for an attempt even if they are not physically present when the agent takes the substantial step.

**Tags:** chapters: [12], topics: [attempt, substantial step, MPC], difficulty: medium, cognitive: application

**Grounding:** Under Model Penal Code § 5.01, a substantial step toward the commission of a crime, such as hiring an agent who then drives to the target location, strongly corroborates the actor's criminal purpose and supports attempt liability.

<!-- GROUNDING-FAIL: MPC "substantial step" framework is not in any chapter map. The closest taught doctrines are: None (meta-map artifact is missing). Correct answer must rely on one of those instead. -->

## Issue 2 — audit

**Q12.** Evaluating Kevin's actions regarding Marco, is Kevin guilty of attempted murder under the Model Penal Code's "substantial step" framework?

(a) Kevin is guilty of attempted murder because hiring the hitman, providing the address, and the hitman's drive to the neighborhood collectively constitute a substantial step strongly corroborating the criminal purpose. <!-- correct -->
(b) Kevin is guilty of attempted murder because the explicit exchange of monetary funds automatically transforms any preliminary criminal discussion into a fully completed attempt under the Model Penal Code.
(c) Kevin is not guilty of attempted murder because the hitman's arrest for an entirely unrelated traffic warrant legally serves as a valid voluntary abandonment of the attempted assassination.
(d) Kevin is not guilty of attempted murder because a criminal attempt cannot be legally charged unless the immediate perpetrator comes within physical striking distance of the intended victim.
(e) Kevin is not guilty of attempted murder because he was not physically present in the vehicle with the hitman when the alleged substantial step toward completion was actually taken.

**Answer:** (a)

**Explanation:** Under the Model Penal Code, attempt liability requires a substantial step that strongly corroborates the actor's criminal purpose. Kevin paying the hitman, providing the address, and the hitman's drive to the target's neighborhood collectively satisfy this requirement, making (a) correct. (b) is incorrect because merely exchanging funds is an act of preparation or solicitation that does not automatically constitute a fully completed attempt without further action. (c) is incorrect because an arrest by law enforcement is an involuntary interruption, which legally defeats any claim of voluntary abandonment. (d) is incorrect because the MPC substantial step test explicitly discarded the restrictive requirement that a perpetrator must reach physical striking distance. (e) is incorrect because a solicitor can be held liable for an attempt even if they are not physically present when the agent takes the substantial step.

**Tags:** chapters: [12], topics: [attempt, substantial step, MPC], difficulty: medium, cognitive: application

**Grounding:** Under Model Penal Code § 5.01, a substantial step toward the commission of a crime, such as hiring an agent who then drives to the target location, strongly corroborates the actor's criminal purpose and supports attempt liability.

<!-- audit: MUST FIX
Check 1: pass
Check 2: pass
Check 3: The explanation loosely and inaccurately states that Kevin's and the hitman's actions "collectively" constitute a substantial step. Under the MPC, attempt evaluates the actor's conduct individually. Kevin would be guilty either as an accomplice to the hitman's attempt (where the *hitman's* drive is the substantial step) or under MPC § 5.01(3) for conduct designed to aid. Merging multiple individuals' actions into a single "collective" substantial step is doctrinally imprecise.
Check 4: The question stem completely lacks a fact pattern. It references "Kevin's actions regarding Marco" but fails to provide any operative facts, forcing students to reverse-engineer the events (hiring the hitman, the drive, the traffic warrant arrest) entirely from the answer options and explanation.
Check 5: pass
Check 6: pass
Check 7: pass
Check 8: pass
Recommended fix: Add a brief factual scenario to the stem describing Kevin's solicitation, payment, and the hitman's subsequent drive and arrest. Revise option (a) and the explanation to clarify that Kevin is liable as an accomplice to the hitman's attempt (or via MPC § 5.01(3)), rather than relying on a "collective" substantial step.
-->
