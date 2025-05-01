#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 30 19:42:26 2025

@author: jonathan_m_adamson
"""

import yfinance as yf
import pandas as pd

# Define tickers
tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'META']

# Download data without slicing ['Adj Close'] immediately
raw_data = yf.download(tickers, 
                       start="2019-01-01", 
                       end="2024-12-31", 
                       group_by='ticker', 
                       progress=False, 
                       threads=False)

# Export to CSV for use in Jupyter
raw_data.to_csv("tech_stock_prices_5yr.csv")

