# Fix Guidance for q12

The QA pipeline flagged this question. Rewrite `q12.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q12.** Assume Carter is charged with destruction of evidence, an offense requiring the specific intent to destroy evidence of a crime. Can Carter successfully assert a mistake of fact defense?

(a) Yes, because Carter genuinely believed the boxes contained old tax records, which negates the specific intent required for the crime of destruction of evidence. <!-- correct -->
(b) Yes, because the mistake of fact defense applies strictly whenever a defendant lacks actual knowledge of the underlying federal investigation targeting their employer.
(c) No, because the doctrine of transferred intent imputes Vance's criminal purpose to Carter as soon as Carter took physical possession of the sealed boxes.
(d) No, because a mistake of fact must be objectively reasonable to serve as a defense, and failing to check the sealed boxes was inherently unreasonable.
(e) No, because destruction of evidence is a strict liability regulatory offense that does not permit a mistake of fact defense under any circumstances whatsoever.

**Answer:** (a)

**Explanation:** Destruction of evidence is a specific intent crime. A mistake of fact is a defense to a specific intent crime if it negates the required specific mens rea, regardless of whether the mistake is reasonable or unreasonable (as long as it is honest). Carter genuinely believed he was destroying old tax records, which completely negates the intent to destroy evidence of a crime (Fact 10). (a) is correct. (b) is wrong because the defense relies on negating the mens rea regarding the nature of the evidence, not merely proving ignorance of the broader federal investigation. (c) is wrong because transferred intent applies to intended harms against different victims (e.g., in homicide), not imputing a principal's mens rea to an innocent agent. (d) is wrong because an honest, even if unreasonable, mistake of fact is a valid defense to a specific intent crime. (e) is wrong because destruction of evidence requires specific intent and is not a strict liability offense.

**Tags:** chapters: [3], topics: [mistake-of-fact, specific-intent, mens-rea], difficulty: medium, cognitive: application

**Grounding:** Common law mistake of fact doctrine for specific intent crimes

<!-- audit: MUST FIX
Check 1: pass
Check 2: pass
Check 3: pass
Check 4: Fails. The stem completely lacks the factual scenario necessary to answer the question (e.g., who is Carter, what were the sealed boxes, who is Vance, what were the tax records). While this appears to be pulled from a macro fact pattern, as a standalone question it is unanswerable without assumptions beyond the stem.
Check 5: pass
Check 6: pass
Check 7: pass
Check 8: pass
Recommended fix: Integrate the missing facts into the question stem, e.g., "Assume Carter, who was given sealed boxes by Vance and genuinely believed they contained old tax records, is charged with destruction of evidence..."
-->
