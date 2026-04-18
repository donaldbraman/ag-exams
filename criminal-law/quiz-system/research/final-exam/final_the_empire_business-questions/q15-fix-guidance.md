# Fix Guidance for q15

The QA pipeline flagged this question. Rewrite `q15.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q15.** Dominic is charged with being a felon in possession of a firearm under 18 U.S.C. § 922(g). How does his genuine belief about the classification of his prior conviction affect the charge?

(a) It is a complete defense, because under Rehaif the government must prove he knew his prior conviction belonged to the prohibited class, meaning he knew it was a felony. <!-- correct -->
(b) It provides no defense, because a defendant's mistaken belief about the legal classification of a prior conviction is an invalid mistake of law under the traditional ignorance of law rule.
(c) It is a complete defense, because the Second Amendment categorically prohibits the disarmament of any person whose prior conviction was for a purely nonviolent commercial fraud offense.
(d) It provides no defense, because Rehaif only requires the government to prove that the defendant knew he possessed the firearm, not that he knew his underlying legal status.
(e) It is a complete defense, because his sentence of probation proves that the prior state court did not consider him dangerous enough to warrant stripping his constitutional firearm rights.

**Answer:** (a)

**Explanation:** Under Rehaif v. United States, the Morissette presumption requires the government to prove the defendant knew both that he possessed a firearm and that he belonged to the prohibited class. Because Dominic genuinely believed his prior conviction was a misdemeanor, he did not know he possessed the status of a felon, which negates the required mens rea. (b) is incorrect because Rehaif explicitly extends the knowledge requirement to the legal status element. (c) is incorrect because the constitutionality of disarming nonviolent felons post-Bruen and Rahimi (e.g., Range v. Attorney General) remains an actively disputed circuit split, whereas Rehaif provides a definitive statutory defense. (d) is incorrect because it states the pre-Rehaif rule. (e) is incorrect because the sentence received (probation) does not alter the statutory definition of a felony (punishable by more than one year).

**Tags:** chapters: [10, 15], topics: [mistake of law, status elements, felon in possession, Second Amendment], difficulty: hard, cognitive: analysis

**Grounding:** Rehaif v. United States; United States v. Rahimi; Range v. Attorney General

<!-- audit: MUST FIX
Check 1: Fails. Option (a) incorrectly states that Rehaif requires proving "he knew it was a felony." 18 U.S.C. § 922(g)(1) explicitly targets possession by someone convicted of "a crime punishable by imprisonment for a term exceeding one year." Knowing the offense's legal classification as a "felony" is doctrinally imprecise, as some state misdemeanors are punishable by >1 year and trigger the federal ban. 
Check 2: Fails. Because the stem omits Dominic's specific belief, a prepared student could reasonably assume he knew the offense was punishable by >1 year but mistakenly believed its legal label was a "misdemeanor." Under that assumption, Rehaif offers no defense, making Option (b) a credibly correct answer.
Check 3: Fails. The explanation relies on facts that do not exist in the stem (specifically stating that Dominic "genuinely believed his prior conviction was a misdemeanor" and referencing "the sentence received (probation)").
Check 4: Fails catastrophically. The stem is missing its core fact pattern. It asks how "his genuine belief" affects the charge, but never actually states what he believed. Option (e) also relies on "his sentence of probation," a fact never established in the prompt.
Check 5: pass
Check 6: pass
Check 7: pass
Recommended fix: Add the missing facts to the stem: "Dominic was previously convicted of a state offense and sentenced to probation. He genuinely believed his prior offense was legally punishable by a maximum of one year in prison." Revise Option (a) to match the statutory text: "meaning he knew his prior conviction was punishable by more than one year" instead of "meaning he knew it was a felony." Update the explanation accordingly.
-->
