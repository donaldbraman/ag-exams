# Fix Guidance for q06

The QA pipeline flagged this question. Rewrite `q06.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

<!-- audit: MUST FIX -->

**Safety Block Triggered.** The previous version of this question was blocked by Gemini's safety filters as unsafe. Please rewrite the fact pattern to reduce the risk of unsafe content blocking.

Error: Model returned empty or blocked response.

## Issue 2 — argpass-sonnet

**Q6.** The prosecution charges Marlowe with attempted distribution of a controlled substance based on him driving toward the meeting point before being stopped for a broken taillight. Under the Model Penal Code's "substantial step" test and the common law's "dangerous proximity" test, how will courts likely rule?

(a) Guilty under both tests, because driving toward the meeting point unambiguously corroborates his intent and places him in immediate physical proximity to the buyer.
(b) Not guilty under both tests, because an ordinary traffic stop for an unrelated violation operates as a legally cognizable abandonment of the attempted offense.
(c) Guilty under the substantial step test because driving strongly corroborates his purpose, but not guilty under the dangerous proximity test because he was two miles away. <!-- correct -->
(d) Not guilty under the substantial step test because he had not arrived at the location, but guilty under dangerous proximity because he possessed the drugs.
(e) Guilty under the substantial step test because attempt is complete upon forming the agreement, but not guilty under the common law dangerous proximity test.

**Answer:** (c)

**Explanation:** The MPC's "substantial step" test focuses on what the defendant has already done, finding an attempt if the act strongly corroborates criminal purpose (like driving to a drug meeting). The common law "dangerous proximity" test focuses on what remains to be done, requiring the defendant to be on the brink of success, which a two-mile distance likely defeats. (a) fails because two miles away is generally not close enough to satisfy the dangerous proximity test. (b) fails because an abandonment defense requires voluntary renunciation, not interruption by police intervention. (d) fails because it reverses the stringency of the tests; substantial step is easier to satisfy than dangerous proximity. (e) fails because attempt requires an act beyond mere preparation, whereas forming an agreement is the actus reus of conspiracy.

**Tags:** chapters: [17], topics: [attempt, substantial step, dangerous proximity], difficulty: medium, cognitive: analysis

**Grounding:** Chapter 17 (actus-reus-substantial-step; actus-reus-proximity-test)

<!-- argument-pass: MUST FIX
(a) Argument-for: A student could argue that based solely on the facts in the stem, "driving toward the meeting point" means Marlowe could be moments away from arriving. Without a specified distance, driving to the site with the drugs can satisfy the common law's dangerous proximity test because the remaining acts are de minimis. The MPC's substantial step test is also easily satisfied by driving to the scene, making him guilty under both tests.
(b) Argument-for: A student could defend this by arguing that because the police stopped Marlowe for an unrelated traffic offense (a broken taillight), his specific criminal attempt was thwarted by an extrinsic, unrelated factor. They might mistakenly categorize this circumstantial interruption as a "legally cognizable abandonment" since the drug transaction was never actually detected or initiated on scene.
(c) Argument-for: Under MPC § 5.01, driving to the scene of a contemplated crime strongly corroborates criminal purpose, readily satisfying the substantial step test. However, the common law dangerous proximity doctrine requires the defendant to be on the brink of success. Being two miles away clearly defeats dangerous proximity, neatly capturing the classic divergence between these two attempt doctrines.
(d) Argument-for: A student could argue that possession of the drugs creates the core "danger" required for the dangerous proximity test, satisfying the common law requirement. Concurrently, they might mistakenly believe the MPC's substantial step test strictly requires actual arrival at the location to establish the "step," resulting in a guilty verdict under common law but an acquittal under the MPC.
(e) Argument-for: A student could argue that attempt requires a culpable mind and an overt act, and that agreeing to the deal satisfies both under the MPC's broader standard. By conflating the completion of conspiracy (the agreement) with the substantial step for attempt, a student could conclude he is guilty under the MPC but falls short of the strict common law proximity standard.

Head-to-head: The question stem contains a fatal omission: it never states how far Marlowe was from the meeting point. Option (c) introduces the dispositive fact ("because he was two miles away") out of nowhere. Because the stem omits this fact, a student could plausibly assume Marlowe was pulled over 50 feet from the meeting point, which would make option (a) factually and legally defensible. Options (b), (d), and (e) rely on explicitly false legal rules, but (a) is nearly as strong as the keyed answer because the only thing defeating it is a fact missing from the prompt. 

Falsifiable claim per distractor:
- (a): "unambiguously corroborates his intent and places him in immediate physical proximity" — wrong because driving toward a location does not categorically establish immediate physical proximity (but this relies on assuming he is far away, which the stem forgets to state).
- (b): "operates as a legally cognizable abandonment" — wrong because abandonment/renunciation categorically requires voluntary abandonment, not an involuntary interruption by police.
- (d): "guilty under dangerous proximity because he possessed the drugs" — wrong because dangerous proximity strictly requires physical closeness to the completion of the actus reus, not merely possessing the instrumentality of the crime.
- (e): "attempt is complete upon forming the agreement" — wrong because forming an agreement is categorically the actus reus for conspiracy; attempt requires a substantial step/overt act beyond mere agreement.

Recommended fix: Add the missing distance fact to the question stem. Edit the first sentence: "...based on him driving toward the meeting point before being stopped for a broken taillight two miles away from the destination."
-->

## Issue 3 — argpass-opus

**Q6.** The prosecution charges Marlowe with attempted distribution of a controlled substance based on him driving toward the meeting point before being stopped for a broken taillight. Under the Model Penal Code's "substantial step" test and the common law's "dangerous proximity" test, how will courts likely rule?

(a) Guilty under both tests, because driving toward the meeting point unambiguously corroborates his intent and places him in immediate physical proximity to the buyer.
(b) Not guilty under both tests, because an ordinary traffic stop for an unrelated violation operates as a legally cognizable abandonment of the attempted offense.
(c) Guilty under the substantial step test because driving strongly corroborates his purpose, but not guilty under the dangerous proximity test because he was two miles away. <!-- correct -->
(d) Not guilty under the substantial step test because he had not arrived at the location, but guilty under dangerous proximity because he possessed the drugs.
(e) Guilty under the substantial step test because attempt is complete upon forming the agreement, but not guilty under the common law dangerous proximity test.

**Answer:** (c)

**Explanation:** The MPC's "substantial step" test focuses on what the defendant has already done, finding an attempt if the act strongly corroborates criminal purpose (like driving to a drug meeting). The common law "dangerous proximity" test focuses on what remains to be done, requiring the defendant to be on the brink of success, which a two-mile distance likely defeats. (a) fails because two miles away is generally not close enough to satisfy the dangerous proximity test. (b) fails because an abandonment defense requires voluntary renunciation, not interruption by police intervention. (d) fails because it reverses the stringency of the tests; substantial step is easier to satisfy than dangerous proximity. (e) fails because attempt requires an act beyond mere preparation, whereas forming an agreement is the actus reus of conspiracy.

**Tags:** chapters: [17], topics: [attempt, substantial step, dangerous proximity], difficulty: medium, cognitive: analysis

**Grounding:** Chapter 17 (actus-reus-substantial-step; actus-reus-proximity-test)

<!-- argument-pass: MUST FIX
(a) Argument-for: A student could argue that driving to a drug deal constitutes enough of an act to satisfy both tests. Since the prompt states Marlowe was "driving toward the meeting point" without specifying distance, it is factually possible he was intercepted just down the block. Without a specified distance in the prompt, a student could assume he was close enough to be in immediate physical proximity, making him guilty under dangerous proximity as well.
(b) Argument-for: A student could argue that an ordinary traffic stop for a broken taillight resets the scenario, as it is unrelated to the substantive drug offense. They might falsely infer that because the interruption was not initiated due to the drugs, it functions as a legally cognizable abandonment of the attempt. This relies on the idea that without targeted intervention, the specific attempt timeline was legally aborted.
(c) Argument-for: A student could argue that driving towards the meeting point strongly corroborates the criminal purpose, fulfilling the MPC's substantial step test. They would further argue that he fails the dangerous proximity test because he was still two miles away from the target, putting him too far from completion. Even though the "two miles" fact isn't in the prompt, this option introduces the missing fact that aligns perfectly with the standard legal distinction between the two tests.
(d) Argument-for: A student could argue that the MPC substantial step test categorically requires actual arrival at the target location to be "strongly corroborative." Conversely, they might argue that the dangerous proximity test is strictly focused on the dangerousness of the actor's present capabilities; thus, possessing the drugs makes the situation sufficiently dangerous to satisfy the common law test regardless of physical distance.
(e) Argument-for: A student could argue that forming the agreement is the core criminal act for both attempt and conspiracy. They might mistakenly assume that under the more modern MPC, the mere formation of the agreement serves as the "substantial step" that strongly corroborates the criminal purpose. Thus, he is guilty under the MPC but not under the stricter common law test.

Head-to-head: 
The fatal flaw in this question is that the correct answer (c) and the explanation hinge on a factual premise ("he was two miles away") that is entirely absent from the prompt. Because the distance is omitted, option (a) becomes a highly viable answer; if Marlowe was only a block away, he might satisfy the dangerous proximity test. Distractors (b), (d), and (e) all contain explicit, legally false claims (conflating abandonment with involuntary police stops, misstating the proximity test's focus on possession, and conflating attempt actus reus with conspiracy). However, because the prompt lacks the factual grounding to definitively rule out (a), the question is currently unanswerable without making outside assumptions and requires revision.

Falsifiable claim per distractor:
- (a): "places him in immediate physical proximity" — logically unfalsifiable as written since the prompt omits the distance, making this a fatal distractor.
- (b): "operates as a legally cognizable abandonment" — wrong because abandonment requires voluntary renunciation, not an involuntary traffic stop.
- (d): "guilty under dangerous proximity because he possessed the drugs" — wrong because dangerous proximity requires physical closeness to completion, not merely possessing contraband.
- (e): "attempt is complete upon forming the agreement" — wrong because forming an agreement is the actus reus for conspiracy; attempt requires a substantial step beyond preparation.

Recommended fix: Add the missing "two miles away" fact to the prompt: "...based on him driving toward the meeting point before being stopped for a broken taillight two miles away from the location." To fully lock out the distractors per the close-call standard, add absolute wording to the false claims (e.g., in (b), "categorically operates as a legally cognizable abandonment"; in (d), "guilty solely because he possessed the drugs").
-->
