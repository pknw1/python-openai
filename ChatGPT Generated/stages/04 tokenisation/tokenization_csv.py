import csv
import tiktoken

# Define the CSV file path
csv_file = '/output/scraped_data.csv'

# Open the CSV file in read mode and create a CSV reader
with open(csv_file, 'r') as f:
    reader = csv.reader(f)
    rows = list(reader)

# Process each row in the CSV file, excluding the header row
for row in rows[1:]:
    # Get the chunks from the row
    chunks = row[2:]  # Assuming the chunked data starts from index 3

    # Tokenize the chunks
    tokenize = tiktoken.get_encoding("cl100k_base")
    tokenized_chunks = [tokenize.encode(chunk) for chunk in chunks]

    # Store the tokenized chunks in the row
    row.extend(tokenized_chunks)

    # Store the number of tokens in an additional column
    row.append(sum(len(tokens) for tokens in tokenized_chunks))

# Write the updated rows to the CSV file
with open(csv_file, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(rows)

print(f"Data has been tokenized and updated in {csv_file}")
