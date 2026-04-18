# Polite Legal Retrieval & Grounding Pattern

This document explains the strategy for "Polite Retrieval" of legal documents from the public internet, a pattern developed to solve the fragility and blocking issues associated with direct web scraping.

## 1. The Challenge (Scraping Blocks)
Legal repositories like Google Scholar, Westlaw, and LexisNexis employ aggressive anti-bot measures. Direct HTTP fetching (`web_fetch`) by LLM agents often triggers:
- **429 Too Many Requests**: Immediate IP blocks.
- **CAPTCHAs**: Which agents cannot solve.
- **Incomplete Content**: Heavy JavaScript rendering issues.

## 2. The Solution: Search Grounding vs. Scraping
Instead of attempting to "visit" and "scrape" a specific page, the system uses **Search Grounding**.

- **Mechanism**: The agent is provided ONLY with a `web_search` tool (or native Google Search grounding).
- **Process**:
    1.  The agent issues a highly specific query for the case name + citation + "full text".
    2.  The LLM leverages the search engine's indexed snippets and cached content.
    3.  **The "Polite" Part**: The LLM consumes the search engine's pre-processed data (which comes from Google's own polite, high-reputation crawlers) rather than hitting the source site directly.

## 3. Tool Specialization Rule
To prevent technical failures in the Google provider, the system enforces a strict tool separation:
- **Single Tool Responsibility**: An agent shall not mix search grounding (`web_search`) with low-level scraping (`web_fetch`) in a single step.
- **Rationale**: Mixing these tools often triggers a **400 INVALID_ARGUMENT** error in the Gemini API (e.g., "Tool use with function calling is unsupported"), as the model attempts to switch between internal grounding and external function calls ambiguously.

## 4. Extraction of Full Text
While snippets are enough for "Verification" and "Finder" stages, the "Editing" stage requires full text.
- **Strategy**: The `document-retriever` uses its search grounding to find a "Clean Repo" URL (often from CourtListener, Justia, or a State Supreme Court site).
- **Execution**: The model is instructed to extract the "Full Judicial Opinion" specifically, using the citations and identifiers it verified in previous steps. Because it is a high-capability model (Gemini 1.5 Pro/3.0), it can synthesize the full text from its grounding search result without requiring a fragile "scrape" of the raw HTML.

## 5. Summary of Benefits
- **Reliability**: Zero 429 blocks during production runs.
- **Efficiency**: No need for complex HTML parsing or CSS selector maintenance.
- **Pedagogical Fidelity**: Ensures the model uses "Court-Authorized" text rather than fragmented third-party summaries.
