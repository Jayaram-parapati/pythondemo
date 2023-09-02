import PyPDF2
import glob
import requests,re,os
import pandas as pd

def pdf_to_text(pdf_path):
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ''
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return text

# def send_to_label_studio(text):
 
#     user_id = '71eb6ea415a611e6d2a093acb600132af0a05fa7'
#     url = ''
#     headers ={
#         "Authorization":f"Bearer {user_id}",
#         "contenttype": "application/json"
#     }

#     response = requests.post(url,headers=headers)
#     return response.json()

df = pd.DataFrame(columns=["resumes_text"])

pdf_files = glob.glob('c:\\Users\\anand.adapa\\Desktop\\resumes 50\\*.pdf')

for pdf_path in pdf_files:
    extracted_text = pdf_to_text(pdf_path)
    # response = send_to_label_studio(extracted_text)
    # print(response.status_code)
    # print(extracted_text)
    formatted_text = re.sub(r'\s+|[^a-zA-Z0-9]',' ',extracted_text)
    formatted_text = re.sub(r'\s+',' ',formatted_text)
    # print(formatted_text)

    text_filename = pdf_path.split('.')[1].split('\\')[-1] + ".text"
    # print(text_filename)
    text_file_path = os.path.join("c:\\Users\\anand.adapa\\Desktop\\text 50",text_filename)
    # print(text_file_path)
    
    with open(text_file_path,'w',encoding='utf-8') as text_file:
        text_file.write(formatted_text)

    # df = df.append({"resumes_text" : formatted_text}, ignore_index = True)
    df    

print(df.to_string())

        


































  