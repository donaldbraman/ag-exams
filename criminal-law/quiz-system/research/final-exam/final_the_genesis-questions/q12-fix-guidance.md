# Fix Guidance for q12

The QA pipeline flagged this question. Rewrite `q12.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q12.** Avon is charged with possession of the drugs found in the wall safe in his personal office. He argues he has not opened the safe in months. Under the doctrine of constructive possession, will this defense succeed?

(a) Yes, because the government must prove actual, physical handling of the contraband at the exact time of the arrest to establish criminal possession.
(b) Yes, because the lack of temporal proximity to his last use of the safe definitively negates the mental state required for knowing possession.
(c) No, because his exclusive knowledge of the safe's code establishes his power and intention to exercise control over the drugs within the safe. <!-- correct -->
(d) No, because a corporate officer is strictly liable for any contraband found anywhere within the corporate headquarters, regardless of direct access.
(e) No, because constructive possession automatically applies to any individual who holds an ownership stake in the property where the contraband is found.

**Answer:** (c)

**Explanation:** Constructive possession exists when a person lacks physical custody but has the power and intention to exercise dominion and control over an item. Avon's exclusive knowledge of the code to his personal safe clearly establishes his dominion and control over its contents. (a) fails because physical handling is actual possession; the law recognizes constructive possession as a substitute. (b) fails because possession is a continuing offense, and not recently opening the safe does not terminate constructive possession. (d) fails because officers are not strictly liable for all corporate premises; specific control and intent must be established. (e) fails because mere ownership of a building is insufficient; the defendant must have a nexus of control over the specific contraband.

**Tags:** chapters: [15], topics: [constructive possession, dominion and control], difficulty: easy, cognitive: application

**Grounding:** Chapter 15 (cp-exclusive-control)

<!-- audit: MUST FIX
check 1: pass
check 2: pass
check 3: pass
check 4: fails. The correct answer (c) and the explanation rely on a dispositive fact—Avon's "exclusive knowledge of the safe's code"—that is entirely missing from the stem. A well-prepared student will eliminate (c) because they are trained not to assume facts not in evidence (e.g., that it's a combination safe rather than a key safe, or that no one else has the code/access). 
check 5: pass
check 6: pass
check 7: pass
Recommended fix: Add the missing fact to the stem: "...found in the wall safe in his personal office, to which only he knows the combination." Alternatively, generalize (c) to match the stem: "No, because his control over his personal office and the safe within it establishes his power and intention to exercise control over the drugs."
-->

## Issue 2 — argpass-opus

**Q12.** Avon is charged with possession of the drugs found in the wall safe in his personal office. He argues he has not opened the safe in months. Under the doctrine of constructive possession, will this defense succeed?

(a) Yes, because the government must prove actual, physical handling of the contraband at the exact time of the arrest to establish criminal possession.
(b) Yes, because the lack of temporal proximity to his last use of the safe definitively negates the mental state required for knowing possession.
(c) No, because his exclusive knowledge of the safe's code establishes his power and intention to exercise control over the drugs within the safe. <!-- correct -->
(d) No, because a corporate officer is strictly liable for any contraband found anywhere within the corporate headquarters, regardless of direct access.
(e) No, because constructive possession automatically applies to any individual who holds an ownership stake in the property where the contraband is found.

**Answer:** (c)

**Explanation:** Constructive possession exists when a person lacks physical custody but has the power and intention to exercise dominion and control over an item. Avon's exclusive knowledge of the code to his personal safe clearly establishes his dominion and control over its contents. (a) fails because physical handling is actual possession; the law recognizes constructive possession as a substitute. (b) fails because possession is a continuing offense, and not recently opening the safe does not terminate constructive possession. (d) fails because officers are not strictly liable for all corporate premises; specific control and intent must be established. (e) fails because mere ownership of a building is insufficient; the defendant must have a nexus of control over the specific contraband.

**Tags:** chapters: [15], topics: [constructive possession, dominion and control], difficulty: easy, cognitive: application

**Grounding:** Chapter 15 (cp-exclusive-control)

<!-- argument-pass: SHOULD FIX
(a) Argument-for: A student might argue that criminal possession strictly requires a contemporaneous actus reus. Under a hyper-strict evidentiary view, if the defendant is not physically holding the item when apprehended, the government cannot concretely establish the act of possession. Therefore, to ensure no innocent person is convicted, the government must prove actual, physical handling at the exact time of the arrest.
(b) Argument-for: A student could assert that knowing possession is an active state of mind that requires ongoing temporal proximity. Because Avon has not opened the safe in months, this massive gap severs the temporal nexus necessary to prove mens rea. Thus, this lack of recent use definitively negates the knowing mental state required for criminal possession.
(c) Argument-for: A student would argue that constructive possession relies on the power and intention to exercise dominion and control over contraband. Since the safe is in Avon's personal office, it is a direct inference that he controls access to it. His exclusive ability to access the safe establishes his ongoing control over the drugs inside, rendering his lack of recent access irrelevant.
(d) Argument-for: A student might analogize to the responsible corporate officer doctrine, arguing that high-level officers bear strict liability for legal violations within their business purview. Because the safe is located in the corporate headquarters, his status as an officer makes him strictly liable for any contraband found anywhere on the premises.
(e) Argument-for: A student could argue that property law principles of ownership cleanly extend to criminal possession. If an individual holds an ownership stake in the property, the law imputes dominion and control over everything physically located inside it. Therefore, constructive possession automatically applies to him solely because of his ownership interest.

Head-to-head: 
Option (c) correctly articulates the rule for constructive possession—power and intention to exercise control. However, (c) imports a fact ("exclusive knowledge of the safe's code") that is never established in the prompt, which only states it is a safe in "his personal office." While students can reasonably infer he has the code, injecting unstated facts makes the keyed answer slightly flawed. The distractors, however, are securely and explicitly false. Option (a) relies on the falsifiable claim that actual physical handling "at the exact time" is required. Option (b) falsely claims a time gap "definitively negates" the mental state. Option (d) incorrectly applies strict liability to "anywhere within the corporate headquarters." Option (e) uses the absolute phrase "automatically applies." Because the correct answer assumes a fact not in evidence, a minor adjustment is recommended.

Falsifiable claim per distractor:
- (a): "must prove actual, physical handling of the contraband at the exact time of the arrest" — wrong because constructive possession exists precisely as a legal substitute for actual possession, and the actus reus does not require simultaneous physical contact at the moment of arrest.
- (b): "definitively negates the mental state required" — wrong because possession is a continuing offense; a lack of recent physical access does not categorically extinguish a defendant's knowledge of or intent to control the contents.
- (d): "strictly liable for any contraband found anywhere within the corporate headquarters" — wrong because strict liability does not categorically apply to corporate officers for general possession offenses simply because contraband is located somewhere in the building.
- (e): "automatically applies to any individual who holds an ownership stake" — wrong because mere ownership of a property does not automatically or categorically establish the specific nexus, knowledge, and control required for constructive possession.

Recommended fix: Either alter the prompt to include the missing fact ("Avon is charged with possession of the drugs found in the wall safe in his personal office, to which only he has the code.") OR alter (c) to rely entirely on the given text ("No, because his control over the safe in his personal office establishes his power and intention to exercise control over the drugs within it.").
-->
