# Fix Guidance for q05

The QA pipeline flagged this question. Rewrite `q05.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — grounding

**Q5.** Assume Arthur is charged under a statute criminalizing the "reckless creation of a risk of catastrophe." Can Arthur successfully defend against this charge by arguing his instruction to Brenda ("No flammable agents") meant he did not proximately cause the actual fire?

(a) Yes, because catastrophe statutes fundamentally operate as result crimes. The prosecution must establish a direct causal link between the defendant's conduct and the ultimate property damage.
(b) Yes, because Arthur's explicit instruction against using flammable agents functions as a legally sufficient independent intervening cause. This instruction completely severs his proximate liability.
(c) No, because risking catastrophe is a conduct crime that eliminates the causation requirement entirely. The prosecution only needs to prove Arthur recklessly created the risk by establishing the illicit lab. <!-- correct -->
(d) No, because the Model Penal Code applies the "too remote or accidental" standard to both conduct and result crimes. Causation is automatically presumed for all high-risk felony enterprises.
(e) No, because Arthur's instruction to keep a low profile demonstrates he possessed the specific intent to cause a catastrophic event. This elevates his culpability beyond mere recklessness to purpose.

**Answer:** (c)

**Explanation:** Option (c) is correct because statutes targeting the "creation of a risk of catastrophe" are conduct crimes, not result crimes. The prosecution does not need to trace a causal chain from Arthur to the actual fire; they only need to prove his involvement in setting up a hazardous chemical lab in a residential high-rise recklessly created a catastrophic risk. Option (a) is incorrect because risking catastrophe is a conduct crime that deliberately abandons the causation requirement. Option (b) is incorrect because intervening causes apply only to result crimes. Option (d) is incorrect because the MPC causation standards do not apply to conduct crimes, which require no result to be caused. Option (e) is incorrect because an instruction to "keep a low profile" to avoid detection does not demonstrate specific intent to cause a catastrophe.

**Tags:** chapters: [8], topics: [causation, risking vs causing catastrophe, conduct crimes], difficulty: medium, cognitive: application

**Grounding:** Chapter 8, Beyond Causation: Risking Catastrophe and Widespread Harm (Conduct vs Result Crimes)

<!-- GROUNDING-FAIL: risking vs causing catastrophe is not in any chapter map. The closest taught doctrines are: None (meta-map missing). Correct answer must rely on one of those instead. -->

## Issue 2 — audit

**Q5.** Assume Arthur is charged under a statute criminalizing the "reckless creation of a risk of catastrophe." Can Arthur successfully defend against this charge by arguing his instruction to Brenda ("No flammable agents") meant he did not proximately cause the actual fire?

(a) Yes, because catastrophe statutes fundamentally operate as result crimes. The prosecution must establish a direct causal link between the defendant's conduct and the ultimate property damage.
(b) Yes, because Arthur's explicit instruction against using flammable agents functions as a legally sufficient independent intervening cause. This instruction completely severs his proximate liability.
(c) No, because risking catastrophe is a conduct crime that eliminates the causation requirement entirely. The prosecution only needs to prove Arthur recklessly created the risk by establishing the illicit lab. <!-- correct -->
(d) No, because the Model Penal Code applies the "too remote or accidental" standard to both conduct and result crimes. Causation is automatically presumed for all high-risk felony enterprises.
(e) No, because Arthur's instruction to keep a low profile demonstrates he possessed the specific intent to cause a catastrophic event. This elevates his culpability beyond mere recklessness to purpose.

**Answer:** (c)

**Explanation:** Option (c) is correct because statutes targeting the "creation of a risk of catastrophe" are conduct crimes, not result crimes. The prosecution does not need to trace a causal chain from Arthur to the actual fire; they only need to prove his involvement in setting up a hazardous chemical lab in a residential high-rise recklessly created a catastrophic risk. Option (a) is incorrect because risking catastrophe is a conduct crime that deliberately abandons the causation requirement. Option (b) is incorrect because intervening causes apply only to result crimes. Option (d) is incorrect because the MPC causation standards do not apply to conduct crimes, which require no result to be caused. Option (e) is incorrect because an instruction to "keep a low profile" to avoid detection does not demonstrate specific intent to cause a catastrophe.

**Tags:** chapters: [8], topics: [causation, risking vs causing catastrophe, conduct crimes], difficulty: medium, cognitive: application

**Grounding:** Chapter 8, Beyond Causation: Risking Catastrophe and Widespread Harm (Conduct vs Result Crimes)

<!-- audit: MUST FIX
check 1: pass
check 2: pass
check 3: pass
check 4: fails. The stem refers to Arthur, Brenda, an "actual fire," and option (c) references "establishing the illicit lab," but no background facts are provided. The explanation further mentions "setting up a hazardous chemical lab in a residential high-rise." This appears to be an orphaned question separated from a multi-question fact pattern. A standalone question must provide the necessary facts.
check 5: pass
check 6: pass
check 7: pass
check 8: pass
Recommended fix: Integrate the missing fact pattern into the stem (e.g., "Arthur and Brenda set up an illicit chemical lab in a residential high-rise. Arthur instructed Brenda to use 'no flammable agents,' but a fire nonetheless occurred. Assume Arthur is charged...").
-->
