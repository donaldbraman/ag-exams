# Casebook Build System

The casebook is built using Quarto, supporting multi-format output.

## Output Formats
- **HTML**: Searchable, responsive, and navigable web version.
- **PDF**: 8×10" format optimized for print.
- **EPUB**: Reflowable text for e-readers.

## Directory Structure
- `chapters/`: Contains `.qmd` individual chapter files.
- `assets/`: Custom SCSS, images, and styling resources.
- `sources/`: Input materials (PDFs, old lectures).
- `_output/`: Destination for generated formats.
- `scripts/`: Python scripts for DOCX conversion and revision agents.

## Core Commands (Make)
- `make build`: Build the container environment.
- `make preview`: Preview the HTML version locally.
- `make render`: Generate all output formats.
- `make convert`: Extract content from source DOCX to Quarto chapters.

## Configuration
The `_quarto.yml` file defines book metadata, output options, and cross-reference settings.
