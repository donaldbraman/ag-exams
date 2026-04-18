# Fix Guidance for q08

The QA pipeline flagged this question. Rewrite `q08.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

Now that we've mapped the homicides, we need to secure the underlying drug, conspiracy, and attempt charges. We have financial evidence linking Sloane to the operation, and drug evidence from Trey's arrest. Analyze the conspiracy and accomplice liability for Sloane, attempt liability for Trey, and whether we can charge the whole network under RICO.

**Q8.** Assume Sloane is charged with conspiracy to distribute narcotics. Under the *Lauria* framework for establishing intent to agree, does her compensation structure establish the requisite mens rea?

(a) Yes, because receiving a percentage of the profits gives her a direct financial stake in the venture, supporting an inference that she purposed to promote the illegal enterprise. <!-- correct -->
(b) No, because as a subordinate drug chemist, she lacked the bilateral agreement with the street-level sellers that is strictly necessary to form a complete and valid wheel conspiracy.
(c) Yes, because providing specialized chemical manufacturing services to a known criminal operation constitutes strict liability participation in the ongoing conspiracy regardless of her subjective mental state.
(d) No, because knowledge of the criminal nature of the enterprise cannot be legally inferred solely from a profit-sharing arrangement without proof of an independent physical overt act.
(e) Yes, because under the unilateral approach to conspiracy, her individual subjective belief that she was participating in a localized crime is sufficient to satisfy the specific intent requirement.

**Answer:** (a)

**Explanation:** (a) is correct. *People v. Lauria* holds that while knowledge of illegal use alone is generally insufficient to prove a provider of goods/services purposed to join a conspiracy, that purpose can be inferred if the provider has a "stake in the venture." Receiving a 20% cut of the profits directly ties Sloane's financial success to the network's illegal sales, satisfying this inference. (b) is wrong because a chain conspiracy does not require every member to bilaterally agree with every other member. (c) is wrong because conspiracy is a specific intent crime; there is no strict liability participation. (d) is wrong because the profit-sharing arrangement proves the *intent to agree*, which is distinct from the overt act requirement. (e) is wrong because the unilateral approach eliminates the requirement that the *other* party genuinely agree, but the defendant must still possess the purpose to promote the crime.

**Tags:** chapters: [19], topics: [conspiracy, intent to agree, Lauria, stake in the venture], difficulty: medium, cognitive: application

**Grounding:** Chapter 19, lauria-stake-in-venture

<!-- audit: SHOULD FIX
Check 1: pass
Check 2: pass
Check 3: pass
Check 4: finding (The provided stem states there is "financial evidence linking Sloane to the operation" but does not specify that she receives a 20% cut of the profits, nor does it explicitly establish her role as a "subordinate drug chemist." Unless these exact facts are clearly established in the master fact pattern, the question requires assumptions beyond the stem.)
Check 5: pass
Check 6: pass
Check 7: pass
Check 8: pass
Recommended fix: Update the local stem to briefly anchor the relevant facts from the master fact pattern (e.g., "We have financial evidence showing Sloane, a chemist, received a 20% cut of the operation's profits...").
-->
