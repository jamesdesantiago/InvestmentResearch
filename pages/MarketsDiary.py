import streamlit as st
import pandas as pd
import requests

def load_data(url):
    response = requests.get(url)
    
    # Check the status code of the response
    if response.status_code != 200:
        print("Failed to fetch data: Status code", response.status_code)
        print("Response body:", response.text)
        return None
    
    try:
        data = pd.json_normalize(response.json())
    except ValueError as e:
        print("Failed to decode JSON:", e)
        print("Response content:", response.text)
        return None
    
    return data

def main():
    st.title("Market Data Viewer")
    # URL of the JSON data
    url1 = "https://www.wsj.com/market-data/stocks/marketsdiary?id=%7B%22application%22%3A%22WSJ%22%2C%22marketsDiaryType%22%3A%22diaries%22%7D&type=mdc_marketsdiary"
    url2 = "https://www.wsj.com/market-data/stocks/marketsdiary?id=%7B%22application%22%3A%22WSJ%22%2C%22marketsDiaryType%22%3A%22breakdownOfVolumes%22%7D&type=mdc_marketsdiary"
    url3 = "https://www.wsj.com/market-data/stocks/marketsdiary?id=%7B%22application%22%3A%22WSJ%22%2C%22marketsDiaryType%22%3A%22weeklyTotals%22%7D&type=mdc_marketsdiary"
    
    if st.button("Load Data"):
        # Loading data
        data = load_data(url1)
        # Displaying the DataFrame in Streamlit
        st.write(data)

if __name__ == "__main__":
    main()
