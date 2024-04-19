import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the page containing the market statistics
url = "https://www.cboe.com/us/options/market_statistics/"

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
    tables = soup.find_all('table', class_='data-table')
    dataframes = [pd.read_html(str(table))[0] for table in tables if table]
    return dataframes

def main():
    st.title("CBOE Options Market Statistics")

    html_content = fetch_data(url)
    if html_content:
        dataframes = parse_tables(html_content)
        
        if dataframes:
            st.header("Total Options Volume")
            st.dataframe(dataframes[0])

            st.header("Index Options Volume")
            st.dataframe(dataframes[1])

            st.header("Equity Options Volume")
            st.dataframe(dataframes[2])

if __name__ == "__main__":
    main()
