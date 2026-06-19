from pypdf import PdfReader

def extract_forms(pdf_path):
    reader = PdfReader(pdf_path)

    fields = reader.get_fields()

    if not fields:
        return {}

    output = {}

    for key, value in fields.items():
        output[key] = value.get("/V", "")

    return output