import streamlit as st
from fredapi import Fred

# Your FRED API Key
fred_api_key = st.secrets["FRED_API"]
fred = Fred(api_key=fred_api_key)

def main():
    st.title('FRED Data Explorer')

    # User input for the FRED series ID
    series_id = st.text_input('Enter FRED Series ID:', 'GDP')

    if st.button('Fetch Data'):
        # Fetch the data
        data = fred.get_series(series_id)
        
        # Display the data
        st.line_chart(data)

if __name__ == "__main__":
    main()
