# Fix Guidance for q09

The QA pipeline flagged this question. Rewrite `q09.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q9.** Assume again that the payment to the judge constitutes a substantive criminal offense. Under the traditional common law approach to accomplice liability, is Thorne liable as an accomplice to Vance's crime?

(a) Yes, because Thorne knowingly facilitated the crime by physically delivering the briefcase, and knowledge is the standard mens rea for all forms of accomplice liability.
(b) Yes, because Thorne owed a fiduciary duty to the court as an attorney, which converts his knowing assistance into purposeful facilitation of the underlying crime.
(c) No, because traditional accomplice liability requires the defendant to act with the purpose of promoting the offense, and Thorne's purpose was only to collect fees. <!-- correct -->
(d) No, because accomplice liability requires the accessory to be physically present at the exact moment the principal completes the substantive criminal act.
(e) No, because Thorne was merely following the directives of his client, which provides an affirmative defense of professional compulsion under the common law.

**Answer:** (c)

**Explanation:** Under the traditional common law approach (e.g., Judge Learned Hand's formulation in *Peoni*), accomplice liability requires that the accessory act with the "purpose" or specific intent of promoting or facilitating the commission of the offense. Mere knowledge that one's actions will assist the principal is insufficient. Because Thorne acted only with the purpose of collecting fees, he lacks the requisite purpose (Fact 5). (c) is correct. (a) is wrong because knowledge is not the traditional baseline standard; purpose is generally required. (b) is wrong because an attorney's fiduciary duty does not alter the fundamental mens rea requirement for criminal accomplice liability. (d) is wrong because a person can be an accessory before the fact without being physically present during the culmination of the crime. (e) is wrong because professional compulsion by a client is not a recognized legal defense in criminal law.

**Tags:** chapters: [5], topics: [accomplice-liability, mens-rea, purpose-vs-knowledge], difficulty: medium, cognitive: application

**Grounding:** United States v. Peoni, 100 F.2d 401 (2d Cir. 1938) and traditional accomplice mens rea

<!-- audit: MUST FIX
<check 1>: pass
<check 2>: pass
<check 3>: pass
<check 4>: fails. The question is a dependent question ("Assume again...") that relies on an external, unprovided master fact pattern containing the identities of Thorne, Vance, and the details of the briefcase delivery and fee collection.
<check 5>: pass
<check 6>: pass
<check 7>: pass
<check 8>: pass
Recommended fix: Provide the necessary facts within the question stem itself to make it a standalone question (e.g., "Thorne knowingly delivered a briefcase of bribe money to a judge on behalf of his client Vance, but Thorne's only purpose in doing so was to collect his legal fees..."), or explicitly bundle it with the master fact pattern.
-->

## Issue 2 — edge-case

<!-- edge-case-audit: SHOULD FIX
1. Fact Pattern Booby Traps: By having Thorne physically hand the briefcase to the judge, Thorne actually commits the actus reus of the delivery, making him a Principal in the First Degree (or an innocent agent, given his lack of specific intent) rather than a traditional secondary "accomplice." However, the legal logic of Option (c) still holds perfectly: because he lacks the specific intent/purpose to sway or reward the judge, he is not liable as an accomplice (nor as a principal). 
2. Cross-Doctrine Clashes: There is a minor risk that students confuse motive (collecting fees) with immediate purpose (delivering the briefcase). However, Fact 5 explicitly states Thorne "doesn't care if the judge is swayed or rewarded," which correctly neutralizes the specific intent required for the underlying bribery/gratuity offense. 
3. Cross-Question Spoilers: Q7 tests whether this payment is a bribe or a gratuity (which *Snyder* decriminalized federally). The prompt smartly bypasses this by stating "Assume again that the payment... constitutes a substantive criminal offense," insulating it from Q7's outcome. However, Facts 1-3 establish that Vance committed multiple crimes (RICO, drug trafficking) and Fact 3 explicitly states Thorne *agreed to help* the drug operation evade detection (giving him "purpose" for those crimes). If a student misreads "Vance's crime" as referring to the fentanyl operation rather than the payment, they will be confused. 

Recommended fix: In the question stem, change "is Thorne liable as an accomplice to Vance's crime?" to "is Thorne liable as an accomplice to Vance's offense of paying the judge?" to explicitly firewall this question from Thorne's purposeful facilitation of the RICO enterprise in Fact 3.
-->
