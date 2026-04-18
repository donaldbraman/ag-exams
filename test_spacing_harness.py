import os
import subprocess

def create_test_md(filename, itemsep_val):
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
        \\setlist{{itemsep={itemsep_val}, parsep=0em, topsep=0em, partopsep=0em}}
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
    create_test_md("test_spacing_0_0.md", "0.0em")
    create_test_md("test_spacing_0_25.md", "0.25em")
    create_test_md("test_spacing_1_0.md", "1.0em") # Add a 1.0em to really see the difference

    print("Rendering PDFs...")
    subprocess.run(["quarto", "render", "test_spacing_0_0.md", "--to", "pdf"])
    subprocess.run(["quarto", "render", "test_spacing_0_25.md", "--to", "pdf"])
    subprocess.run(["quarto", "render", "test_spacing_1_0.md", "--to", "pdf"])
    print("Done!")

if __name__ == "__main__":
    main()
