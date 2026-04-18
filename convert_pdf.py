import fitz
doc = fitz.open('criminal-law/quiz-system/research/final-exam/master_exam.pdf')
for i in range(min(3, len(doc))):
    page = doc.load_page(i)
    pix = page.get_pixmap(dpi=150)
    pix.save(f'/Users/donaldbraman/.gemini/antigravity/brain/245cd57a-3eb6-4b01-8279-05ee40caa264/page_{i+1}.png')
print("Saved pages!")
