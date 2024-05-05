import streamlit as st
import pandas as pd
import numpy as np
from glob import glob
from pathlib import Path

st.write("""
        # Budget Dashboard: Test

        Hello world!
        
        """)


path = Path("../../Documents/Personal/Financial/Transactions/2024")

files = glob(str(path/"*"/"*.csv"))

# st.write(files)

df = pd.read_csv(files[10], parse_dates=True)
# df.set_index('Transaction Date',inplace=True)
# df.drop(columns='Post Date', inplace=True)

# grouped = df.groupby(df.index.day_of_week)

st.write(df.head(2))

st.write(df['Category'].unique())
# st.line_chart(data=df, y='Amount')
