import fitz
import os

os.makedirs('pdf_pages', exist_ok=True)
doc = fitz.open('Election-Officers-Forms.pdf')
print(f"Total pages: {len(doc)}")

for i in range(len(doc)):
    page = doc[i]
    pix = page.get_pixmap(dpi=150)
    out_path = f"pdf_pages/page_{i+1:02d}.png"
    pix.save(out_path)
    print(f"Saved {out_path} ({pix.width}x{pix.height})")

print("All pages rendered successfully.")
