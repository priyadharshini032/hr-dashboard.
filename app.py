import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("HR Dashboard 📊")

df = pd.read_excel("HR DATA.xlsx")

st.subheader("Dataset Preview")
st.dataframe(df)

st.subheader("Department Wise Employee Count")
st.bar_chart(df["Department"].value_counts())

st.subheader("Work Mode Distribution")
work_mode = df["Work_Mode"].value_counts()

fig1, ax1 = plt.subplots()
ax1.pie(work_mode, labels=work_mode.index, autopct='%1.1f%%')
st.pyplot(fig1)

st.subheader("Performance Rating Distribution")
st.bar_chart(df["Performance_Rating"].value_counts())

st.subheader("Salary Distribution")
st.line_chart(df["Salary_INR"])

st.subheader("Location Distribution")
st.bar_chart(df["Location"].value_counts())
