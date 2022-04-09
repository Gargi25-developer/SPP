from datetime import datetime
from inspect import Parameter
from select import select
from tkinter import Button
from tkinter.tix import ButtonBox
from tracemalloc import start
import click
from matplotlib import ticker
from matplotlib.pyplot import title
from sklearn.metrics import calinski_harabasz_score
import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt  

st.title("Stock Price Prediction App")
st.header(" Welcome!! ")  
st.subheader('Here you can predict stock price by using some simple steps.')
st.markdown(""" #### Shown are the stock price data for query companies.

""")

#st.title("Finance Dashboard")
st.sidebar.title("Finance Dashboard")

tickers = ('TSLA', 'APPL', 'MSFT', 'BTC-USD', 'SBIN.NS', 'IBM', 'POAHY', 'JAGX','WIPRO.NS')
#ticker_list = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/s-and-p-500-companies/master/data/constituents_symbols.txt')
#tickerSymbol = st.sidebar.selectbox('Stock ticker', ticker_list)



#dropdown =st.multiselect('Pick your Assets', tickers)
#To add the widgets in sidebar
companies=st.sidebar.multiselect('Pick your Assets', tickers)

#this is to add slider
#st.slider("Years", min_value=0, max_value=10,value=0,step=1)

#start = st.date_input('Start',value = pd.to_datetime('2014-01-01'))
#end = st.date_input('End',value = pd.to_datetime('today'))
st.sidebar.subheader('Query Parameter')
start=st.sidebar.date_input('Start',value = pd.to_datetime('2014-01-01'))
end=st.sidebar.date_input('End',value = pd.to_datetime('today'))


if st.button("Search"):
 st.text('Loading data...')
 

 


def relativeret(df):
    rel = df.pct_change()
    cumret = (1+rel).cumprod() - 1
    cumret = cumret.fillna(0)
    return cumret

if len(companies) > 0:
    #df =yf.download(sidebar,start,end)['Adj Close']
    df = relativeret(yf.download(companies, start, end))['Adj Close']
    st.line_chart(df)
    st.bar_chart(df)
    st.area_chart(df)
      