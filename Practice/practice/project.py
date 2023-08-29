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

def send_to_label_studio(text):
    label_studio_url = "http://localhost:8080"  # Replace with your Label Studio server URL
    
    # Prepare the data payload
    data = {
        "data": text
    }
    
    # Send POST request to Label Studio
    response = requests.post(f"{label_studio_url}/api/tasks", json=data)
    return response.json()

pdf_files = glob.glob('c:\\Users\\anand.adapa\\Downloads\\archive\\data\\data\\ACCOUNTANT\\*.pdf')

# for pdf_path in pdf_files:
#     extracted_text = pdf_to_text(pdf_path)
#     response = send_to_label_studio(extracted_text)
#     print(f"Text from {pdf_path} sent to Label Studio. Task ID: {response['id']}")
#     print(response)


# for pdf_path in pdf_files:
pdf_path = "c:\\Users\\anand.adapa\\Downloads\\archive\\data\\data\\ACCOUNTANT\\98559931.pdf"
extracted_text = pdf_to_text(pdf_path)
response = send_to_label_studio(extracted_text)
print(f"Text from {pdf_path} sent to Label Studio. Task ID: {response['id']}")
print(response)