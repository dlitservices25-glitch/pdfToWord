from docling.document_converter import DocumentConverter

def extract_with_docling(pdf_path):

    converter = DocumentConverter()

    result = converter.convert(pdf_path)

    markdown = result.document.export_to_markdown()

    return markdown