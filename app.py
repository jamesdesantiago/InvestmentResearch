import streamlit as st
from fredapi import Fred

st.set_page_config(layout="wide")

# Your FRED API Key
fred_api_key = st.secrets["FRED_API"]
fred = Fred(api_key=fred_api_key)

def main():
    st.title('FRED Data Explorer')

    # Date range picker
    start_date, end_date = st.sidebar.date_input(
        "Select Date Range",
        value=[datetime(2020, 1, 1), datetime(2023, 1, 1)],
        min_value=datetime(2000, 1, 1),
        max_value=datetime.today()
    ).strftime('%Y-%m-%d')

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
    
    st.markdown("Total Nonfarm Employees")
    st.line_chart(total_nonfarm_employees)
    st.markdown("Employment Level")
    st.line_chart(employment_level)
    st.markdown("Job Postings in US")
    st.line_chart(job_postings_in_us)
    st.markdown("Wage Growth Tracker")
    st.line_chart(wage_growth_tracker)    

def consumer_behavior(start_date, end_date):
    personal_consumption_expenditures = fred.get_series('PCEC96', observation_start=start_date, observation_end=end_date)
    commercial_bank_credit = fred.get_series('CCLACBW027SBOG', observation_start=start_date, observation_end=end_date)
    real_disposable_personal_income = fred.get_series('W875RX1', observation_start=start_date, observation_end=end_date)
    retail_and_food_services_sales = fred.get_series('CMRMTSPL', observation_start=start_date, observation_end=end_date)

    st.markdown("Personal Consumption Expenditures")
    st.line_chart(personal_consumption_expenditures)
    st.markdown("Commercial Bank Credit")
    st.line_chart(commercial_bank_credit)
    st.markdown("Real Disposable Personal Income")
    st.line_chart(real_disposable_personal_income)
    st.markdown("Retail and Food Services Sales")
    st.line_chart(retail_and_food_services_sales) 


def industrial_production(start_date, end_date):
    industrial_production = fred.get_series('INDPRO', observation_start=start_date, observation_end=end_date)
    manufacturing_production = fred.get_series('IPMAN', observation_start=start_date, observation_end=end_date)

    st.markdown("Industrial Production")
    st.line_chart(industrial_production)
    st.markdown("Manufacturing Production")
    st.line_chart(manufacturing_production)

def financial_conditions(start_date, end_date):
    nfc_index = fred.get_series('NFCI', observation_start=start_date, observation_end=end_date)
    drtscilm_index = fred.get_series('DRTSCILM', observation_start=start_date, observation_end=end_date)
    totbkcr_index = fred.get_series('TOTBKCR', observation_start=start_date, observation_end=end_date)

    st.markdown("National Financial Conditions Index")
    st.line_chart(nfc_index)
    st.markdown("Delinquency Rate on All Loans")
    st.line_chart(drtscilm_index)
    st.markdown("Total Bank Credit")
    st.line_chart(totbkcr_index)

    st.markdown("---")

    financial_conditions_index = fred.get_series('STLFSI', observation_start=start_date, observation_end=end_date)
    financial_stress_index = fred.get_series('STLFSI2', observation_start=start_date, observation_end=end_date)
    financial_conditions_credit_spreads = fred.get_series('BAA10Y', observation_start=start_date, observation_end=end_date)
    financial_conditions_leverage_ratio = fred.get_series('TLAACBW027NBOG', observation_start=start_date, observation_end=end_date)

    st.markdown("Financial Conditions Index")
    st.line_chart(financial_conditions_index)
    st.markdown("Financial Stress Index")
    st.line_chart(financial_stress_index)
    st.markdown("Credit Spreads")
    st.line_chart(financial_conditions_credit_spreads)
    st.markdown("Leverage Ratio")
    st.line_chart(financial_conditions_leverage_ratio)

def economic_health(start_date, end_date):
    walcl_series = fred.get_series('WALCL', observation_start=start_date, observation_end=end_date)
    sahmrealtime_series = fred.get_series('SAHMREALTIME', observation_start=start_date, observation_end=end_date)
    recprous_series = fred.get_series('RECPROUSM156N', observation_start=start_date, observation_end=end_date)
    bbkmleix_series = fred.get_series('BBKMLEIX', observation_start=start_date, observation_end=end_date)

    st.markdown("Assets: Total Assets Held Outright by the Federal Reserve")
    st.line_chart(walcl_series)
    st.markdown("Recession Probability Index")
    st.line_chart(sahmrealtime_series)
    st.markdown("Recession Probability Index")
    st.line_chart(recprous_series)
    st.markdown("BBK Moody's Analytics Recession Indicator")
    st.line_chart(bbkmleix_series)

    st.markdown("---")

    leading_index = fred.get_series('USSLIND', observation_start=start_date, observation_end=end_date)
    coincident_index = fred.get_series('USPHCI', observation_start=start_date, observation_end=end_date)
    lagging_index = fred.get_series('M16005USM358SNBR', observation_start=start_date, observation_end=end_date)

    st.markdown("Leading Index")
    st.line_chart(leading_index)
    st.markdown("Coincident Index")
    st.line_chart(coincident_index)
    st.markdown("Lagging Index")
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
    treasury_yield_10y = fred.get_series('GS10', observation_start=start_date, observation_end=end_date)
    treasury_yield_2y = fred.get_series('GS2', observation_start=start_date, observation_end=end_date)
    treasury_yield_3m = fred.get_series('TB3MS', observation_start=start_date, observation_end=end_date)
    treasury_yield_5y = fred.get_series('GS5', observation_start=start_date, observation_end=end_date)

    st.markdown("VIX Index")
    st.line_chart(vix_index)
    st.markdown("10-Year Treasury Yield")
    st.line_chart(treasury_yield_10y)
    st.markdown("2-Year Treasury Yield")
    st.line_chart(treasury_yield_2y)
    st.markdown("3-Month Treasury Yield")
    st.line_chart(treasury_yield_3m)
    st.markdown("5-Year Treasury Yield")
    st.line_chart(treasury_yield_5y)

if __name__ == "__main__":
    main()
