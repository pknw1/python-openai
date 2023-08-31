import csv
import requests
from bs4 import BeautifulSoup
import re

# Define the URL(s) to scrape
urls = ['https://ai.pknw1.co.uk', 'https://web.pknw1.co.uk']

# Define the CSV file path
csv_file = 'scraped_data.csv'

# Open the CSV file in append mode and create a CSV writer
with open(csv_file, 'a', newline='') as f:
    writer = csv.writer(f)

    # Process each URL
    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Parse and extract the relevant data
        parsed_text = soup.get_text()  # Example: parsing text from a specific div
        cleansed_data = re.sub(r'\n', '', parsed_text)

        # Write the data to the CSV file
        writer.writerow([url, cleansed_data])

print(f"Scraped data has been saved to {csv_file}")
