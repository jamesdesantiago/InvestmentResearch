import streamlit as st
import pandas as pd
import requests

def load_data(url):
    # Fetching the JSON data from the URL
    response = requests.get(url)
    # Assuming the JSON structure allows direct conversion to DataFrame
    data = pd.json_normalize(response.json())
    return data

def main():
    st.title("Market Data Viewer")
    # URL of the JSON data
    url = "https://www.wsj.com/market-data/stocks/marketsdiary?id=%7B%22application%22%3A%22WSJ%22%2C%22marketsDiaryType%22%3A%22diaries%22%7D&type=mdc_marketsdiary"
    
    if st.button("Load Data"):
        # Loading data
        data = load_data(url)
        # Displaying the DataFrame in Streamlit
        st.write(data)

if __name__ == "__main__":
    main()
