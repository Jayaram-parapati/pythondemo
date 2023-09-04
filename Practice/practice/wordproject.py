import os
import docx2txt,re,requests
import pandas as pd

# Input folder containing Word files
input_folder = "c:\\Users\\anand.adapa\\Desktop\\resumes 50\\Resumes"

# Output folder for text files
output_folder = "c:\\Users\\anand.adapa\\Desktop\\text 50"
data = pd.DataFrame(columns=["Text"])
output_excel_file = "c:\\Users\\anand.adapa\\Desktop\\resumes 50\\textexcel.xlsx"

# # Label Studio project URL
# label_studio_url = "http://localhost:8080"  # Replace with your Label Studio URL

# project_name = "project1"  # Replace with your project name

# # API endpoint for creating tasks in Label Studio
# api_endpoint = f"{label_studio_url}/api/projects/{project_name}/tasks/"

# # Label Studio authentication token (if required)
# headers = {
#     "Authorization": "Token 8e13a14a9f3680cf1702be0bb629365a90129f7d"  # Replace with your authentication token (if required)
# }

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)



# Loop through each file in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".docx"):
        # Construct the full path of the input file
        input_file = os.path.join(input_folder, filename)

        # Extract text from the Word file
        text = docx2txt.process(input_file)

        text = re.sub(r'[^a-zA-Z0-9@]',' ',text)
        text = re.sub(r'\s+',' ',text)




        # Construct the full path of the output text file (with the same name)
        output_file = os.path.join(output_folder, filename.replace(".docx", ".txt"))

        # Save the extracted text as a text file
        with open(output_file, "w", encoding="utf-8") as text_file:
            text_file.write(text)

        data = data._append({"Text": text}, ignore_index=True)

        # task_data = {
        #     "data": {"text": text}
        # }

        # # Send a POST request to create the task in Label Studio
        # response = requests.post(api_endpoint, json=task_data, headers=headers)
        # print(response.status_code)

        # if response.status_code == 201:
        #     print(f"Task created for {filename}")
        # else:
        #     print(f"Failed to create task for {filename}")

    


# Save the DataFrame to an Excel file
data.to_excel(output_excel_file, index=False, engine='openpyxl')

          

print("Conversion completed.")
