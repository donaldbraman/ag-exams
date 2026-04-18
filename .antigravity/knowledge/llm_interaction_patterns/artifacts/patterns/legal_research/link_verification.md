# Legal Link Verification Strategy

Standard web scraping tools and direct HTTP requests (`GET`) often fail when verifying legal authorities from sources like Google Scholar due to aggressive rate limiting (429) and bot protection.

## Verification Patterns

To verify links produced by the research pipeline without triggering blocks:

### 1. Pattern Matching (Scholar Citations)
Instead of fetching the page, use regex or structural analysis to verify the URL contains a valid Case ID or Citation format.
- **Pattern**: `https://scholar.google.com/scholar_case?case=\d+`
- **Logic**: If the model provides a numeric case ID, it is highly likely it retrieved it from a real search result rather than hallucinating a structured URL.

### 2. Search Grounding Verification
Use Gemini's `web_search` tool (Grounding) as a "polite" proxy. 
- **Method**: Provide the generated URL to a verification agent.
- **Instruction**: "Check if the following URL refers to a case about [Topic]. Do not fetch the URL; use your search tools to confirm the existence of this authority."
- **Benefit**: The model uses Google's internal search grounding to confirm the snippet and citation, avoiding direct traffic to the source site.

### 3. Structural Validation
Verify that the domain matches the expected type:
- `law.justia.com`
- `courtlistener.com`
- `caselaw.findlaw.com`
- `legislature.[state].gov`

## Project Context: `verify_links.py`
In the Antigravity ecosystem, link auditing scripts (e.g., `scripts/verify_links.py`) typically use a mix of these strategies:
1. **Accessibility**: Basic `HEAD` request to check if the URL is active (where permitted).
2. **Relevance**: Matching the citation in the URL path (e.g., "State-v-Lisa") against the JSON metadata.
3. **Scholar Logic**: Specifically flagging Scholar links for manual verification if they don't meet the `case=\d+` pattern.
