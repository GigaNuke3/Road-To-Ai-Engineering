from pypdf import PdfReader

reader = PdfReader("ELIB-FINAL-MANUSCRIPT.pdf")

for i, page in enumerate(reader.pages[:20]):
    page_text = page.extract_text()
    first_line = page_text.strip().split("\n")[0] if page_text.strip() else "(empty page)"
    print(f"Page {i}: {first_line}")