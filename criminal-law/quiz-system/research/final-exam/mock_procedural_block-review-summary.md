# Review Summary — mock_procedural_block

**Iterations:** 2 of 5
**Converged:** NO — cap exhausted or early-stop
**Total Qs:** 14
**Flagged at end:** 14

## Per-Q Verdicts

| Q | Grounding | Audit | Edge Case | Sonnet argpass | Opus argpass |
|---|---|---|---|---|---|
| q01 | GROUNDED | MUST FIX | CLEAN | CLEAN | SHOULD FIX |
| q02 | GROUNDED | MUST FIX | CLEAN | CLEAN | CLEAN |
| q03 | GROUNDED | MUST FIX | CLEAN | CLEAN | SHOULD FIX |
| q04 | GROUNDED | MUST FIX | CLEAN | CLEAN | CLEAN |
| q05 | GROUNDED | SHOULD FIX | CLEAN | CLEAN | CLEAN |
| q06 | GROUNDED | MUST FIX | CLEAN | CLEAN | SHOULD FIX |
| q07 | GROUNDING-FAIL | MUST FIX | MUST FIX | CLEAN | CLEAN |
| q08 | GROUNDED | MUST FIX | CLEAN | CLEAN | SHOULD FIX |
| q09 | GROUNDED | MUST FIX | SHOULD FIX | CLEAN | SHOULD FIX |
| q10 | GROUNDING-FAIL | MUST FIX | CLEAN | CLEAN | CLEAN |
| q11 | GROUNDED | MUST FIX | MUST FIX | CLEAN | SHOULD FIX |
| q12 | GROUNDED | MUST FIX | CLEAN | CLEAN | SHOULD FIX |
| q13 | GROUNDING-FAIL | MUST FIX | CLEAN | CLEAN | CLEAN |
| q14 | GROUNDED | MUST FIX | CLEAN | CLEAN | MUST FIX |

## Flagged Qs (needs professor review)

### q01
- Flagged by: **audit**
- Flagged by: **argpass-opus**
- Full QA artifacts: `q01-grounded.md`, `q01-audit.md`, `q01-edge-case.md`, `q01-argpass-sonnet.md`, `q01-argpass-opus.md`

### q02
- Flagged by: **audit**
- Full QA artifacts: `q02-grounded.md`, `q02-audit.md`, `q02-edge-case.md`, `q02-argpass-sonnet.md`, `q02-argpass-opus.md`

### q03
- Flagged by: **audit**
- Flagged by: **argpass-opus**
- Full QA artifacts: `q03-grounded.md`, `q03-audit.md`, `q03-edge-case.md`, `q03-argpass-sonnet.md`, `q03-argpass-opus.md`

### q04
- Flagged by: **audit**
- Full QA artifacts: `q04-grounded.md`, `q04-audit.md`, `q04-edge-case.md`, `q04-argpass-sonnet.md`, `q04-argpass-opus.md`

### q05
- Flagged by: **audit**
- Full QA artifacts: `q05-grounded.md`, `q05-audit.md`, `q05-edge-case.md`, `q05-argpass-sonnet.md`, `q05-argpass-opus.md`

### q06
- Flagged by: **audit**
- Flagged by: **argpass-opus**
- Full QA artifacts: `q06-grounded.md`, `q06-audit.md`, `q06-edge-case.md`, `q06-argpass-sonnet.md`, `q06-argpass-opus.md`

### q07
- Flagged by: **grounding**
- Flagged by: **audit**
- Flagged by: **edge-case**
- Full QA artifacts: `q07-grounded.md`, `q07-audit.md`, `q07-edge-case.md`, `q07-argpass-sonnet.md`, `q07-argpass-opus.md`

### q08
- Flagged by: **audit**
- Flagged by: **argpass-opus**
- Full QA artifacts: `q08-grounded.md`, `q08-audit.md`, `q08-edge-case.md`, `q08-argpass-sonnet.md`, `q08-argpass-opus.md`

### q09
- Flagged by: **audit**
- Flagged by: **edge-case**
- Flagged by: **argpass-opus**
- Full QA artifacts: `q09-grounded.md`, `q09-audit.md`, `q09-edge-case.md`, `q09-argpass-sonnet.md`, `q09-argpass-opus.md`

### q10
- Flagged by: **grounding**
- Flagged by: **audit**
- Full QA artifacts: `q10-grounded.md`, `q10-audit.md`, `q10-edge-case.md`, `q10-argpass-sonnet.md`, `q10-argpass-opus.md`

### q11
- Flagged by: **audit**
- Flagged by: **edge-case**
- Flagged by: **argpass-opus**
- Full QA artifacts: `q11-grounded.md`, `q11-audit.md`, `q11-edge-case.md`, `q11-argpass-sonnet.md`, `q11-argpass-opus.md`

### q12
- Flagged by: **audit**
- Flagged by: **argpass-opus**
- Full QA artifacts: `q12-grounded.md`, `q12-audit.md`, `q12-edge-case.md`, `q12-argpass-sonnet.md`, `q12-argpass-opus.md`

### q13
- Flagged by: **grounding**
- Flagged by: **audit**
- Full QA artifacts: `q13-grounded.md`, `q13-audit.md`, `q13-edge-case.md`, `q13-argpass-sonnet.md`, `q13-argpass-opus.md`

### q14
- Flagged by: **audit**
- Flagged by: **argpass-opus**
- Full QA artifacts: `q14-grounded.md`, `q14-audit.md`, `q14-edge-case.md`, `q14-argpass-sonnet.md`, `q14-argpass-opus.md`

## Handicapped-Haiku Blind-Take (floor check)

```
Q1: d
Q2: a
Q3: a
Q4: c
Q5: b
Q6: a
Q7: b
Q8: a
Q9: c
Q10: a
Q11: d
Q12: a
Q13: c
Q14: b
```

Interpretation: Haiku (effort=low, no tools, single turn) should score in the 50-75% range on a well-calibrated exam. Scores above 85% suggest Qs may be too easy; scores below 40% suggest unfair or overly-subtle phrasing.