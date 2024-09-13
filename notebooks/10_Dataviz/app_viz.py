path = '/workspaces/DF-P/notebooks/10_Dataviz/data/gapminder.csv'
import pandas as pd
df = pd.read_csv(path)
print(df)

import streamlit as st

st.write(df)