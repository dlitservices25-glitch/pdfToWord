import fitz

def extract_text(pdf_path):
    doc = fitz.open(pdf_path)

    pages = []

    for page in doc:
        blocks = page.get_text("blocks")

        page_content = []

        for block in blocks:
            text = block[4].strip()

            if text:
                page_content.append(text)

        pages.append(page_content)

    return pages