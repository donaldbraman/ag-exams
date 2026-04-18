# Fix Guidance for q07

The QA pipeline flagged this question. Rewrite `q07.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q7.** Assume Marcus asserts a duress defense to the distribution charge, citing Leo's threat to "put a bullet in your head" tomorrow. Will this defense succeed?

(a) Yes, because a threat of death or serious bodily injury from a known syndicate enforcer creates a reasonable fear of harm that excuses the criminal conduct.
(b) Yes, because the severe threat overbore his free will and he lacked any realistic safe avenue to report the syndicate to municipal law enforcement.
(c) No, because duress is never a legally valid defense to narcotics distribution offenses, as they are designated as inherently dangerous to the general public.
(d) No, because Leo's threat to track down and harm Marcus the following day fails to satisfy the doctrinal requirement of a present and imminent threat. <!-- correct -->
(e) No, because Marcus voluntarily joined the criminal syndicate, which means he entirely forfeits his right to raise a duress defense for any future violent threats.

**Answer:** (d)

**Explanation:** The correct answer is (d). At common law, duress requires a present, imminent, and impending threat of death or serious bodily injury. A threat of future harm—even a severe threat like "tomorrow"—fails the imminence requirement because it theoretically leaves the defendant time to escape or seek help from law enforcement (Fact 6).

(a) is incorrect because while the threat is severe, it lacks the strictly required temporal element of imminence.
(b) is incorrect because the law objectively presumes that a non-imminent threat provides an avenue for escape or police intervention, regardless of the defendant's subjective belief about safety.
(c) is incorrect because duress is generally available for all crimes except intentional murder; it is not categorically barred for drug distribution.
(e) is incorrect because while voluntarily joining a criminal enterprise can defeat a duress claim, the failure of the imminence element is the primary and direct doctrinal bar to the defense here.

**Tags:** chapters: [21], topics: [duress, duress-imminence-proximity], difficulty: easy, cognitive: application

**Grounding:** Chapter 21 - Necessity and Duress > Duress imminence/proximity

<!-- audit: MUST FIX
check 1: fail - The correct answer hinges entirely on strict imminence, which is a Common Law requirement. The MPC (§ 2.09) replaces strict imminence with a "reasonable firmness" standard. Because the stem does not stipulate jurisdiction, (d) is not universally correct.
check 2: fail - A prepared student could strongly argue for (b) under the MPC. If there is no "realistic safe avenue" (linking to the `duress-corrupt-authorities` tag), a person of reasonable firmness might be unable to resist a threat for "tomorrow," thus making the defense potentially viable under the MPC.
check 3: pass - The explanation correctly states the Common Law rule, but inadvertently highlights that the stem forgot to establish the jurisdiction.
check 4: pass - Assuming the facts about Leo and the syndicate are provided in the shared scenario.
check 5: fail - Duress is a classic jurisdictional split (Common Law vs. MPC). The stem fails to resolve this split cleanly. 
check 6: pass - No excluded topic bleed.
check 7: pass - Duress imminence is squarely in the Chapter 21 map.
Recommended fix: Add "under common law" to the question stem. E.g., "Assume Marcus asserts a common law duress defense to the distribution charge..."
-->

## Issue 2 — argpass-sonnet

**Q7.** Assume Marcus asserts a duress defense to the distribution charge, citing Leo's threat to "put a bullet in your head" tomorrow. Will this defense succeed?

(a) Yes, because a threat of death or serious bodily injury from a known syndicate enforcer creates a reasonable fear of harm that excuses the criminal conduct.
(b) Yes, because the severe threat overbore his free will and he lacked any realistic safe avenue to report the syndicate to municipal law enforcement.
(c) No, because duress is never a legally valid defense to narcotics distribution offenses, as they are designated as inherently dangerous to the general public.
(d) No, because Leo's threat to track down and harm Marcus the following day fails to satisfy the doctrinal requirement of a present and imminent threat. <!-- correct -->
(e) No, because Marcus voluntarily joined the criminal syndicate, which means he entirely forfeits his right to raise a duress defense for any future violent threats.

**Answer:** (d)

**Explanation:** The correct answer is (d). At common law, duress requires a present, imminent, and impending threat of death or serious bodily injury. A threat of future harm—even a severe threat like "tomorrow"—fails the imminence requirement because it theoretically leaves the defendant time to escape or seek help from law enforcement (Fact 6).

(a) is incorrect because while the threat is severe, it lacks the strictly required temporal element of imminence.
(b) is incorrect because the law objectively presumes that a non-imminent threat provides an avenue for escape or police intervention, regardless of the defendant's subjective belief about safety.
(c) is incorrect because duress is generally available for all crimes except intentional murder; it is not categorically barred for drug distribution.
(e) is incorrect because while voluntarily joining a criminal enterprise can defeat a duress claim, the failure of the imminence element is the primary and direct doctrinal bar to the defense here.

**Tags:** chapters: [21], topics: [duress, duress-imminence-proximity], difficulty: easy, cognitive: application

**Grounding:** Chapter 21 - Necessity and Duress > Duress imminence/proximity

<!-- argument-pass: SHOULD FIX
(a) Argument-for: A student could argue that when dealing with a known and ruthless syndicate enforcer, a threat of death tomorrow is highly credible and inescapable. The student might conclude that this creates a reasonable fear of severe harm, which satisfies the subjective and objective components of duress, thus excusing the criminal act even if not immediately imminent.
(b) Argument-for: A student could argue under the Model Penal Code approach, which does not strictly demand imminence but rather asks if a person of reasonable firmness would be unable to resist. If Marcus genuinely had no realistic safe avenue to report to the police, his free will was overborne, potentially excusing his conduct despite the threat being for "tomorrow."
(c) Argument-for: A student might mistakenly believe that duress is categorically unavailable for all inherently dangerous felonies. Knowing that duress is never a defense to intentional murder, the student might assume this strict exclusion extends to narcotics distribution offenses because of their danger to the general public.
(d) Argument-for: A student would argue that the common-law standard for duress requires a threat of death or serious bodily harm to be present, imminent, and impending. Because Leo's threat explicitly concerns future harm ("tomorrow"), it theoretically leaves Marcus time to escape or seek help, meaning the defense categorically fails on the imminence element.
(e) Argument-for: A student could argue that the defense of duress is unavailable if the defendant recklessly or voluntarily placed himself in a situation where coercion was probable. Because Marcus voluntarily joined a criminal syndicate, he assumed the risk of such threats and therefore forfeits the right to raise a duress defense.

Head-to-head: Option (d) is the keyed correct answer, correctly stating that a future threat ("tomorrow") fails the common-law imminence requirement. Option (e) is a strong distractor because the voluntary joining of a syndicate does generally defeat a duress claim, but it safely fails here due to the overbroad, falsifiable phrase "entirely forfeits... for any future violent threats" (which wrongly includes unrelated threats). However, distractors (a) and (b) lack explicit, identifiable false legal propositions locked with absolute words; they merely apply facts to the wrong legal standard (or the MPC standard) without making a categorically false legal claim. Because (b) could be defensible under the MPC if Marcus lacked an escape route, and lacks a strictly falsifiable falsehood, this question needs to lock its distractors.

Falsifiable claim per distractor:
- (a): "creates a reasonable fear of harm that excuses the criminal conduct" — wrong because under common law, reasonable fear does not excuse conduct without imminence; however, it lacks absolute locking language.
- (b): "overbore his free will and he lacked any realistic safe avenue" — lacks an explicit falsifiable legal claim; it merely asserts factual conclusions that might support an MPC duress claim without absolute locking words.
- (c): "never a legally valid defense to narcotics distribution offenses" — wrong because the categorical exclusion of duress applies only to intentional murder, not narcotics distribution.
- (e): "entirely forfeits his right to raise a duress defense for any future violent threats" — wrong because voluntary involvement only forfeits the defense for threats arising from that involvement, not "any" future threat.

Recommended fix: Add absolute locking words to (a) and (b) to create explicit false legal claims. For example, edit (b) to: "Yes, because the subjective lack of a realistic safe avenue to report the syndicate categorically overrides the requirement of an imminent threat." Modify (a) to: "Yes, because any credible threat of death from a known syndicate enforcer automatically excuses criminal conduct."
-->
