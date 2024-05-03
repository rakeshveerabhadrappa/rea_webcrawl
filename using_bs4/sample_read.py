# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 23:42:35 2024

@author: Backpack1
"""

import pandas as pd


suburb = "manor+lakes"
state = "vic"
pc = "3024"


data = pd.read_csv(f'../data/Sold/sold_{suburb}_{state}_{pc}.csv')
#%%
# data.agent = data.agent.str.lstrip()
# data.agent = data.agent.replace('N/', 'N/A')
data = data[~data['sold_on'].str.contains('House|Residential')]
try:
    data['sold_on'] = pd.to_datetime(data['sold_on'], format='%d %b %Y')
except pd.errors.ParserError:
    print("Invalid date format encountered.")
# Convert the 'Date' column to datetime format


# Extract the year and create a new column 'Year'
data['sold_year'] = data['sold_on'].dt.year


#%%
agency_agent = data.groupby(["agency", "agent"]).count()
