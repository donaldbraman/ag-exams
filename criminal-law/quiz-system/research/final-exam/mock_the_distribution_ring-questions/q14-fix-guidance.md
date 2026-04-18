# Fix Guidance for q14

The QA pipeline flagged this question. Rewrite `q14.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q14.** Assume the jurisdiction follows the Model Penal Code's approach to conspiracy liability. Is Artie liable for Vic's murder solely based on his role as the conspiracy's ringleader?

(a) No, because the MPC rejects the *Pinkerton* doctrine and requires the prosecution to prove Artie met the traditional elements of accomplice liability for the specific murder. <!-- correct -->
(b) Yes, because the MPC universally adopted the *Pinkerton* doctrine to ensure organized crime leaders are held accountable for the foreseeable violent actions of their subordinates.
(c) No, because under the MPC, ringleaders are immune from homicide charges unless they personally ordered the execution or provided the murder weapon prior to the event.
(d) Yes, because Artie's post-crime wire transfer of $1,000 constitutes an attempt to aid the substantive offense, which satisfies the MPC's relaxed actus reus standard.
(e) No, because the MPC dictates that all substantive offenses merge into the conspiracy charge, meaning Artie can only be convicted of conspiracy to commit robbery.

**Answer:** (a)

**Explanation:** (a) is correct because the MPC explicitly rejected *Pinkerton* vicarious liability; mere membership in a conspiracy is insufficient, and a defendant must actually aid, abet, or encourage the specific offense with purpose to be liable for it. (b) is wrong because it states the exact opposite of the MPC's position. (c) is wrong because immunity is not the standard; Artie could be liable if he purposefully aided the murder, which does not strictly require ordering it or providing the gun. (d) is wrong because accessory after the fact assistance (the post-crime wire transfer) does not establish accomplice liability for the already-completed murder. (e) is wrong because under the MPC, conspiracy to commit an offense does not merge with the completed offense; both can be charged, but *Pinkerton* vicarious liability is rejected.

**Tags:** chapters: [19], topics: [conspiracy, mpc-pinkerton-rejection], difficulty: medium, cognitive: analysis

**Grounding:** Chapter 19, pinkerton-mpc-rejection

<!-- audit: MUST FIX
check 1: pass
check 2: pass
check 3: pass
check 4: MUST FIX (The stem completely lacks a fact pattern. It references "Artie," "Vic's murder," a "post-crime wire transfer," and a "conspiracy to commit robbery" without ever introducing these facts. Students cannot properly evaluate the options without the scenario.)
check 5: pass
check 6: pass
check 7: pass
check 8: pass
Recommended fix: Add the missing factual scenario to the stem, detailing Artie's role in the robbery conspiracy, Vic's murder, and the post-crime wire transfer.
-->

## Issue 2 — edge-case

**Q14.** Assume the jurisdiction follows the Model Penal Code's approach to conspiracy liability. Is Artie liable for Vic's murder solely based on his role as the conspiracy's ringleader?

(a) No, because the MPC rejects the *Pinkerton* doctrine and requires the prosecution to prove Artie met the traditional elements of accomplice liability for the specific murder. <!-- correct -->
(b) Yes, because the MPC universally adopted the *Pinkerton* doctrine to ensure organized crime leaders are held accountable for the foreseeable violent actions of their subordinates.
(c) No, because under the MPC, ringleaders are immune from homicide charges unless they personally ordered the execution or provided the murder weapon prior to the event.
(d) Yes, because Artie's post-crime wire transfer of $1,000 constitutes an attempt to aid the substantive offense, which satisfies the MPC's relaxed actus reus standard.
(e) No, because the MPC dictates that all substantive offenses merge into the conspiracy charge, meaning Artie can only be convicted of conspiracy to commit robbery.

**Answer:** (a)

**Explanation:** (a) is correct because the MPC explicitly rejected *Pinkerton* vicarious liability; mere membership in a conspiracy is insufficient, and a defendant must actually aid, abet, or encourage the specific offense with purpose to be liable for it. (b) is wrong because it states the exact opposite of the MPC's position. (c) is wrong because immunity is not the standard; Artie could be liable if he purposefully aided the murder, which does not strictly require ordering it or providing the gun. (d) is wrong because accessory after the fact assistance (the post-crime wire transfer) does not establish accomplice liability for the already-completed murder. (e) is wrong because under the MPC, conspiracy to commit an offense does not merge with the completed offense; both can be charged, but *Pinkerton* vicarious liability is rejected.

**Tags:** chapters: [19], topics: [conspiracy, mpc-pinkerton-rejection], difficulty: medium, cognitive: analysis

**Grounding:** Chapter 19, pinkerton-mpc-rejection

<!-- edge-case-audit: SHOULD FIX
1. Fact Pattern Booby Traps: pass
2. Cross-Doctrine Clashes: The explanation for choice (e) misstates the MPC rule for conspiracy merger. The explanation claims "under the MPC, conspiracy to commit an offense does not merge with the completed offense." This describes the common law rule. The MPC (§ 1.07(1)(b)) actually *does* merge conspiracy into the completed offense (unless the conspiracy contemplates additional offenses). 
3. Cross-Question Spoilers: pass
Recommended fix: Update the explanation for (e) to correctly state why it is wrong. For example: "(e) is wrong because it reverses the merger rule. Under the MPC, a conspiracy merges into the completed substantive offense, not the other way around, and Artie's liability for murder under the MPC depends on accomplice principles, not merger."
-->

## Issue 3 — argpass-sonnet

**Q14.** Assume the jurisdiction follows the Model Penal Code's approach to conspiracy liability. Is Artie liable for Vic's murder solely based on his role as the conspiracy's ringleader?

(a) No, because the MPC rejects the *Pinkerton* doctrine and requires the prosecution to prove Artie met the traditional elements of accomplice liability for the specific murder. <!-- correct -->
(b) Yes, because the MPC universally adopted the *Pinkerton* doctrine to ensure organized crime leaders are held accountable for the foreseeable violent actions of their subordinates.
(c) No, because under the MPC, ringleaders are immune from homicide charges unless they personally ordered the execution or provided the murder weapon prior to the event.
(d) Yes, because Artie's post-crime wire transfer of $1,000 constitutes an attempt to aid the substantive offense, which satisfies the MPC's relaxed actus reus standard.
(e) No, because the MPC dictates that all substantive offenses merge into the conspiracy charge, meaning Artie can only be convicted of conspiracy to commit robbery.

**Answer:** (a)

**Explanation:** (a) is correct because the MPC explicitly rejected *Pinkerton* vicarious liability; mere membership in a conspiracy is insufficient, and a defendant must actually aid, abet, or encourage the specific offense with purpose to be liable for it. (b) is wrong because it states the exact opposite of the MPC's position. (c) is wrong because immunity is not the standard; Artie could be liable if he purposefully aided the murder, which does not strictly require ordering it or providing the gun. (d) is wrong because accessory after the fact assistance (the post-crime wire transfer) does not establish accomplice liability for the already-completed murder. (e) is wrong because under the MPC, conspiracy to commit an offense does not merge with the completed offense; both can be charged, but *Pinkerton* vicarious liability is rejected.

**Tags:** chapters: [19], topics: [conspiracy, mpc-pinkerton-rejection], difficulty: medium, cognitive: analysis

**Grounding:** Chapter 19, pinkerton-mpc-rejection

<!-- argument-pass: MUST FIX
(a) Argument-for: Under the MPC, conspiracy alone does not establish vicarious liability for the substantive offenses of co-conspirators. The MPC explicitly rejects the *Pinkerton* doctrine. Therefore, to hold Artie liable for Vic's murder, the prosecution must prove he possessed the requisite mens rea and actus reus for accomplice liability regarding that specific murder.
(b) Argument-for: A student could argue that the Model Penal Code was drafted to address modern organized criminal enterprises and thus embraced the *Pinkerton* doctrine. Under this view, making ringleaders strictly liable for the foreseeable violent actions of their subordinates is a logical way to ensure accountability, meaning Artie is automatically liable because the murder was a foreseeable outcome of the conspiracy.
(c) Argument-for: A student might choose this option because it correctly identifies the outcome ("No") and attempts to apply a strict actus reus standard for accomplice liability. One could argue that to hold a non-present ringleader liable for homicide under the MPC, there must be concrete proof of purposeful facilitation, which categorically limits liability to explicit orders or providing the instrumentality of the crime.
(d) Argument-for: Assuming the unstated facts involve a wire transfer, a student might argue that the MPC's inclusion of "attempts to aid" in its accomplice liability statute broadens the actus reus significantly. They could contend that sending funds post-crime reflects a prior agreement or an ongoing attempt to assist the substantive offense, thereby satisfying the MPC's standard for accomplice liability.
(e) Argument-for: The student might recall that the MPC changed the common law rule on merger. Under MPC § 1.07(1)(b), a defendant generally cannot be convicted of both a conspiracy to commit an offense and the completed offense itself. They could misinterpret this to mean that the substantive offense universally merges into the conspiracy charge, leaving Artie liable only for the underlying conspiracy to commit robbery.

Head-to-head: Option (a) correctly states the law, as the MPC explicitly rejects *Pinkerton* and requires traditional accomplice liability for substantive crimes. Option (b) is factually backwards about the MPC. Option (c) relies on a falsely rigid actus reus rule ("immune... unless"), as accomplice liability can be established through any purposeful aid or encouragement. Option (d) incorrectly characterizes post-crime assistance as satisfying the actus reus for the completed substantive offense. Option (e) falsely claims that "all substantive offenses merge into the conspiracy charge," which incorrectly reverses the direction of merger. However, the fundamental flaw in this question is that the stem is completely missing the underlying fact pattern. Options (d) and (e) reference highly specific facts (a post-crime $1,000 wire transfer and a robbery) that do not exist in the prompt, making the question unanswerable as a coherent hypothetical. 

Falsifiable claim per distractor:
- (b): "the MPC universally adopted the Pinkerton doctrine" — wrong because the MPC explicitly rejects *Pinkerton* vicarious liability.
- (c): "ringleaders are immune from homicide charges unless they personally ordered the execution or provided the murder weapon" — wrong because accomplice liability can attach through any form of purposeful aid, agreement to aid, or encouragement, not just those two exclusive acts.
- (d): "post-crime wire transfer of $1,000 constitutes an attempt to aid the substantive offense" — wrong because unilateral post-crime assistance constitutes hindering prosecution/accessory after the fact, not accomplice liability for an already-completed murder.
- (e): "the MPC dictates that all substantive offenses merge into the conspiracy charge" — wrong because the MPC dictates that conspiracy merges into the substantive offense (not vice versa), and this only applies if the conspiracy does not encompass further criminal objectives.

Recommended fix: Add the missing fact pattern to the question stem. The prompt must describe Artie as the ringleader of a conspiracy to commit robbery, Vic's murder during the conspiracy, and Artie's subsequent post-crime $1,000 wire transfer. Without these facts, distractors (d) and (e) refer to "ghost facts" and make no sense.
-->
