import os
import pandas as pd

# Specify the folder containing the text files
text_folder = 'output_texts'

# Create an empty DataFrame to store the text data
text_data = pd.DataFrame(columns=['Filename', 'Text'])

# Iterate through text files in the folder
for filename in os.listdir(text_folder):
    if filename.endswith('.txt'):
        text_filepath = os.path.join(text_folder, filename)
        
        # Read the text from the text file
        with open(text_filepath, 'r', encoding='utf-8') as text_file:
            text = text_file.read()
        
        # Append the filename and text to the DataFrame
        text_data = text_data.append({'Filename': filename, 'Text': text}, ignore_index=True)

# Specify the Excel file where you want to save the data
excel_filename = 'text_data.xlsx'

# Save the DataFrame to an Excel file
text_data.to_excel(excel_filename, index=False)

print(f"Text data has been saved to {excel_filename}")
