# Fix Guidance for q12

The QA pipeline flagged this question. Rewrite `q12.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q12.** Assume Alex is charged with Blake's death. How does Dr. Davis's gross medical negligence (ignoring the bright red allergy bracelet to look at his phone) affect Alex's liability?

(a) It has no effect, because medical treatment provided to a gunshot victim is always considered a dependent intervening cause that cannot break the chain of proximate causation.
(b) It severs the causal chain, because the doctor's gross negligence in actively ignoring the medical warning bracelet was highly extraordinary and unforeseeable. <!-- correct -->
(c) It has no effect, because any negligence by a third party must be intentional or malicious in order to shield the original wrongdoer from homicide liability.
(d) It severs the causal chain, because any subsequent act by a medical professional automatically breaks proximate cause and shifts the legal blame to the treating physician.
(e) It has no effect, because a defendant takes their victim as they find them, including the victim's susceptibility to subsequent medical errors during emergency hospital treatment.

**Answer:** (b)

**Explanation:** The gross negligence severs the causal chain. While ordinary medical negligence is considered a foreseeable, dependent intervening cause that does not break proximate causation, gross medical negligence—such as a doctor deliberately ignoring a bright red allergy bracelet to look at a phone—is considered highly extraordinary and independent. This severs Alex's liability for the completed homicide. 
(a) fails because only ordinary medical negligence is dependent; gross negligence breaks the chain. 
(c) fails because gross, reckless negligence is sufficient to break the chain without requiring malicious intent. 
(d) fails because it incorrectly asserts that any medical act, even ordinary care, breaks the chain. 
(e) fails because the "eggshell skull" rule applies to pre-existing biological conditions, not subsequent extraordinary medical errors.

**Tags:** chapters: [8], topics: [causation, independent intervening cause, gross negligence], difficulty: medium, cognitive: application

**Grounding:** Chapter 8 (Proximate cause, medical gross negligence as independent intervening cause)

<!-- audit: MUST FIX
check 1: pass
check 2: pass
check 3: pass
check 4: FAIL. The stem lacks essential foundational facts. It never states what Alex did to Blake or why Blake is receiving medical treatment, forcing the student to reverse-engineer the "gunshot" scenario entirely from distractor (a). It also fails to explicitly state that the allergic reaction from the doctor's negligence is what actually killed Blake.
check 5: pass
check 6: pass
check 7: pass
Recommended fix: Revise the stem to establish the initial act and the actual cause of death. E.g., "Assume Alex shoots Blake, who is rushed to the hospital. There, Dr. Davis administers a medication that causes a fatal allergic reaction, killing Blake. If Dr. Davis's actions constituted gross medical negligence (ignoring a bright red allergy bracelet to look at his phone), how does this affect Alex's liability for the homicide?"
-->
