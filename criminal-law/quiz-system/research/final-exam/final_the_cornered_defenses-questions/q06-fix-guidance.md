# Fix Guidance for q06

The QA pipeline flagged this question. Rewrite `q06.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q6.** Dave is charged as an accomplice to the warehouse arson. Under the common law approach to accomplice liability, does Dave possess the required mental state to be convicted as an accomplice?

(a) Yes, because he knew Marcus intended to burn the warehouse and his act of unlocking the door significantly facilitated the crime.
(b) Yes, because his charging of a flat upfront fee demonstrates a shared criminal purpose to destroy Silas's waterfront property.
(c) No, because taking a flat upfront fee and declaring "no stake in your beef" indicates he had knowledge but lacked the requisite purpose. <!-- correct -->
(d) No, because he did not physically participate in pouring the gasoline or starting the fire inside the warehouse with the other men.
(e) Yes, because any voluntary act that aids a felony automatically satisfies the mental state requirement for accomplice liability under the common law.

**Answer:** (c)

**Explanation:** Under the strict common law rule, an accomplice must act with the *purpose* of facilitating the underlying crime. Mere knowledge that a crime will occur is insufficient. Dave's statement that he had "no stake in your beef" and his charging of a flat upfront fee demonstrate knowledge of the arson but an explicit lack of purpose to see it succeed; he just wanted the $500. (a) is wrong because knowledge and facilitation are not enough under the strict purpose standard. (b) is wrong because a flat upfront fee (unlike a percentage cut) negates an inference of shared purpose. (d) is wrong because physical participation in the core actus reus is not required for accomplice liability. (e) is wrong because voluntary aiding requires the correct mens rea.

**Tags:** chapters: [18], topics: [accomplice liability, mens rea, purpose vs. knowledge], difficulty: medium, cognitive: application

**Grounding:** Chapter 18 (Accomplice Liability), mr-purpose-not-knowledge refinement.

<!-- audit: MUST FIX
check 1: pass
check 2: pass
check 3: pass
check 4: MUST FIX. The stem is missing the fact pattern entirely. It refers to "the warehouse arson" and the answer choices rely on specific facts (Marcus, unlocking a door, taking a flat upfront fee, declaring "no stake in your beef") that are nowhere in the prompt.
check 5: pass
check 6: pass
check 7: pass
Recommended fix: Insert the missing fact pattern into the question stem (e.g., "Marcus planned to burn down Silas's waterfront warehouse. Marcus asked Dave, a security guard, to unlock the back door. Dave charged Marcus a flat $500 upfront fee, stating 'I have no stake in your beef, I just want the cash.' Dave unlocked the door, and Marcus committed the arson.").
-->

## Issue 2 — argpass-opus

**Q6.** Dave is charged as an accomplice to the warehouse arson. Under the common law approach to accomplice liability, does Dave possess the required mental state to be convicted as an accomplice?

(a) Yes, because he knew Marcus intended to burn the warehouse and his act of unlocking the door significantly facilitated the crime.
(b) Yes, because his charging of a flat upfront fee demonstrates a shared criminal purpose to destroy Silas's waterfront property.
(c) No, because taking a flat upfront fee and declaring "no stake in your beef" indicates he had knowledge but lacked the requisite purpose. <!-- correct -->
(d) No, because he did not physically participate in pouring the gasoline or starting the fire inside the warehouse with the other men.
(e) Yes, because any voluntary act that aids a felony automatically satisfies the mental state requirement for accomplice liability under the common law.

**Answer:** (c)

**Explanation:** Under the strict common law rule, an accomplice must act with the *purpose* of facilitating the underlying crime. Mere knowledge that a crime will occur is insufficient. Dave's statement that he had "no stake in your beef" and his charging of a flat upfront fee demonstrate knowledge of the arson but an explicit lack of purpose to see it succeed; he just wanted the $500. (a) is wrong because knowledge and facilitation are not enough under the strict purpose standard. (b) is wrong because a flat upfront fee (unlike a percentage cut) negates an inference of shared purpose. (d) is wrong because physical participation in the core actus reus is not required for accomplice liability. (e) is wrong because voluntary aiding requires the correct mens rea.

**Tags:** chapters: [18], topics: [accomplice liability, mens rea, purpose vs. knowledge], difficulty: medium, cognitive: application

**Grounding:** Chapter 18 (Accomplice Liability), mr-purpose-not-knowledge refinement.

<!-- argument-pass: SHOULD FIX
(a) Argument-for: Under the minority common law approach (e.g., the *Fountain* rule), providing substantial assistance with knowledge of the criminal intent can sometimes suffice for liability, especially for serious crimes like arson. A student could argue that knowledge plus significant facilitation meets the mental state requirement here.
(b) Argument-for: A student could argue that charging a fee ties Dave's financial interest to the commission of the act. By providing a specialized service for a fee, Dave effectively joins the venture, arguably demonstrating a shared criminal purpose.
(c) Argument-for: Under the strict common law rule articulated in *United States v. Peoni*, an accomplice must act with the specific purpose of facilitating the crime. Charging a flat upfront fee without a stake in the outcome, combined with his explicit disavowal ("no stake in your beef"), proves Dave had mere knowledge but lacked the requisite purpose.
(d) Argument-for: A student might argue that Dave was merely a peripheral facilitator who didn't take part in the core actus reus, and without physical participation, he cannot be fully "associated" with the criminal venture in a way that establishes accomplice liability.
(e) Argument-for: A student might conflate general intent with the accomplice mental state, arguing that because Dave voluntarily performed an act (unlocking the door) that objectively aided a felony, the law automatically imputes the required mental state for accomplice liability.

Head-to-head: Option (c) accurately applies the majority common law *Peoni* purpose standard, correctly concluding that a flat upfront fee and explicit disavowal negate the purpose mens rea. Option (a) incorrectly concludes liability exists based solely on knowledge and significant facilitation, which fails the purpose test. Option (b) falsely claims a flat upfront fee demonstrates shared purpose, when doctrinally it demonstrates the opposite. Option (d) incorrectly implies physical participation is required for accomplice liability. Option (e) uses "automatically satisfies," which is a blatantly false legal claim for mens rea. While all distractors contain falsifiable claims, options (a) and (d) lack absolute words, leaving them slightly vulnerable to edge-case arguments about minority rules or specific factual scenarios.

Falsifiable claim per distractor:
- (a): "Yes, because he knew Marcus intended to burn the warehouse and his act of unlocking the door significantly facilitated the crime." — wrong because under the majority common law standard, knowledge and facilitation are insufficient without purpose, making the "Yes" conclusion false.
- (b): "charging of a flat upfront fee demonstrates a shared criminal purpose" — wrong because a flat fee independent of the crime's success explicitly negates an inference of shared purpose.
- (d): "because he did not physically participate in pouring the gasoline" — wrong because physical participation in the core actus reus is explicitly not required to be an accomplice.
- (e): "any voluntary act that aids a felony automatically satisfies" — wrong because it ignores the independent specific intent/purpose requirement entirely.

Recommended fix: Add absolute words to (a) and (d) to lock them perfectly. Change (a) to: "Yes, because knowledge of a crime combined with significant facilitation categorically satisfies the mental state requirement." Change (d) to: "No, solely because he did not physically participate in pouring the gasoline..."
-->
