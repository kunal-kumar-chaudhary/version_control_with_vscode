import streamlit as st 
import yfinance as yf  # yahoo finance API
import pandas as pd 
st.write("""
# simple stock price app

shown are the stock **closing price** and ***volume*** of google!
"""
)


# define the ticker symbol
tickerSymbol = 'GOOGL'


# get data on this ticker symbol
tickerData = yf.Ticker(tickerSymbol)
# get the historical prices for this ticker
tickerDF = tickerData.history(period='1d', start='2015-5-31', end='2020-5-31')
# open high low Close Volume Dividends Stocks Splits


st.line_chart(tickerDF.Close)
st.line_chart(tickerDF.Volume)