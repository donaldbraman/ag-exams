# Fix Guidance for q01

The QA pipeline flagged this question. Rewrite `q01.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q1.** The prosecution charges Arthur with manufacturing and distributing Compound Y. Arthur files a motion to dismiss, arguing that because the statute is silent on mens rea, it imposes strict liability, which is unconstitutional for a felony. Which of the following is the most likely ruling on the mens rea requirement?

(a) The statute imposes strict liability because drug manufacturing involves dangerous items that put the possessor on notice of regulation.
(b) The statute requires proof of mens rea because the severe 15-year maximum penalty rebuts the presumption of a strict liability public welfare offense. <!-- correct -->
(c) The statute imposes strict liability because the legislature's silence on mens rea conclusively demonstrates an intent to eliminate the requirement.
(d) The statute requires proof of mens rea because all public welfare offenses constitutionally require proof of the defendant's knowledge of the regulation.
(e) The statute imposes strict liability because the explicit goal of the statute is to protect public health and safety from dangerous substances.

**Answer:** (b)

**Explanation:** Under *Staples v. United States*, when a statute carries a severe felony penalty (such as 15 years), courts presume the legislature intended to require mens rea even if the statute is silent. This severe penalty rebuts the normal presumption that silence equals strict liability for regulatory offenses. (a) is wrong because while drug dealing involves dangerous items, the severe penalty overrides the strict liability heuristic. (c) is wrong because the *Morissette* presumption holds that statutory silence does not eliminate mens rea. (d) is wrong because public welfare offenses can be strict liability if the penalties are minor. (e) is wrong because regulatory purpose alone does not justify strict liability when penalties are severe.

**Tags:** chapters: [11], topics: [public welfare offenses, Staples presumption, statutory interpretation], difficulty: medium, cognitive: application

**Grounding:** staples-outlier-serious-penalties

<!-- audit: MUST FIX
check 1: pass (The doctrinal application of *Staples* is legally accurate, but see check 4).
check 2: Option (a) is defensible. Because the stem doesn't specify the penalty length, a prepared student could analogize "Compound Y" directly to *Balint* (narcotics), which the Supreme Court held *was* a strict liability public welfare offense despite being a felony. 
check 3: pass
check 4: Fail. The stem is missing crucial facts that magically appear in the answer choices. The stem never states that the crime carries a "15-year maximum penalty" (needed for B) or that Compound Y is a "drug" (needed for A). A student cannot select (b) based on facts not in the fact pattern.
check 5: pass
check 6: pass
check 7: pass
Recommended fix: Inject the missing facts into the stem: "The prosecution charges Arthur with manufacturing and distributing Compound Y, a regulated pharmaceutical drug. The statute is silent on mens rea but carries a 15-year maximum prison sentence..."
-->

## Issue 2 — argpass-opus

**Q1.** The prosecution charges Arthur with manufacturing and distributing Compound Y. Arthur files a motion to dismiss, arguing that because the statute is silent on mens rea, it imposes strict liability, which is unconstitutional for a felony. Which of the following is the most likely ruling on the mens rea requirement?

(a) The statute imposes strict liability because drug manufacturing involves dangerous items that put the possessor on notice of regulation.
(b) The statute requires proof of mens rea because the severe 15-year maximum penalty rebuts the presumption of a strict liability public welfare offense. <!-- correct -->
(c) The statute imposes strict liability because the legislature's silence on mens rea conclusively demonstrates an intent to eliminate the requirement.
(d) The statute requires proof of mens rea because all public welfare offenses constitutionally require proof of the defendant's knowledge of the regulation.
(e) The statute imposes strict liability because the explicit goal of the statute is to protect public health and safety from dangerous substances.

**Answer:** (b)

**Explanation:** Under *Staples v. United States*, when a statute carries a severe felony penalty (such as 15 years), courts presume the legislature intended to require mens rea even if the statute is silent. This severe penalty rebuts the normal presumption that silence equals strict liability for regulatory offenses. (a) is wrong because while drug dealing involves dangerous items, the severe penalty overrides the strict liability heuristic. (c) is wrong because the *Morissette* presumption holds that statutory silence does not eliminate mens rea. (d) is wrong because public welfare offenses can be strict liability if the penalties are minor. (e) is wrong because regulatory purpose alone does not justify strict liability when penalties are severe.

**Tags:** chapters: [11], topics: [public welfare offenses, Staples presumption, statutory interpretation], difficulty: medium, cognitive: application

**Grounding:** staples-outlier-serious-penalties

<!-- argument-pass: MUST FIX
(a) Argument-for: Under the public welfare offense doctrine established in cases like *Balint* and *Dotterweich*, regulations concerning dangerous drugs and substances are designed to protect public health and safety. The dangerous nature of manufacturing "Compound Y" inherently puts the defendant on notice of regulation, satisfying the *Staples* exception for dangerous devices. Therefore, a silent statute in this context imposes strict liability.
(b) Argument-for: Under *Staples v. United States*, mere statutory silence does not dispense with the mens rea requirement. This is especially true for felonies with severe penalties (like the 15 years stipulated by this option). The presence of a severe felony penalty rebuts the presumption that the statute is a strict liability public welfare offense, meaning mens rea must be proven.
(c) Argument-for: According to strict textualist interpretations, courts should not read requirements into a statute that the legislature chose to omit. If a statute is silent on mens rea, it conclusively demonstrates that the legislature intended to eliminate the requirement. Thus, the statute imposes strict liability.
(d) Argument-for: Due process principles mandate that criminal punishment requires some degree of culpability. Even for public welfare offenses, defendants must have at least some knowledge to be constitutionally convicted. Therefore, all public welfare offenses constitutionally require proof of the defendant's knowledge of the regulation.
(e) Argument-for: The primary justification for public welfare offenses is the protection of society from widespread harm. When a statute explicitly aims to protect public health and safety from dangerous substances, courts interpret silence as imposing strict liability to maximize deterrence. Thus, the statute imposes strict liability.

Head-to-head: Option (b) is the intended correct answer because it correctly applies the *Staples* rule that severe penalties prevent a silent statute from being interpreted as a strict liability public welfare offense. However, option (b) is fatally flawed because it introduces a "15-year maximum penalty" that is nowhere found in the question stimulus. A reasonable student would eliminate (b) for assuming facts not in evidence. Options (a) and (e) are legally plausible for minor regulatory offenses but fail here because the prompt specifies it is a felony. Option (c) contradicts the *Morissette* presumption. Option (d) relies on an absolute, false claim about constitutional requirements for public welfare offenses. Because the correct answer relies on a highly specific phantom fact, this question MUST FIX.

Falsifiable claim per distractor:
- (a): "The statute imposes strict liability" — wrong because under *Staples*, the severe felony classification precludes applying the strict liability public welfare exception, regardless of the dangerousness of the items.
- (c): "silence on mens rea conclusively demonstrates an intent to eliminate the requirement" — wrong because under *Morissette* and *Staples*, silence creates a presumption that mens rea *is* required, not conclusively eliminated.
- (d): "all public welfare offenses constitutionally require proof of the defendant's knowledge of the regulation" — wrong because the Supreme Court has repeatedly held that true public welfare offenses can constitutionally impose strict liability without knowledge.
- (e): "The statute imposes strict liability because the explicit goal..." — wrong because regulatory purpose alone does not override the presumption of mens rea for a felony offense.

Recommended fix: Add the 15-year penalty to the stimulus: "The prosecution charges Arthur with manufacturing and distributing Compound Y, a felony carrying a maximum penalty of 15 years in prison." Alternatively, modify option (b) to remove the specific number: "because the severe felony penalty rebuts the presumption..."
-->
