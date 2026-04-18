import os
import subprocess

def create_test_md(filename, itemsep_val):
    content = f"""---
format:
  pdf:
    keep-tex: true
    geometry:
      - top=1in
      - bottom=1in
      - left=1.25in
      - right=1.25in
    include-in-header:
      text: |
        \\usepackage{{enumitem}}
        \\setlist{{{itemsep_val}}}
        \\def\\tightlist{{}}
---
### Test Question with {itemsep_val} spacing

**Q1.** This is a test question. What is the correct answer?

a. This is option A. It should be spaced according to the settings.
b. This is option B. It should be spaced according to the settings.
c. This is option C. It should be spaced according to the settings.
d. This is option D. It should be spaced according to the settings.
e. This is option E. It should be spaced according to the settings.

"""
    with open(filename, "w") as f:
        f.write(content)

def main():
    print("Building harness...")
    create_test_md("test_spacing_nosep.md", "nosep")
    create_test_md("test_spacing_0_5.md", "itemsep=0.5em")
    create_test_md("test_spacing_2_0.md", "itemsep=2.0em")

    print("Rendering PDFs...")
    subprocess.run(["quarto", "render", "test_spacing_nosep.md", "--to", "pdf"])
    subprocess.run(["quarto", "render", "test_spacing_0_5.md", "--to", "pdf"])
    subprocess.run(["quarto", "render", "test_spacing_2_0.md", "--to", "pdf"])
    print("Done!")

if __name__ == "__main__":
    main()
