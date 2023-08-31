import csv

# Define the CSV file path
csv_file = '/output/scraped_data.csv'

# Define the chunk size
chunk_size = 50

# Open the CSV file in read mode and create a CSV reader
with open(csv_file, 'r') as f:
    reader = csv.reader(f)
    rows = list(reader)

# Process each row in the CSV file, excluding the header row
for row in rows[1:]:
    # Get the parsed text from the row
    parsed_text = row[1]  # Assuming the parsed text column is at index 2

    # Chunk the parsed text
    chunks = [parsed_text[i:i + chunk_size] for i in range(0, len(parsed_text), chunk_size)]

    # Add the chunked data as an additional column in the row
    row.append(chunks)

# Write the updated rows to the CSV file
with open(csv_file, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(rows)

print(f"Data has been chunked and updated in {csv_file}")
