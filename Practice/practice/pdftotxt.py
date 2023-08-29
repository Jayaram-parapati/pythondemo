import PyPDF2

def pdf_to_text(pdf_path):
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        text = ''
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            text += page.extractText()
    return text

# Provide the path to your PDF file
pdf_path = 'path_to_your_pdf_file.pdf'
extracted_text = pdf_to_text(pdf_path)

print(extracted_text)
