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
day_list=[1,7,30,90,365]
interval_list = ['daily','']

currency='cad'
day=90
interval='daily'

API_URL = '''https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=cad&days=90&interva
l=daily'''
BASE_URL='https://api.coingecko.com/api/v3/coins/bitcoin/market_chart'

API_URL=BASE_URL + '?vs_currency='+currency + '&days='+ str(day)+'&interval=' + interval
req = requests.get(API_URL)

if(req.status_code==200):
    raw_data = req.json()

df = pd.DataFrame(raw_data['prices'],
                  columns=['date','price'])

df['date'] = pd.to_datetime(df['date'], unit='ms')
df.sort_values(by="date",inplace=True)
df.plot.line(x="date", y="price")
average_price = df['price'].mean()
result = "Average price during this time was "+ str(average_price)+' '+currency
st.write(result)
