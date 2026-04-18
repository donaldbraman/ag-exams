# Criminal Law Casebook Overview

## Purpose
The `criminal-law` repository is dedicated to creating a modern, open-access criminal law casebook. It serves a dual purpose:
1. **Publication Platform**: Utilizing Quarto to generate professional-quality casebooks in HTML (searchable/web), PDF (print-optimized), and EPUB (e-reader) formats.
2. **AI-Driven Content Revision**: Implementing a **Gemini-optimized** revision pipeline to research, extract topics, and edit case law specifically for pedagogical use. This system uses a sequential "Generate -> Verify -> Refine" pattern.

## Project Structure
The repository is organized into two primary systems:
- **Casebook Build System**: Quarto-based publishing.
- **Revision Agent System**: A Google Gemini-based workflow orchestrated by the `multi` engine for generating and refining content.

## Status (Spring 2026)
As of early 2026, the project is active and being used for the Spring 2026 Criminal Law course at GW Law School. The project recently completed a major refactor (Jan 2026) to transition from a multi-model architecture to a streamlined Gemini-specific pipeline.

## Key Technologies
- **Quarto**: For document rendering and publishing.
- **Python (uv)**: For dependency management and scripting.
- **Google Gemini**: The primary LLM used for content research and editing (`gemini-3-flash-preview`).
- **Podman/Makefile**: For containerized development environment.
- **Sister Libraries**: Relies on `auth-utils` (authentication) and `multi` (workflow engine).
