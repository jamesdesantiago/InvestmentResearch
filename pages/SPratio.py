import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the page containing the market statistics
url = "https://www.multpl.com/s-p-500-pe-ratio/table/by-month"

def fetch_data(url):
    """Fetch and parse HTML data from the given URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for request success
        return response.text
    except requests.RequestException as e:
        st.error(f"Failed to fetch data: {e}")
        return None

def parse_tables(html_content):
    """Parse HTML tables into pandas DataFrames."""
    soup = BeautifulSoup(html_content, 'html.parser')
    tables = soup.find_all('table', id='datatable')
    dataframes = [pd.read_html(str(table))[0] for table in tables if table]
    return dataframes

def main():
    st.title("S&P 500 PE Ratio by Month")

    html_content = fetch_data(url)
    if html_content:
        dataframes = parse_tables(html_content)
        
        if dataframes:
            df = dataframes[0]
            # Convert 'Date' column to datetime type
            #df['Date'] = pd.to_datetime(df['Date'])
            st.line_chart(dataframes[0].set_index('Date')['Value'])

if __name__ == "__main__":
    main()
