# Fix Guidance for q04

The QA pipeline flagged this question. Rewrite `q04.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q4.** Assume Sloane is charged with manslaughter under the Model Penal Code for Chloe's overdose death. Which of the following is the most likely outcome?

(a) Guilty, because she consciously disregarded a substantial and unjustifiable risk that the heavily concentrated fentanyl batch would cause fatal overdoses among the drug network's standard customer base. <!-- correct -->
(b) Not guilty, because she was acting under Deacon's direct operational orders, which effectively negates the voluntariness of her actions under the Model Penal Code's hierarchical liability framework.
(c) Guilty, because any reasonable professional chemist in her position would have known the grave danger, which is sufficient to establish strict liability for the resulting unintentional homicide.
(d) Not guilty, because her explicit warning to Deacon legally transferred the duty of care and severed her subjective liability for the ultimate distribution of the lethal drug product.
(e) Guilty, because her failure to exercise ordinary caution in manufacturing the drugs constituted a gross deviation from the standard of care that a reasonable person would observe.

**Answer:** (a)

**Explanation:** (a) is correct. The MPC defines manslaughter as a reckless killing. Recklessness requires subjective awareness—that the actor consciously disregarded a substantial and unjustifiable risk. Sloane's explicit warning to Deacon demonstrates she possessed actual awareness of the fatal risk. (b) is wrong because following orders does not negate the voluntariness of an act. (c) is wrong because the MPC rejects strict liability for manslaughter. (d) is wrong because warning a co-conspirator does not legally transfer a duty of care or sever liability for one's own reckless contribution to a death. (e) is wrong because "gross deviation from the standard of care" without conscious awareness defines MPC negligent homicide, whereas Sloane was subjectively aware of the risk, making it manslaughter.

**Tags:** chapters: [13], topics: [mpc manslaughter, subjective awareness, recklessness], difficulty: easy, cognitive: application

**Grounding:** Chapter 13, mpc-manslaughter-negligent-homicide-split

<!-- audit: MUST FIX
<check 1>: pass (accurately applies MPC subjective recklessness standard for manslaughter).
<check 2>: pass (distractors rely on fabricated doctrines like "hierarchical liability framework" or misstate the MPC's rejection of strict liability for homicide).
<check 3>: pass (explanation perfectly tracks the MPC distinction between subjective recklessness and objective negligence).
<check 4>: MUST FIX. The stem completely lacks the factual scenario. It references "Sloane," "Chloe," and "Deacon," heavily concentrated fentanyl, and a warning, but none of these facts are actually provided in the prompt. Without the parent fact pattern, the question is unanswerable.
<check 5>: pass (explicitly specifies Model Penal Code).
<check 6>: pass.
<check 7>: pass (MPC manslaughter vs. negligent homicide split is properly grounded in Chapter 13).
<check 8>: pass (all options are roughly symmetrical in length and structure, ranging from 25 to 32 words).
Recommended fix: Integrate the required facts into the stem. For example: "Sloane, a chemist, manufactured a highly concentrated fentanyl batch under orders from Deacon, a drug distributor. Sloane explicitly warned Deacon that the batch was highly lethal, but Deacon distributed it anyway, leading to Chloe's fatal overdose. Assume Sloane is charged with manslaughter..."
-->
