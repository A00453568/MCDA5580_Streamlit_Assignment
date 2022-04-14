# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 19:27:02 2022

@author: Shailesh
"""

import pandas as pd
import requests
import streamlit as st

st.title("Bitcoin Prices")

currency_list = ['cad','usd','inr']
interval='daily'

#API_URL=BASE_URL + '?vs_currency='+currency + '&days='+ str(day)+'&interval=' + interval
API_URL='https://api.coingecko.com/api/v3/coins/bitcoin/market_chart'

day = st.slider('No of Days', min_value=1, max_value=365)
currency = st.radio('Currency', currency_list)

payload = {'vs_currency':currency,'days':str(day),'interval':interval}
req = requests.get(API_URL,payload)

if(req.status_code==200):
    raw_data = req.json()

    df = pd.DataFrame(raw_data['prices'], columns=['date','price'])
    df['date'] = pd.to_datetime(df['date'], unit='ms')
    df.sort_values(by="date",inplace=True)
    df = df.set_index('date')
    st.line_chart(df)
    
    average_price = df['price'].mean()
    result = "Average price during this time was "+ str(average_price)+' '+currency
    st.write(result)

else:
    st.write('API has failed to fetch data.')
