import streamlit as st
import pandas as pd

st.title('My first app')
df = pd.read_csv(
    "../../datasets/2023-06-12-cleaned-data.csv"
)
st.line_chart(df)