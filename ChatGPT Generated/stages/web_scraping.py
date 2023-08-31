import requests
from bs4 import BeautifulSoup
import json

# Define the URL(s) to scrape
urls = ['https://ai.pknw1.co.uk', 'https://web.pknw1.co.uk']

# Loop through each URL and scrape the content
for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    #print(soup.get_text())
    scraped_data=url

    with open('scraped_data.json', 'w') as f:
      json.dump(scraped_data, f)