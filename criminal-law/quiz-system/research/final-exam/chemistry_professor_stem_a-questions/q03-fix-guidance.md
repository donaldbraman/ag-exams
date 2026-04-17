# Fix Guidance for q03

The QA pipeline flagged this question. Rewrite `q03.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q3.** Assume Arthur is charged with homicide based on his failure to summon emergency medical aid for Marcus. Did Arthur owe a legal duty to act under these circumstances?

(a) Yes, because Arthur owed a contractual duty to Marcus as a buyer in a commercial drug transaction.
(b) No, because Arthur did not have a recognized special status relationship with Marcus, such as parent or spouse.
(c) Yes, because Arthur created the peril by distributing the lethal drug that caused Marcus to overdose. <!-- correct -->
(d) No, because the general rule of criminal law is that individuals have no legal duty to rescue strangers in distress.
(e) Yes, because the jurisdiction's Controlled Substances Act implicitly creates a statutory duty to report overdoses.

**Answer:** (c)

**Explanation:** Criminal omission liability requires a legal duty to act. One of the recognized *Jones* categories triggering a duty is the "creation of peril." Because Arthur provided the drugs that caused Marcus to overdose, he created the dangerous situation and therefore had a legal duty to summon aid. (a) is wrong because illegal drug sales do not create enforceable contractual duties to rescue. (b) is wrong because a status relationship is not required if the defendant created the peril. (d) is wrong because while the baseline rule is no duty to rescue, the creation of peril forms an exception. (e) is wrong because there is no fact indicating a specific statutory duty to report overdoses.

**Tags:** chapters: [9], topics: [omissions, creation of peril, duty to act], difficulty: easy, cognitive: application

**Grounding:** creation-of-peril-category

<!-- audit: MUST FIX
Check 1: pass (Under the creation of peril doctrine, providing lethal drugs that cause an overdose can trigger a duty to act).
Check 2: MUST FIX (Because the stem lacks the facts showing Arthur actually created the peril, a prepared student could successfully argue for (d)—since the stem gives no facts establishing a *Jones* exception, the baseline "no duty" rule should apply).
Check 3: pass (The explanation correctly applies the creation of peril doctrine, but relies on facts entirely missing from the stem).
Check 4: MUST FIX (The stem is completely missing the factual scenario. It asks whether Arthur had a duty "under these circumstances," but the only circumstance provided is that he was charged. The facts that Arthur sold the drugs and caused the overdose only appear in the answer choices and explanation).
Check 5: pass
Check 6: pass
Check 7: pass
Recommended fix: Add the missing facts to the stem. Example: "Arthur sold a lethal batch of drugs to Marcus. Marcus consumed the drugs in Arthur's presence and began to overdose. Arthur did not call 911 or summon help. Assume Arthur is charged with homicide based on his failure to summon emergency medical aid for Marcus. Did Arthur owe a legal duty to act under these circumstances?"
-->

## Issue 2 — argpass-sonnet

**Q3.** Assume Arthur is charged with homicide based on his failure to summon emergency medical aid for Marcus. Did Arthur owe a legal duty to act under these circumstances?

(a) Yes, because Arthur owed a contractual duty to Marcus as a buyer in a commercial drug transaction.
(b) No, because Arthur did not have a recognized special status relationship with Marcus, such as parent or spouse.
(c) Yes, because Arthur created the peril by distributing the lethal drug that caused Marcus to overdose. <!-- correct -->
(d) No, because the general rule of criminal law is that individuals have no legal duty to rescue strangers in distress.
(e) Yes, because the jurisdiction's Controlled Substances Act implicitly creates a statutory duty to report overdoses.

**Answer:** (c)

**Explanation:** Criminal omission liability requires a legal duty to act. One of the recognized *Jones* categories triggering a duty is the "creation of peril." Because Arthur provided the drugs that caused Marcus to overdose, he created the dangerous situation and therefore had a legal duty to summon aid. (a) is wrong because illegal drug sales do not create enforceable contractual duties to rescue. (b) is wrong because a status relationship is not required if the defendant created the peril. (d) is wrong because while the baseline rule is no duty to rescue, the creation of peril forms an exception. (e) is wrong because there is no fact indicating a specific statutory duty to report overdoses.

**Tags:** chapters: [9], topics: [omissions, creation of peril, duty to act], difficulty: easy, cognitive: application

**Grounding:** creation-of-peril-category

<!-- argument-pass: SHOULD FIX
(a) Argument-for: Under the *Jones v. United States* framework, one of the five recognized categories of legal duty arises from a contract. While illegal contracts are generally void, a student could argue that the commercial nature of the drug transaction creates a de facto "special relationship" or a contractual expectation that the purveyor of a dangerous substance will monitor the consumer's safety. This interpretation suggests that by accepting money in exchange for a high-risk product, Arthur implicitly contracted to provide a safe environment or necessary assistance should the product cause foreseeable harm.

(b) Argument-for: This option correctly observes that Arthur and Marcus lack a formal "status relationship," which is often the most common trigger for a duty to act. In jurisdictions that strictly construe omission liability to avoid over-criminalization, a court might hold that in the absence of a parent-child or spousal bond, the law should not impose a duty to rescue. This argument posits that Marcus’s voluntary ingestion of the drug was an independent act that prevents Arthur’s conduct from reaching the level of "creating the peril," leaving the lack of a status relationship as the dispositive legal factor.

(c) Argument-for: The "creation of peril" doctrine specifies that if a person's actions, whether criminal or innocent, place another in a position of danger, that person acquires a legal duty to take reasonable steps to prevent further harm. Here, Arthur’s act of distributing the lethal drug is the direct "but-for" cause of Marcus’s overdose. Because Arthur set the life-threatening situation in motion, he was no longer a mere bystander and was legally obligated to summon emergency aid, making his failure to do so a valid basis for a homicide charge.

(d) Argument-for: This option relies on the fundamental "American Bystander" rule, which dictates that individuals generally owe no legal duty to rescue others from distress. A student could argue that this baseline rule applies because the act of selling a product to a competent adult does not legally constitute the "creation of peril"; rather, the buyer’s autonomous decision to consume the substance is the source of the danger. Under this theory, Arthur remains a legal stranger to Marcus's self-inflicted plight, and the general rule of no-rescue remains the governing principle.

(e) Argument-for: Statutes are a recognized source of legal duties to act under *Jones*. One could argue that the jurisdiction's Controlled Substances Act, designed to protect public health from the dangers of narcotics, carries an inherent statutory obligation for those involved in the distribution chain to minimize fatal outcomes. This argument suggests that the comprehensive regulatory scheme of the CSA creates a "duty imposed by statute" requiring participants to report medical emergencies caused by the very substances the Act seeks to control.

Head-to-head: (c) is the strongest option as it reflects the prevailing common law exception that supplying the instrument of death constitutes the "creation of peril," triggering a duty to act. (d) is its most significant rival, as it correctly states the general rule of no-rescue, which would apply if a court determined the victim's voluntary act broke the chain of causation. However, (b) and (d) are both "No" answers that ignore the specific exception applicable here. (a) and (e) are weaker because they rely on "implicit" or illegal versions of recognized duties (contract and statute) that are almost never upheld in criminal court. Distractors (b) and (d) are technically "true but incomplete" rather than containing "explicit false legal claims," as they state general rules or facts but use them to reach an incorrect conclusion by omitting the exception.

Falsifiable claim per distractor:
- (a): "Arthur owed a contractual duty... as a buyer" — wrong because illegal drug transactions are void as a matter of public policy and cannot generate enforceable legal duties; additionally, Arthur was the seller, not the buyer.
- (b): "No, because Arthur did not have a recognized special status relationship" — wrong because it implies that a status relationship is the only way to trigger a duty, whereas creation of peril is an independent and sufficient trigger.
- (d): "No, because the general rule... is that individuals have no legal duty to rescue" — wrong because it asserts the general rule applies here, disregarding the specific "creation of peril" exception triggered by the distribution of the drugs.
- (e): "the jurisdiction's Controlled Substances Act implicitly creates a statutory duty" — wrong because criminal omission liability based on a statute requires an explicit legislative mandate to satisfy the principle of legality and fair notice.

Recommended fix: To meet the close-call standard, add absolute language to distractors (b) and (d) to make their legal claims explicitly false. For (b): "No, because a status relationship is categorically required to trigger a legal duty to act." For (d): "No, because the no-duty-to-rescue rule applies regardless of whether the defendant provided the substance causing the distress."
-->

## Issue 3 — argpass-opus

**Q3.** Assume Arthur is charged with homicide based on his failure to summon emergency medical aid for Marcus. Did Arthur owe a legal duty to act under these circumstances?

(a) Yes, because Arthur owed a contractual duty to Marcus as a buyer in a commercial drug transaction.
(b) No, because Arthur did not have a recognized special status relationship with Marcus, such as parent or spouse.
(c) Yes, because Arthur created the peril by distributing the lethal drug that caused Marcus to overdose. <!-- correct -->
(d) No, because the general rule of criminal law is that individuals have no legal duty to rescue strangers in distress.
(e) Yes, because the jurisdiction's Controlled Substances Act implicitly creates a statutory duty to report overdoses.

**Answer:** (c)

**Explanation:** Criminal omission liability requires a legal duty to act. One of the recognized *Jones* categories triggering a duty is the "creation of peril." Because Arthur provided the drugs that caused Marcus to overdose, he created the dangerous situation and therefore had a legal duty to summon aid. (a) is wrong because illegal drug sales do not create enforceable contractual duties to rescue. (b) is wrong because a status relationship is not required if the defendant created the peril. (d) is wrong because while the baseline rule is no duty to rescue, the creation of peril forms an exception. (e) is wrong because there is no fact indicating a specific statutory duty to report overdoses.

**Tags:** chapters: [9], topics: [omissions, creation of peril, duty to act], difficulty: easy, cognitive: application

**Grounding:** creation-of-peril-category

<!-- argument-pass: SHOULD FIX
(a) Argument-for: A contractual duty to act is one of the recognized *Jones* categories that establishes a legal duty. The facts state Marcus was a buyer in a drug transaction, implying a commercial agreement between the two. Even in illicit contexts, a court could theoretically find an implied assumption of care during the physical transaction. Thus, the transaction itself creates a contractual duty to act.
(b) Argument-for: Omission liability generally requires a legal duty to act, often derived from a special status relationship under *Jones v. United States* (e.g., parent-child or spouses). Since Arthur and Marcus were merely parties to a transaction, no such special status relationship existed. Without this relationship, a student could argue the baseline rule of no duty to rescue applies, excusing Arthur from liability.
(c) Argument-for: Under the *Jones* categories for omission liability, a legal duty to act is imposed when a person creates the peril that places another in danger. By providing the lethal drug to Marcus, Arthur factually caused the perilous situation. Because he created this peril, Arthur acquired a legal duty to summon emergency medical aid.
(d) Argument-for: Anglo-American criminal law generally imposes no legal duty to rescue or summon aid for a stranger in peril. Even if Arthur provided the drugs, Marcus's overdose resulted from his own voluntary act of ingestion, making Arthur legally a mere bystander to the distress. Therefore, the general rule of no duty to rescue applies, shielding Arthur from omission liability.
(e) Argument-for: Statutory duties are another recognized *Jones* category. Given the context of a lethal overdose, a student could argue that modern Controlled Substances Acts implicitly mandate reporting medical emergencies arising from illicit distribution. Assuming such an implicit statutory framework applies, Arthur would have a legally recognized duty to report the overdose.

Head-to-head: Option (c) is the definitively correct answer because it accurately applies the "creation of peril" exception to the facts. Option (a) contains an explicitly false claim about illegal contracts forming enforceable duties. Option (e) contains a false claim about implicit statutory duties. However, options (b) and (d) are the weakest distractors because they lack explicitly false legal claims. They state true legal premises (Arthur lacked a status relationship; the general rule is no duty to rescue) and rely on implicit omissions to reach the wrong conclusion, failing the close-call standard without absolute locking words. 

Falsifiable claim per distractor:
- (a): "Arthur owed a contractual duty to Marcus as a buyer in a commercial drug transaction." — wrong because illegal contracts are void against public policy and do not create legally enforceable *Jones* duties to rescue.
- (b): "Arthur did not have a recognized special status relationship" — wrong only by implicit omission; the statement itself is factually and legally true, but lacks an absolute word (like "solely") to make the legal reasoning explicitly false.
- (d): "the general rule of criminal law is that individuals have no legal duty to rescue strangers" — wrong only by implicit omission of exceptions; the articulation of the general rule is true, and it lacks absolute words to deny exceptions (e.g., "categorically").
- (e): "the jurisdiction's Controlled Substances Act implicitly creates a statutory duty" — wrong because there is no such general implicit statutory duty to report overdoses recognized under standard Controlled Substances Acts.

Recommended fix: Add absolute locking words to (b) and (d). 
Change (b) to: "No, because a legal duty to act arises solely from a recognized special status relationship, such as parent or spouse." 
Change (d) to: "No, because criminal law categorically imposes no legal duty to rescue strangers in distress, regardless of how the peril arose."
-->
