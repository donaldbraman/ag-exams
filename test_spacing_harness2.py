import os
import subprocess

def create_test_md(filename, setlist_macro):
    content = f"""---
format:
  pdf:
    geometry:
      - top=1in
      - bottom=1in
      - left=1.25in
      - right=1.25in
    include-in-header:
      text: |
        \\usepackage{{enumitem}}
        {setlist_macro}
        \\def\\tightlist{{}}
---
### Test Question

**Q1.** This is a test question. What is the correct answer?

a. This is option A.
b. This is option B.
c. This is option C.
d. This is option D.
e. This is option E.

"""
    with open(filename, "w") as f:
        f.write(content)

def main():
    print("Building harness...")
    # Generate 0 spacing
    create_test_md("test_spacing_zero.md", "\\setlist{nosep}")
    # Generate 0.25 spacing
    create_test_md("test_spacing_quarter.md", "\\setlist{itemsep=0.25em, parsep=0em, topsep=0em, partopsep=0em}")

    print("Rendering PDFs...")
    subprocess.run(["quarto", "render", "test_spacing_zero.md", "--to", "pdf"])
    subprocess.run(["quarto", "render", "test_spacing_quarter.md", "--to", "pdf"])
    print("Done!")

if __name__ == "__main__":
    main()
