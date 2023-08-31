import csv
import numpy as np
import openai

# Define the CSV file path
csv_file = '/output/scraped_data.csv'

# Set up OpenAI API credentials
openai.api_key = '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'

# Open the CSV file in read mode and create a CSV reader
with open(csv_file, 'r') as f:
    reader = csv.reader(f)
    rows = list(reader)

# Remove the header row
header_row = rows[0]
data_rows = rows[1:]

# Define the column names for the embeddings CSV file
embeddings_header = ['index', 'source', 'embeddings']

# Initialize the list to store embeddings
embeddings_data = []

# Process each data row
for index, row in enumerate(data_rows):
    source = row[1]  # Assuming the URL or filename is stored at index 1

    # Assuming the tokenized chunks start from index 4
    tokens = [token for chunk in row[4:] for token in chunk]

    # Create embeddings for the tokens using OpenAI API
    response = openai.Embedding.create(model='text-davinci-003', tokens=tokens)
    embeddings = response['embeddings']

    embeddings_data.append([index, source, embeddings])

# Save the embeddings data to the CSV file
embeddings_csv_file = '/output/embeddings.csv'

with open(embeddings_csv_file, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(embeddings_header)
    writer.writerows(embeddings_data)

print(f"Embeddings have been generated and saved to {embeddings_csv_file}")
