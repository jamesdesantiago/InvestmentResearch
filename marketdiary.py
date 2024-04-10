import requests
from bs4 import BeautifulSoup

# URL of the page
url = 'https://www.wsj.com/market-data/stocks/marketsdiary'

# Fetch the page
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find data (adjust selector based on actual data you're looking for)
    data = soup.find()  # Use soup.find_all() for multiple items
    
    # Process and print your data
    print(data.text)
else:
    print("Failed to fetch the page")
