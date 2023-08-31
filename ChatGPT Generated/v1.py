import os
import re
import textract
from bs4 import BeautifulSoup

def read_text_from_pdf(pdf_path):
    text = textract.process(pdf_path).decode("utf-8")
    return text

def read_text_from_html(html_path):
    with open(html_path, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")
        text = soup.get_text()
    return text

def read_files(directory):
    files_data = []
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        if file_name.endswith(".pdf"):
            text = read_text_from_pdf(file_path)
            files_data.append(text)
        elif file_name.endswith(".html"):
            text = read_text_from_html(file_path)
            files_data.append(text)
        # Add more conditions for other file formats if needed

    return files_data

# Provide the directory containing the files
directory = "path/to/your/files"

# Read and process the files
files_data = read_files(directory)

# Perform your desired queries on the files_data and return the most appropriate results
# Example: Find lines containing a specific keyword in all files
keyword = "example"
matching_lines = []
for data in files_data:
    lines = data.split("\n")
    matching_lines.extend([line for line in lines if re.search(r"\b{}\b".format(keyword), line, re.IGNORECASE)])

# Print the matching lines
for line in matching_lines:
    print(line)
