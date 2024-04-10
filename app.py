import streamlit as st
from fredapi import Fred

# Your FRED API Key
fred_api_key = st.secrets["FRED_API"]
fred = Fred(api_key=fred_api_key)

def main():
    st.title('FRED Data Explorer')

    t1, t2, t3, t4, t5,t5 = st.tabs(["Labor Market","Consumer Behavior & Inflation", "Industrial & Production", "Financial Conditions & Credit", "Economic Health & Outlook", "Market Trends & Valuation"])

    with t1:
        # Fetch the data
        labor_market()

    with t2:
        consumer_behavior()
    
    with t3:
        industrial_production()

    with t4:
        financial_conditions()
    
    with t5:
        economic_health()
    
    with t6:
        market_trends()

def labor_market():
    total_nonfarm_employees = fred.get_series('PAYEMS')
    employment_level = fred.get_series('CE16OV')
    job_postings_in_us = fred.get_series('IHLIDXUS')
    wage_growth_tracker = fred.get_series('FRBATLWGT12MMUMHWGJST')
    
    st.line_chart(total_nonfarm_employees)
    st.line_chart(employment_level)
    st.line_chart(job_postings_in_us)
    st.line_chart(wage_growth_tracker)    

def consumer_behavior():
    personal_consumption_expenditures = fred.get_series('PCEC96')
    commercial_bank_credit = fred.get_series('CCLACBW027SBOG')
    real_disposable_personal_income = fred.get_series('W875RX1')
    retail_and_food_services_sales = fred.get_series('CMRMTSPL')

    st.line_chart(personal_consumption_expenditures)
    st.line_chart(commercial_bank_credit)
    st.line_chart(real_disposable_personal_income)
    st.line_chart(retail_and_food_services_sales) 

    st.markdown("---")

    consumer_sentiment = fred.get_series('UMCSENT')
    consumer_spending = fred.get_series('PCE')
    consumer_debt = fred.get_series('CMDEBT')
    consumer_credit = fred.get_series('TOTALSL')
    
    st.line_chart(consumer_sentiment)
    st.line_chart(consumer_spending)
    st.line_chart(consumer_debt)
    st.line_chart(consumer_credit) 

def industrial_production():
    industrial_production = fred.get_series('INDPRO')
    manufacturing_production = fred.get_series('IPMAN')
    durable_goods_production = fred.get_series('IPDG')
    non_durable_goods_production = fred.get_series('IPND')

    st.line_chart(industrial_production)
    st.line_chart(manufacturing_production)
    st.line_chart(durable_goods_production)
    st.line_chart(non_durable_goods_production)

def financial_conditions():
    nfc_index = fred.get_series('NFCI')
    drtscilm_index = fred.get_series('DRTSCILM')
    totbkcr_index = fred.get_series('TOTBKCR')

    st.line_chart(nfc_index)
    st.line_chart(drtscilm_index)
    st.line_chart(totbkcr_index)

    st.markdown("---")

    financial_conditions_index = fred.get_series('STLFSI')
    financial_stress_index = fred.get_series('STLFSI2')
    financial_conditions_credit_spreads = fred.get_series('BAA10Y')
    financial_conditions_leverage_ratio = fred.get_series('TLAACBW027NBOG')

    st.line_chart(financial_conditions_index)
    st.line_chart(financial_stress_index)
    st.line_chart(financial_conditions_credit_spreads)
    st.line_chart(financial_conditions_leverage_ratio)

def economic_health():
    walcl_series = fred.get_series('WALCL')
    sahmrealtime_series = fred.get_series('SAHMREALTIME')
    recprous_series = fred.get_series('RECPROUSM156N')
    bbkmleix_series = fred.get_series('BBKMLEIX')

    st.line_chart(walcl_series)
    st.line_chart(sahmrealtime_series)
    st.line_chart(recprous_series)
    st.line_chart(bbkmleix_series)

    st.markdown("---")

    leading_index = fred.get_series('USSLIND')
    coincident_index = fred.get_series('USCOIND')
    lagging_index = fred.get_series('USLGIND')
    leading_index_growth_rate = fred.get_series('USSLINDGROW')
    coincident_index_growth_rate = fred.get_series('USCOINDGROW')
    lagging_index_growth_rate = fred.get_series('USLGINDGROW')

    st.line_chart(leading_index)
    st.line_chart(coincident_index)
    st.line_chart(lagging_index)
    st.line_chart(leading_index_growth_rate)
    st.line_chart(coincident_index_growth_rate)
    st.line_chart(lagging_index_growth_rate)

def market_trends():
    sp500pe_ratio = fred.get_series('MULTPL/SP500_PE_RATIO_MONTH')
    sp500_index = fred.get_series('SP500')
    dow_jones_index = fred.get_series('DJIA')
    nasdaq_index = fred.get_series('NASDAQCOM')
    russell_index = fred.get_series('RUI')

    st.line_chart(sp500pe_ratio)
    st.line_chart(sp500_index)
    st.line_chart(dow_jones_index)
    st.line_chart(nasdaq_index)
    st.line_chart(russell_index)

    st.markdown("---")

    vix_index = fred.get_series('VIXCLS')
    treasury_yield_10y = fred.get_series('GS10')
    treasury_yield_2y = fred.get_series('GS2')
    treasury_yield_3m = fred.get_series('TB3MS')
    treasury_yield_5y = fred.get_series('GS5')

    st.line_chart(vix_index)
    st.line_chart(treasury_yield_10y)
    st.line_chart(treasury_yield_2y)
    st.line_chart(treasury_yield_3m)
    st.line_chart(treasury_yield_5y)

if __name__ == "__main__":
    main()
