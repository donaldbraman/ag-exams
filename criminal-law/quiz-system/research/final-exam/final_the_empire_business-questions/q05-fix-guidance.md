# Fix Guidance for q05

The QA pipeline flagged this question. Rewrite `q05.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q5.** Assume that, whether or not Kevin "used" the firearm on October 1, he is charged with being a felon in possession of a firearm under 18 U.S.C. § 922(g). Kevin argues he cannot be convicted because he genuinely believed his attorney's email stating he was not a felon. Will this argument succeed?

(a) Yes, because a genuine reliance on private legal counsel categorically negates the general intent required to unlawfully possess a dangerous weapon in interstate commerce.
(b) No, because the statute is silent on mental state, meaning the court must apply a strict liability standard to the defendant's prior felony conviction status.
(c) Yes, because the government must prove that Kevin knew both that he possessed the firearm and that he belonged to the prohibited class of felons. <!-- correct -->
(d) No, because ignorance of one's legal status is equivalent to ignorance of the law, which is traditionally barred as a defense in federal firearms prosecutions.
(e) Yes, because his underlying state conviction was labeled "commercial fraud," meaning it lacked the requisite malum in se character to qualify under the federal statute.

**Answer:** (c)

**Explanation:** The correct answer is (c). Under *Rehaif v. United States*, the government must prove that the defendant knew both the conduct (possessing the firearm) and the attendant circumstance (belonging to the prohibited status class, i.e., being a felon). Because Kevin genuinely believed he was convicted of a misdemeanor, he lacked knowledge of his prohibited status. (a) is wrong because reliance on private counsel is not a categorical defense; the defense works here specifically because his mistake negates the knowledge element required by *Rehaif*. (b) is wrong because under the *Morissette* presumption, statutory silence does not mean strict liability; courts read in a mens rea requirement. (d) is wrong because knowing one's prohibited status is treated as a factual circumstance element under *Rehaif*, not an ignorance-of-the-law excuse. (e) is wrong because the federal statute defines a qualifying felony by its maximum potential sentence, not by whether it is malum in se.

**Tags:** chapters: [10], topics: [Rehaif, mens rea of status elements, Morissette presumption], difficulty: hard, cognitive: application

**Grounding:** Chapter 10, Presumption Against Strict Liability (rehaif-status-element; Rehaif v. United States)

<!-- audit: MUST FIX
check 1: pass
check 2: finding: A prepared student could argue (d) is correct because if Kevin knew the facts of his conviction (e.g., that he was sentenced to more than a year in prison) but his attorney's email simply gave bad legal advice that it didn't count as a "felony," this might be treated as an invalid mistake of law rather than a negation of his factual status under *Rehaif*.
check 3: finding: The explanation assumes a fact not in evidence, stating "Because Kevin genuinely believed he was convicted of a misdemeanor..." However, the prompt only says the email stated "he was not a felon."
check 4: finding: The stem lacks the factual specificity needed to confidently choose (c) over (d). It does not clarify whether the attorney's email caused a mistake of fact (e.g., about the maximum sentence or classification of the prior conviction) or an invalid mistake of law.
check 5: pass
check 6: pass
check 7: pass
check 8: pass
Recommended fix: Change the prompt's wording from "stating he was not a felon" to "stating his prior conviction was only a misdemeanor" so that the stem aligns with the explanation and cleanly triggers the *Rehaif* mistake-of-status-fact doctrine.
-->

## Issue 2 — argpass-sonnet

**Q5.** Assume that, whether or not Kevin "used" the firearm on October 1, he is charged with being a felon in possession of a firearm under 18 U.S.C. § 922(g). Kevin argues he cannot be convicted because he genuinely believed his attorney's email stating he was not a felon. Will this argument succeed?

(a) Yes, because a genuine reliance on private legal counsel categorically negates the general intent required to unlawfully possess a dangerous weapon in interstate commerce.
(b) No, because the statute is silent on mental state, meaning the court must apply a strict liability standard to the defendant's prior felony conviction status.
(c) Yes, because the government must prove that Kevin knew both that he possessed the firearm and that he belonged to the prohibited class of felons. <!-- correct -->
(d) No, because ignorance of one's legal status is equivalent to ignorance of the law, which is traditionally barred as a defense in federal firearms prosecutions.
(e) Yes, because his underlying state conviction was labeled "commercial fraud," meaning it lacked the requisite malum in se character to qualify under the federal statute.

**Answer:** (c)

**Explanation:** The correct answer is (c). Under *Rehaif v. United States*, the government must prove that the defendant knew both the conduct (possessing the firearm) and the attendant circumstance (belonging to the prohibited status class, i.e., being a felon). Because Kevin genuinely believed he was convicted of a misdemeanor, he lacked knowledge of his prohibited status. (a) is wrong because reliance on private counsel is not a categorical defense; the defense works here specifically because his mistake negates the knowledge element required by *Rehaif*. (b) is wrong because under the *Morissette* presumption, statutory silence does not mean strict liability; courts read in a mens rea requirement. (d) is wrong because knowing one's prohibited status is treated as a factual circumstance element under *Rehaif*, not an ignorance-of-the-law excuse. (e) is wrong because the federal statute defines a qualifying felony by its maximum potential sentence, not by whether it is malum in se.

**Tags:** chapters: [10], topics: [Rehaif, mens rea of status elements, Morissette presumption], difficulty: hard, cognitive: application

**Grounding:** Chapter 10, Presumption Against Strict Liability (rehaif-status-element; Rehaif v. United States)

<!-- argument-pass: SHOULD FIX
(a) Argument-for: A student might argue that the advice of counsel defense is directly applicable here since Kevin relied on his lawyer's email. If he genuinely believed he was acting lawfully based on a professional's advice, this reliance would conceptually negate the culpability required for the offense. Furthermore, the option's reference to "general intent" might align with older, generalized understandings of weapons possession charges. The student could wrongly conclude that this specific reliance makes it impossible for the government to prove any criminal mind.
(b) Argument-for: A student could observe that 18 U.S.C. § 922(g) lists the elements of the offense without explicitly attaching a mens rea to the status element in the text of that subsection. Following a strict textualist approach, if Congress omits a mental state for a specific attendant circumstance, it may intend strict liability for that element. Therefore, Kevin's mistaken belief would be irrelevant, and he would be strictly liable for being a felon in possession.
(c) Argument-for: A student would recognize this as the direct holding of the Supreme Court in *Rehaif v. United States*. Under *Rehaif*, the "knowingly" mens rea found in the corresponding penalty provision applies to all material elements of the § 922(g) offense, including the defendant's status as a felon. Because Kevin genuinely believed he was not a felon due to his attorney's email, the government cannot prove he knew he belonged to the prohibited class, meaning his argument succeeds.
(d) Argument-for: A student might rely on the age-old maxim *ignorantia juris non excusat* (ignorance of the law is no excuse). If a person is convicted of a crime, knowing the legal classification of that conviction (felony vs. misdemeanor) is arguably a pure question of law. Therefore, Kevin's mistake about his legal status as a felon is a mistake of law, which is traditionally barred as a defense, rendering his argument invalid.
(e) Argument-for: A student might recall that federal criminal law sometimes distinguishes between *malum in se* (inherently wrong) and *malum prohibitum* (wrong because prohibited) offenses, particularly when assessing mens rea and statutory reach. They might argue that commercial fraud is a regulatory or *malum prohibitum* offense. The student could incorrectly infer that federal firearms prohibitions only target individuals with "dangerous" or inherently wicked felony convictions.

Head-to-head: Option (c) correctly applies *Rehaif v. United States*, making it the undeniably correct answer. Option (a) relies on an advice-of-counsel theory but makes the false claim that it "categorically negates" general intent (reliance on counsel is not a categorical general-intent defense; rather, here the mistake specifically negates the "knowledge" requirement). Option (b) correctly notes statutory silence but falsely claims the court "must apply a strict liability standard," violating the *Morissette* presumption. Option (e) invents a requirement that the underlying felony must possess a "requisite malum in se character," which is structurally false under the statute. Option (d) presents a strong distractor based on mistake of law, but the claim that ignorance of legal status "is equivalent to ignorance of the law" was explicitly rejected in *Rehaif*. However, (d) uses "traditionally barred," which is arguably soft. A minor edit would ensure (d) is locked with an absolute word.

Falsifiable claim per distractor:
- (a): "categorically negates the general intent required" — wrong because reliance on counsel is not a categorical defense to general intent, and the statute actually requires knowledge, not general intent.
- (b): "must apply a strict liability standard" — wrong because under the *Morissette* presumption, statutory silence regarding mens rea prompts courts to read in a mental state, rather than defaulting to strict liability.
- (d): "ignorance of one's legal status is equivalent to ignorance of the law, which is traditionally barred" — wrong because *Rehaif* explicitly held that ignorance of felon status acts as a mistake of fact/attendant circumstance rather than an equivalent to ignorance of the law. 
- (e): "lacked the requisite malum in se character" — wrong because 18 U.S.C. § 922(g) defines a felony solely by its potential sentence (exceeding one year), regardless of whether the crime is malum in se.

Recommended fix: In (d), change "traditionally barred" to "categorically barred" to fully satisfy the close-call standard's requirement for absolute words.
-->
