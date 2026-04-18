# Fix Guidance for q05

The QA pipeline flagged this question. Rewrite `q05.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

<!-- audit: MUST FIX -->

**Safety Block Triggered.** The previous version of this question was blocked by Gemini's safety filters as unsafe. Please rewrite the fact pattern to reduce the risk of unsafe content blocking.

Error: Model returned empty or blocked response.

## Issue 2 — edge-case

**Q5.** Marlowe is also charged under the city ordinance, which makes it a "strict-liability misdemeanor to operate an unregistered storage facility." Which of the following factors most strongly supports upholding the constitutionality of this strict-liability offense under the *Morissette* framework?

(a) The offense targets inherently wicked conduct and imposes a severe penalty to strongly deter future building code and environmental storage violations.
(b) The offense strictly regulates inherently dangerous items like hand grenades, placing anyone who possesses them on automatic notice of stringent legal regulation.
(c) The offense carries a minor misdemeanor penalty, targets regulatory enforcement, and places the burden on operators who have the capacity to prevent the harm. <!-- correct -->
(d) The offense explicitly requires proof that the defendant actually knew they were operating an unregistered storage facility, defeating the strict liability presumption.
(e) The offense is justified because all city ordinances are entirely exempt from federal constitutional mens rea requirements and the common law Morissette presumption.

**Answer:** (c)

**Explanation:** (c) is correct because the four *Morissette* factors justifying public welfare strict liability are: regulatory purpose, dangerous items/activities, the defendant's capacity to prevent the harm, and minor penalties. The misdemeanor penalty and the capacity of an operator to register their facility fit this template. (a) is wrong because public welfare offenses target regulatory compliance, not inherently wicked conduct, and rely on minor penalties. (b) is wrong because an unregistered storage facility is not inherently dangerous in the way narcotics or grenades are. (d) is wrong because the ordinance explicitly imposes strict liability, dispensing with the knowledge requirement. (e) is wrong because constitutional constraints and common law presumptions apply to local laws, not just federal ones.

**Tags:** chapters: [11], topics: [public welfare offenses, Morissette factors, strict liability], difficulty: medium, cognitive: application

**Grounding:** cluster-morissette-four-factors / morissette-factor-1 / morissette-factor-4-minor-penalties

<!-- edge-case-audit: SHOULD FIX
1. Fact Pattern Booby Traps: pass
2. Cross-Doctrine Clashes: *Morissette* is a landmark statutory interpretation case regarding the presumption of mens rea when a statute is silent, distinguishing "public welfare offenses" that permit strict liability. It is not a constitutional framework (constitutional limits on strict liability are governed by due process cases like *Lambert*). Asking to uphold its "constitutionality" under *Morissette* conflates statutory interpretation with due process limits.
3. Cross-Question Spoilers: pass
Recommended fix: Change "upholding the constitutionality of this strict-liability offense" to "classifying this statute as a valid public welfare offense" to remain doctrinally precise.
-->
