from PyPDF2 import PdfReader


def extract():
    # Example code to read a PDF file
    path = 'conto.pdf'
    pdf_reader = PdfReader(path);

    page_content = []

    for index, pdf_page in enumerate(pdf_reader.pages):
        page_content.append({
            'page' : str(index + 1),
            'data' : pdf_page.extract_text()
            });

    print(page_content)
    return page_content


def convert(data):
    # Convert the PdfReader data to a JSON-friendly format
    converted_data = []
    for item in data:
        converted_item = {
            "page": item["page"],
            "data": item["data"]
        }
        converted_data.append(converted_item)
    return converted_data