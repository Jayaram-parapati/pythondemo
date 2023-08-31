import PyPDF2
import glob
import requests

def pdf_to_text(pdf_path):
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ''
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return text

# def send_to_label_studio(text):
#     label_studio_url = "http://localhost:8080/"  # Replace with your Label Studio server URL
    
#     # Prepare the data payload
#     data = {
#         "data": text
#     }
    
#     # Send POST request to Label Studio
#     response = requests.post(f"{label_studio_url}/api/tasks", json=data)
#     return response.json()

pdf_files = glob.glob('c:\\Users\\anand.adapa\\Desktop\\resumes 50\\*.pdf')

for pdf_path in pdf_files:
    extracted_text = pdf_to_text(pdf_path)
    # response = send_to_label_studio(extracted_text)
    # print(f"Text from {pdf_path} sent to Label Studio. Task ID: {response['id']}")
    # print(response)
        # Get the name of the PDF file (without the extension)
    pdf_filename = pdf_path.split('/')[-1].split('.')[0]
    print(pdf_path)
    print(pdf_filename)
    # Create a new text file and save the extracted text
    # text_file_path = f'path_to_text_output/{pdf_filename}.txt'
    # with open(text_file_path, 'w') as text_file:
    #     text_file.write(extracted_text)
    
    # print(f"Text from {pdf_path} saved to {text_file_path}")