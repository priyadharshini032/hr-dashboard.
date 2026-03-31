import streamlit as st
import pandas as pd

st.title("HR Dashboard")

df = pd.read_excel("HR DATA.xlsx")

st.dataframe(df)

st.bar_chart(df["Department"].value_counts())
