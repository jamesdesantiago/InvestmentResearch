import streamlit as st
import pandas as pd
import requests

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
    try:
        # Check for different data structures and process accordingly
        if 'instruments' in data['data']:
            return pd.json_normalize(data['data']['instruments'])
        elif 'instrumentSets' in data['data']:
            # Create an empty DataFrame to store the combined data
            combined_df = pd.DataFrame()
            # Iterate through each set of instruments for different markets
            for set_ in data['data']['instrumentSets']:
                # Extract the market name from headerFields
                market_name = [field['label'] for field in set_['headerFields'] if field['value'] == 'name'][0]

                # Convert the instruments to DataFrame
                instruments_df = pd.DataFrame(set_['instruments'])

                # Add a column for the market name
                instruments_df['Market'] = market_name

                # Append this market's data to the combined DataFrame
                combined_df = pd.concat([combined_df, instruments_df], ignore_index=True)
                return combined_df
        elif 'indexes' in data['data']:
            return pd.json_normalize(data['data']['indexes'])
        else:
            print("No recognized data structure found in JSON.")
            return pd.DataFrame()
    except KeyError as e:
        print(f"Key error: {e} - Check the JSON structure")
        return pd.DataFrame()

def run_data_pull(url):
    json_data = fetch_data(url)
    df = process_data(json_data)
    return df

# URLs with different query parameters
urls = [
    "https://www.wsj.com/market-data/stocks/marketsdiary?id=%7B%22application%22%3A%22WSJ%22%2C%22marketsDiaryType%22%3A%22diaries%22%7D&type=mdc_marketsdiary",
    "https://www.wsj.com/market-data/stocks/marketsdiary?id=%7B%22application%22%3A%22WSJ%22%2C%22marketsDiaryType%22%3A%22breakdownOfVolumes%22%7D&type=mdc_marketsdiary",
    "https://www.wsj.com/market-data/stocks/marketsdiary?id=%7B%22application%22%3A%22WSJ%22%2C%22marketsDiaryType%22%3A%22weeklyTotals%22%7D&type=mdc_marketsdiary"
]

def main():
    st.title("WSJ Market Diary")
    url_diaries = run_data_pull(urls[0])
    url_breakdownOfVolumes = run_data_pull(urls[1])
    url_weeklyTotals = run_data_pull(urls[2])

    st.header("Diaries")
    st.dataframe(url_diaries)

    st.header("Breakdown of Volumes")
    st.dataframe(url_breakdownOfVolumes)
    
    st.header("Weekly Totals")
    st.dataframe(url_weeklyTotals)

if __name__ == "__main__":
    main()
