# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 19:27:02 2022

@author: Shailesh
"""

import pandas as pd
import requests
import streamlit as st
import altair as alt

st.title("Bitcoin Prices")

currency_list = ['cad','usd','inr']
interval='daily'

API_URL='https://api.coingecko.com/api/v3/coins/bitcoin/market_chart'

day = st.slider('No of Days', min_value=1, max_value=365)
currency = st.radio('Currency', currency_list)

payload = {'vs_currency':currency,'days':str(day),'interval':interval}
req = requests.get(API_URL,payload)

if(req.status_code==200):
    raw_data = req.json()

    bitcoin_df = pd.DataFrame(raw_data['prices'][:-1], columns=['date',currency])
    bitcoin_df['date'] = pd.to_datetime(bitcoin_df['date'], unit='ms')
    bitcoin_df.sort_values(by="date",inplace=True)
    bitcoin_df = bitcoin_df.set_index('date')
    #st.line_chart(bitcoin_df)
    st.altair_chart(bitcoin_df, use_container_width=True)
    
    average_price = bitcoin_df[currency].mean()
    result = "Average price during this time was "+ str(average_price)+' '+currency
    st.write(result)

else:
    st.write('API has failed to fetch data.')
