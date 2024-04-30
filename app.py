import streamlit as st
from fredapi import Fred
from datetime import datetime
import plotly.graph_objects as go
import pandas as pd

st.set_page_config(layout="wide")

# Your FRED API Key
fred_api_key = st.secrets["FRED_API"]
fred = Fred(api_key=fred_api_key)

def main():
    st.title('FRED Data Explorer')

    # Date range picker
    start_date, end_date = st.sidebar.date_input(
        "Select Date Range",
        value=[datetime(2000, 1, 1), datetime.today()],
        min_value=datetime(2000, 1, 1),
        max_value=datetime.today()
    )
    # Format dates as strings
    start_date_str = start_date.strftime('%Y-%m-%d')
    end_date_str = end_date.strftime('%Y-%m-%d')

    t1, t2, t3, t4, t5, t6 = st.tabs(["Labor Market","Consumer Behavior & Inflation", "Industrial & Production", "Financial Conditions & Credit", "Economic Health & Outlook", "Market Trends & Valuation"])

    with t1:
        # Fetch the data
        labor_market(start_date, end_date)

    with t2:
        consumer_behavior(start_date, end_date)
    
    with t3:
        industrial_production(start_date, end_date)

    with t4:
        financial_conditions(start_date, end_date)
    
    with t5:
        economic_health(start_date, end_date)
    
    with t6:
        market_trends(start_date, end_date)

def labor_market(start_date, end_date):
    total_nonfarm_employees = fred.get_series('PAYEMS', observation_start=start_date, observation_end=end_date)
    employment_level = fred.get_series('CE16OV', observation_start=start_date, observation_end=end_date)
    job_postings_in_us = fred.get_series('IHLIDXUS', observation_start=start_date, observation_end=end_date)
    wage_growth_tracker = fred.get_series('FRBATLWGT12MMUMHWGJST', observation_start=start_date, observation_end=end_date)
    job_switcher = fred.get_series('FRBATLWGT3MMAUMHWGJMJSW', observation_start=start_date, observation_end=end_date)
    
    st.markdown("All Employees, Total Nonfarm (Thousands of Persons, Seasonally Adjusted)")
    st.line_chart(total_nonfarm_employees)
    st.markdown("Employment Level (Thousands of Persons, Seasonally Adjusted)")
    st.line_chart(employment_level)
    st.markdown("Job Postings on Indeed in the United States (Index Feb, 1 2020=100, Seasonally Adjusted)")
    st.line_chart(job_postings_in_us)
    st.markdown("12-Month Moving Average of Unweighted Median Hourly Wage Growth: Job Stayer (Percent Change from Year Ago, Not Seasonally Adjusted)")
    st.line_chart(wage_growth_tracker)
    st.markdown("3-Month Moving Average of Unweighted Median Hourly Wage Growth: Job Switcher (Percent Change from Year Ago, Not Seasonally Adjusted)")
    st.line_chart(job_switcher)       

def consumer_behavior(start_date, end_date):
    personal_consumption_expenditures = fred.get_series('PCEC96', observation_start=start_date, observation_end=end_date)
    commercial_bank_credit = fred.get_series('CCLACBW027SBOG', observation_start=start_date, observation_end=end_date)
    real_disposable_personal_income = fred.get_series('W875RX1', observation_start=start_date, observation_end=end_date)
    real_manufacturing_and_trade_industries_sales = fred.get_series('CMRMTSPL', observation_start=start_date, observation_end=end_date)
    retail_sales_restaurants_and_other_eating_places = fred.get_series('MRTSSM7225USN', observation_start=start_date, observation_end=end_date)

    st.markdown("Real Personal Consumption Expenditures (Billions of Chained 2017 Dollars, Seasonally Adjusted Annual Rate)")
    st.line_chart(personal_consumption_expenditures)
    st.markdown("Consumer Loans: Credit Cards and Other Revolving Plans, All Commercial Banks (Billions of U.S. Dollars, Seasonally Adjusted)")
    st.line_chart(commercial_bank_credit)
    st.markdown("Real personal income excluding current transfer receipts (Billions of Chained 2017 Dollars, Seasonally Adjusted Annual Rate)")
    st.line_chart(real_disposable_personal_income)
    st.markdown("Real Manufacturing and Trade Industries Sales (Millions of Chained 2017 Dollars, Seasonally Adjusted)")
    st.line_chart(real_manufacturing_and_trade_industries_sales) 
    st.markdown("Retail Sales: Food Services and Drinking Places (Millions of U.S. Dollars, Seasonally Adjusted)")
    st.line_chart(retail_sales_restaurants_and_other_eating_places)


def industrial_production(start_date, end_date):
    industrial_production = fred.get_series('INDPRO', observation_start=start_date, observation_end=end_date)
    manufacturing_production = fred.get_series('IPMAN', observation_start=start_date, observation_end=end_date)

    st.markdown("Industrial Production: Total Index (Index 2017=100, Seasonally Adjusted)")
    st.line_chart(industrial_production)
    st.markdown("Index 2017=100, Seasonally Adjusted")
    st.line_chart(manufacturing_production)

def financial_conditions(start_date, end_date):
    nfc_index = fred.get_series('NFCI', observation_start=start_date, observation_end=end_date)
    drtscilm_index = fred.get_series('DRTSCILM', observation_start=start_date, observation_end=end_date)
    totbkcr_index = fred.get_series('TOTBKCR', observation_start=start_date, observation_end=end_date)

    st.markdown("Chicago Fed National Financial Conditions Index (Index, Not Seasonally Adjusted)")
    st.line_chart(nfc_index)
    st.markdown("Net Percentage of Domestic Banks Tightening Standards for Commercial and Industrial Loans to Large and Middle-Market Firms (Percent, Not Seasonally Adjusted)")
    st.line_chart(drtscilm_index)
    st.markdown("Bank Credit, All Commercial Banks (Billions of U.S. Dollars, Seasonally Adjusted)")
    st.line_chart(totbkcr_index)

    st.markdown("---")

    financial_conditions_credit_spreads = fred.get_series('BAA10Y', observation_start=start_date, observation_end=end_date)
    financial_conditions_leverage_ratio = fred.get_series('TLAACBW027NBOG', observation_start=start_date, observation_end=end_date)

    st.markdown("Moody's Seasoned Baa Corporate Bond Yield Relative to Yield on 10-Year Treasury Constant Maturity (Percent, Not Seasonally Adjusted)")
    st.line_chart(financial_conditions_credit_spreads)
    st.markdown("Total Assets, All Commercial Banks (Billions of U.S. Dollars, Not Seasonally Adjusted)")
    st.line_chart(financial_conditions_leverage_ratio)

def economic_health(start_date, end_date):
    walcl_series = fred.get_series('WALCL', observation_start=start_date, observation_end=end_date)
    sahmrealtime_series = fred.get_series('SAHMREALTIME', observation_start=start_date, observation_end=end_date)
    recprous_series = fred.get_series('RECPROUSM156N', observation_start=start_date, observation_end=end_date)
    bbkmleix_series = fred.get_series('BBKMLEIX', observation_start=start_date, observation_end=end_date)

    st.markdown("Assets: Total Assets: Total Assets (Less Eliminations from Consolidation): Wednesday Level (Millions of U.S. Dollars, Not Seasonally Adjusted)")
    st.line_chart(walcl_series)
    st.markdown("Real-time Sahm Rule Recession Indicator (Percentage Points, Seasonally Adjusted)")
    st.line_chart(sahmrealtime_series)
    st.markdown("Smoothed U.S. Recession Probabilities (Percent, Not Seasonally Adjusted)")
    st.line_chart(recprous_series)
    st.markdown("Brave-Butters-Kelley Leading Index (Standard Deviations, Seasonally Adjusted)")
    st.line_chart(bbkmleix_series)

    st.markdown("---")

    leading_index = fred.get_series('USSLIND', observation_start=start_date, observation_end=end_date)
    coincident_index = fred.get_series('USPHCI', observation_start=start_date, observation_end=end_date)
    lagging_index = fred.get_series('M16005USM358SNBR', observation_start=start_date, observation_end=end_date)

    st.markdown("Leading Index for the United States (Percent, Seasonally Adjusted)")
    st.line_chart(leading_index)
    st.markdown("Coincident Economic Activity Index for the United States (Index 2007=100, Seasonally Adjusted)")
    st.line_chart(coincident_index)
    st.markdown("Composite Index of Three Lagging Indicators, Amplitude-Adjusted, Weighted for United States (Index Jan 1948=100, Seasonally Adjusted)")
    st.line_chart(lagging_index)

def market_trends(start_date, end_date):
    sp500_index = fred.get_series('SP500', observation_start=start_date, observation_end=end_date)
    dow_jones_index = fred.get_series('DJIA', observation_start=start_date, observation_end=end_date)
    nasdaq_index = fred.get_series('NASDAQCOM', observation_start=start_date, observation_end=end_date)

    st.markdown("S&P 500 Index")
    st.line_chart(sp500_index)
    st.markdown("Dow Jones Index")
    st.line_chart(dow_jones_index)
    st.markdown("NASDAQ Index")
    st.line_chart(nasdaq_index)

    st.markdown("---")

    vix_index = fred.get_series('VIXCLS', observation_start=start_date, observation_end=end_date)

    st.markdown("VIX Index")
    st.line_chart(vix_index)

    # Yield curve plotting
    yield_curve_data = yield_curve(start_date, end_date)
    fig = go.Figure()
    for column in yield_curve_data.columns:
        fig.add_trace(go.Scatter(x=yield_curve_data.index, y=yield_curve_data[column], mode='lines', name=column))

    fig.update_layout(title='U.S. Treasury Yield Curve', xaxis_title='Date', yaxis_title='Yield (%)', yaxis=dict(autorange=True))
    st.plotly_chart(fig, use_container_width=True)

def yield_curve(start_date, end_date):
    data = {
        '3-Month': fred.get_series('TB3MS', observation_start=start_date, observation_end=end_date),
        '2-Year': fred.get_series('GS2', observation_start=start_date, observation_end=end_date),
        '5-Year': fred.get_series('GS5', observation_start=start_date, observation_end=end_date),
        '10-Year': fred.get_series('GS10', observation_start=start_date, observation_end=end_date)
    }
    return pd.DataFrame(data)

if __name__ == "__main__":
    main()
