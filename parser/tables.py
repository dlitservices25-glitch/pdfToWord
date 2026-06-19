import camelot

def extract_tables(pdf_path):

    tables = camelot.read_pdf(
        pdf_path,
        pages="all",
        flavor="stream"  # try stream if this fails
    )

    output = []

    for table in tables:
        output.append(table.df.values.tolist())

    return output