import streamlit as st
import requests
import pandas as pd

def fetch_data(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    
    with requests.Session() as session:
        session.headers.update(headers)
        response = session.get(url, allow_redirects=True)

        if response.status_code == 200:
            return response.json()  # Return JSON data
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
            print(f"Response: {response.text}")
            return None

def process_data(data):
    df = pd.DataFrame(data['priceIndexData'])
    df['Date'] = df['x'].apply(lambda x: x['value'])
    df['Mean'] = df['y'].apply(lambda x: x['mean']['value'])
    df = df[['Date', 'Mean']]
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    return df

# URL to download data from
url = 'https://www.chrono24.com/api/priceindex/performance-chart.json?type=rolex&period=max'

# Download the content from the URL
downloaded_content = fetch_data(url)

if downloaded_content:
    df = process_data(downloaded_content)
    st.title('Rolex Value Over Time')
    st.line_chart(df['Mean'])

