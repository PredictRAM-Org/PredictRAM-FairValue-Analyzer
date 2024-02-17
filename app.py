import streamlit as st
import yfinance as yf

def calculate_fair_value(stock_symbol, pe_ratio, industry_pe_ratio):
    # Fetch stock data from Yahoo Finance
    stock_data = yf.download(stock_symbol, start="2023-01-01", end="2024-01-01")

    # Calculate fair value based on P/E ratio
    fair_value = stock_data['Close'].iloc[-1] * (pe_ratio / industry_pe_ratio)
    return fair_value

def main():
    st.title('Stock Valuation App')

    # Input parameters
    stock_symbol = st.text_input('Enter Stock Symbol (e.g., AAPL):')
    pe_ratio = st.number_input('Enter P/E Ratio:', min_value=0.1, step=0.1)
    industry_pe_ratio = st.number_input('Enter Industry Average P/E Ratio:', min_value=0.1, step=0.1)

    if st.button('Calculate Fair Value'):
        if not stock_symbol:
            st.warning('Please enter a valid stock symbol.')
        else:
            fair_value = calculate_fair_value(stock_symbol, pe_ratio, industry_pe_ratio)
            st.success(f'The estimated fair value of {stock_symbol} is ${fair_value:.2f}')

if __name__ == '__main__':
    main()
