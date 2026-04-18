# Fix Guidance for q08

The QA pipeline flagged this question. Rewrite `q08.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

<!-- audit: MUST FIX -->

**Safety Block Triggered.** The previous version of this question was blocked by Gemini's safety filters as unsafe. Please rewrite the fact pattern to reduce the risk of unsafe content blocking.

Error: Model returned empty or blocked response.

## Issue 2 — edge-case

**Q8.** The government prosecutes Avon, the CEO, under the strict-liability warehouse health statute. Avon argues he was never at the warehouse and did not personally supervise the unpermitted storage. Under the *Park* doctrine (responsible corporate officer doctrine), is Avon criminally liable?

(a) Yes, because as the CEO who orchestrated the use of the warehouse for corporate illicit purposes, he stood in a responsible relation to the regulatory violation. <!-- correct -->
(b) Yes, because the doctrine imposes absolute vicarious liability on all corporate officers for any employee's criminal act, regardless of the officer's specific operational authority.
(c) No, because the doctrine requires the prosecution to prove that the corporate officer had actual, subjective knowledge of the specific missing permit for the warehouse.
(d) No, because the doctrine requires proof that the executive purposefully directed the subordinate to commit the specific regulatory infraction leading to the criminal charge.
(e) No, because Avon's lack of physical presence at the warehouse severs the causal chain between his corporate role and the specific regulatory violation at issue.

**Answer:** (a)

**Explanation:** The *Park* doctrine allows corporate officers to be convicted of strict-liability public welfare offenses if they stand in a "responsible relation" to the violation, meaning they had the authority to prevent or correct it. As CEO who explicitly agreed to use the warehouse for the drug lab, Avon had clear authority over the operation. (b) fails because the doctrine is not pure vicarious liability; it requires the officer to have a responsible relation and authority to prevent the harm. (c) and (d) fail because the doctrine specifically dispenses with the need for actual knowledge or purposeful direction. (e) fails because physical presence is irrelevant to corporate authority and the affirmative duty to exercise vigilance.

**Tags:** chapters: [11], topics: [Park doctrine, responsible corporate officer, strict liability], difficulty: medium, cognitive: application

**Grounding:** Chapter 11 (responsible-corporate-officer-dotterweich; park-doctrine-foresight-vigilance)

<!-- edge-case-audit: SHOULD FIX
1. Fact Pattern Booby Traps: pass
2. Cross-Doctrine Clashes: Fact 3 establishes that the public welfare statute is graded as a "strict-liability felony." Applying the *Park* doctrine (which dispenses with conventional mens rea) to a felony strongly clashes with the due process limits on public welfare offenses (e.g., *Morissette*, *Staples*), which generally restrict strict liability to misdemeanors with light penalties. Advanced students might argue *Park* cannot constitutionally apply here because courts would strike down a strict-liability felony or read a mens rea requirement into it.
3. Cross-Question Spoilers: pass
Recommended fix: Add a clarifying sentence to the question stem (e.g., "Assume the jurisdiction constitutionally permits the application of strict liability to this felony regulatory offense") or coordinate with the fact-pattern author to downgrade the charge in Fact 3 to a misdemeanor.
-->

## Issue 3 — argpass-opus

**Q8.** The government prosecutes Avon, the CEO, under the strict-liability warehouse health statute. Avon argues he was never at the warehouse and did not personally supervise the unpermitted storage. Under the *Park* doctrine (responsible corporate officer doctrine), is Avon criminally liable?

(a) Yes, because as the CEO who orchestrated the use of the warehouse for corporate illicit purposes, he stood in a responsible relation to the regulatory violation. <!-- correct -->
(b) Yes, because the doctrine imposes absolute vicarious liability on all corporate officers for any employee's criminal act, regardless of the officer's specific operational authority.
(c) No, because the doctrine requires the prosecution to prove that the corporate officer had actual, subjective knowledge of the specific missing permit for the warehouse.
(d) No, because the doctrine requires proof that the executive purposefully directed the subordinate to commit the specific regulatory infraction leading to the criminal charge.
(e) No, because Avon's lack of physical presence at the warehouse severs the causal chain between his corporate role and the specific regulatory violation at issue.

**Answer:** (a)

**Explanation:** The *Park* doctrine allows corporate officers to be convicted of strict-liability public welfare offenses if they stand in a "responsible relation" to the violation, meaning they had the authority to prevent or correct it. As CEO who explicitly agreed to use the warehouse for the drug lab, Avon had clear authority over the operation. (b) fails because the doctrine is not pure vicarious liability; it requires the officer to have a responsible relation and authority to prevent the harm. (c) and (d) fail because the doctrine specifically dispenses with the need for actual knowledge or purposeful direction. (e) fails because physical presence is irrelevant to corporate authority and the affirmative duty to exercise vigilance.

**Tags:** chapters: [11], topics: [Park doctrine, responsible corporate officer, strict liability], difficulty: medium, cognitive: application

**Grounding:** Chapter 11 (responsible-corporate-officer-dotterweich; park-doctrine-foresight-vigilance)

<!-- argument-pass: SHOULD FIX
(a) Argument-for: Under the *Park* doctrine, corporate officers can be held criminally liable for strict-liability public welfare offenses if they have a "responsible relation" to the violation. This means the officer had the authority to prevent or correct the violation, even without personal supervision. As CEO, Avon possessed the ultimate authority over corporate operations, fulfilling the responsible relation requirement. Furthermore, if he orchestrated the warehouse's use, this directly establishes his power to prevent the unpermitted storage.
(b) Argument-for: One could argue that because public welfare offenses are strict liability, the responsible corporate officer doctrine functionally operates as absolute vicarious liability. If an employee commits a criminal act within the scope of corporate operations, the CEO is strictly liable by virtue of their title. Thus, Avon is liable automatically due to his status as CEO, rendering his specific operational authority or personal involvement irrelevant to the strict-liability analysis.
(c) Argument-for: An argument could be made that criminal liability, even under the responsible corporate officer doctrine, requires some minimum mens rea to satisfy due process. One could contend that a CEO cannot be held liable for an omission unless they had actual, subjective knowledge of the specific missing permit. Since Avon did not supervise the storage and had no knowledge of the permit issue, he cannot be convicted.
(d) Argument-for: A student might argue that the *Park* doctrine still requires some affirmative act or purposeful direction to connect the executive to the crime, differentiating it from purely vicarious liability. In this view, a CEO is only liable if they purposefully directed the subordinate to commit the specific regulatory infraction. Because Avon merely lacked presence and didn't supervise, he did not purposefully direct the infraction and thus avoids liability.
(e) Argument-for: One could argue that causation requires some proximity to the offense. The *Park* doctrine holds officers liable for failing to prevent harm, but an officer who is entirely physically removed from a facility might lack the practical ability to exercise vigilance. Under this theory, Avon's total lack of physical presence at the warehouse severs the causal chain between his executive role and the local regulatory violation, precluding criminal liability.

Head-to-head: Option (a) accurately articulates the *Park* doctrine's "responsible relation" standard, correctly capturing that an officer with authority to prevent or correct a violation is liable regardless of personal supervision. Options (b), (c), (d), and (e) each fail because they make explicit, categorically false legal claims about the *Park* doctrine. Option (b) ignores the requirement for operational authority, while (c) and (d) improperly import mens rea requirements (subjective knowledge and purposeful direction) into a strict-liability framework. Option (e) incorrectly elevates physical presence to a legal requirement for causation. However, option (a) introduces facts ("orchestrated the use of the warehouse for corporate illicit purposes") not present in the standalone prompt, which could confuse a test-taker.

Falsifiable claim per distractor:
- (b): "absolute vicarious liability on all corporate officers... regardless of the officer's specific operational authority" — wrong because *Park* explicitly requires that the officer have a responsible relation and operational authority to prevent or correct the violation.
- (c): "requires the prosecution to prove that the corporate officer had actual, subjective knowledge" — wrong because the *Park* doctrine explicitly dispenses with the requirement of actual knowledge.
- (d): "requires proof that the executive purposefully directed the subordinate" — wrong because liability under *Park* can be based on an omission or failure to exercise vigilance without purposeful direction.
- (e): "lack of physical presence at the warehouse severs the causal chain" — wrong because physical presence is not a legal prerequisite; authority and responsibility establish the causal link regardless of geography.

Recommended fix: Remove the external facts from option (a) so it relies only on the prompt. Change (a) to: "Yes, because as the CEO with the authority to prevent or correct the unpermitted storage, he stood in a responsible relation to the regulatory violation."
-->
