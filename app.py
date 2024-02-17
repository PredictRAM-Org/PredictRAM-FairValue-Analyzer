import streamlit as st
import yfinance as yf

def fetch_stock_info(stock_symbol):
    # Fetch general information about the stock from Yahoo Finance
    stock_info = yf.Ticker(stock_symbol)
    return stock_info

def calculate_fair_value(stock_symbol, pe_ratio, ps_ratio, pb_ratio, current_price):
    # Calculate fair value based on user-provided ratios
    fair_value_pe = current_price * pe_ratio
    fair_value_ps = current_price * ps_ratio
    fair_value_pb = current_price * pb_ratio

    return fair_value_pe, fair_value_ps, fair_value_pb

def main():
    st.title('Stock Valuation App')

    # Input parameters
    stock_symbol = st.text_input('Enter Stock Symbol (e.g., AAPL):')
    expected_pe_ratio = st.number_input('Enter Expected P/E Ratio:', min_value=0.1, step=0.1)
    expected_ps_ratio = st.number_input('Enter Expected P/S Ratio:', min_value=0.1, step=0.1)
    expected_pb_ratio = st.number_input('Enter Expected P/B Ratio:', min_value=0.1, step=0.1)

    if st.button('Fetch Data and Calculate Fair Value'):
        if not stock_symbol:
            st.warning('Please enter a valid stock symbol.')
        else:
            # Fetch general information about the stock
            stock_info = fetch_stock_info(stock_symbol)

            # Get the current stock price
            current_price = stock_info.history(period='1d')['Close'].iloc[-1]

            # Calculate fair value based on user-provided ratios
            fair_value_pe, fair_value_ps, fair_value_pb = calculate_fair_value(
                stock_symbol, expected_pe_ratio, expected_ps_ratio, expected_pb_ratio, current_price
            )

            # Display the results
            st.subheader('Current Stock Price:')
            st.write(f'${current_price:.2f}')

            st.subheader('Fair Values:')
            st.write(f'Fair Value (P/E): ${fair_value_pe:.2f}')
            st.write(f'Fair Value (P/S): ${fair_value_ps:.2f}')
            st.write(f'Fair Value (P/B): ${fair_value_pb:.2f}')

if __name__ == '__main__':
    main()
