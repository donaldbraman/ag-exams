# Review Summary — self_defense

**Iterations:** 3 of 3
**Converged:** NO — cap exhausted or early-stop
**Total Qs:** 12
**Flagged at end:** 7

## Per-Q Verdicts

| Q | Grounding | Audit | Edge Case | Sonnet argpass | Opus argpass |
|---|---|---|---|---|---|
| q01 | GROUNDED | MUST FIX | CLEAN | CLEAN | SHOULD FIX |
| q02 | GROUNDED | MISSING | CLEAN | MUST FIX | MUST FIX |
| q03 | GROUNDED | MUST FIX | CLEAN | CLEAN | SHOULD FIX |
| q04 | GROUNDED | MISSING | MUST FIX | CLEAN | CLEAN |
| q05 | GROUNDED | CLEAN | CLEAN | CLEAN | CLEAN |
| q06 | GROUNDED | MISSING | MUST FIX | CLEAN | CLEAN |
| q07 | GROUNDED | MISSING | CLEAN | CLEAN | CLEAN |
| q08 | GROUNDED | CLEAN | CLEAN | CLEAN | MUST FIX |
| q09 | GROUNDED | MISSING | CLEAN | CLEAN | CLEAN |
| q10 | GROUNDED | MUST FIX | CLEAN | CLEAN | CLEAN |
| q11 | GROUNDED | CLEAN | CLEAN | CLEAN | CLEAN |
| q12 | GROUNDED | MISSING | CLEAN | CLEAN | CLEAN |

## Flagged Qs (needs professor review)

### q01
- Flagged by: **audit**
- Flagged by: **argpass-opus**
- Full QA artifacts: `q01-grounded.md`, `q01-audit.md`, `q01-edge-case.md`, `q01-argpass-sonnet.md`, `q01-argpass-opus.md`

### q02
- Flagged by: **argpass-sonnet**
- Flagged by: **argpass-opus**
- Full QA artifacts: `q02-grounded.md`, `q02-audit.md`, `q02-edge-case.md`, `q02-argpass-sonnet.md`, `q02-argpass-opus.md`

### q03
- Flagged by: **audit**
- Flagged by: **argpass-opus**
- Full QA artifacts: `q03-grounded.md`, `q03-audit.md`, `q03-edge-case.md`, `q03-argpass-sonnet.md`, `q03-argpass-opus.md`

### q04
- Flagged by: **edge-case**
- Full QA artifacts: `q04-grounded.md`, `q04-audit.md`, `q04-edge-case.md`, `q04-argpass-sonnet.md`, `q04-argpass-opus.md`

### q06
- Flagged by: **edge-case**
- Full QA artifacts: `q06-grounded.md`, `q06-audit.md`, `q06-edge-case.md`, `q06-argpass-sonnet.md`, `q06-argpass-opus.md`

### q08
- Flagged by: **argpass-opus**
- Full QA artifacts: `q08-grounded.md`, `q08-audit.md`, `q08-edge-case.md`, `q08-argpass-sonnet.md`, `q08-argpass-opus.md`

### q10
- Flagged by: **audit**
- Full QA artifacts: `q10-grounded.md`, `q10-audit.md`, `q10-edge-case.md`, `q10-argpass-sonnet.md`, `q10-argpass-opus.md`

## Handicapped-Haiku Blind-Take (floor check)

```
Q1: a
Q2: c
Q3: b
Q4: c
Q5: c
Q6: d
Q7: a
Q8: c
Q9: b
Q10: e
Q11: c
Q12: c
```

Interpretation: Haiku (effort=low, no tools, single turn) should score in the 50-75% range on a well-calibrated exam. Scores above 85% suggest Qs may be too easy; scores below 40% suggest unfair or overly-subtle phrasing.