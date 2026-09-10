from pypdf import PdfReader

reader = PdfReader("ELIB-FINAL-MANUSCRIPT.pdf")

for i, page in enumerate(reader.pages[:20]):
    page_text = page.extract_text()
    lines = page_text.strip().split("\n")

    meaningful_lines = [
        line for line in lines 
        if len(line.strip()) > 20 and "POLYTECHNIC" not in line.upper().replace(" "," ")
    ]
    
    preview = meaningful_lines[0] if meaningful_lines else "(mostly header/empty)"
    print(f"Page {i}: {preview}")