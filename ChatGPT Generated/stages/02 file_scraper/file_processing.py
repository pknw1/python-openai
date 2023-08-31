import os
import csv
import re

# Define the directory path to scrape files from
directory_path = '/tmp/openai'

# Define the CSV file path
csv_file = '/output/scraped_data.csv'

# Open the CSV file in append mode and create a CSV writer
with open(csv_file, 'a', newline='') as f:
    writer = csv.writer(f)  

    # Process each file in the directory
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)

        # Read the file content
        with open(file_path, 'r') as file:
            file_content = file.read()
            cleansed_data = re.sub(r'\n', ' ', file_content)
            cleansed_data = re.sub(r'\t', ' ', cleansed_data)
            cleansed_data = re.sub(r'           ', ' ', cleansed_data)
            cleansed_data = re.sub(r'     ', ' ', cleansed_data)
            cleansed_data = re.sub(r'    ', ' ', cleansed_data)

        # Write the data to the CSV file
        writer.writerow([filename, cleansed_data])

print(f"Scraped data has been saved to {csv_file}")