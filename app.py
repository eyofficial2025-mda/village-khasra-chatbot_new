import streamlit as st
import pandas as pd

st.title("Village Khasra Search Chatbot")

# Load the CSV file
@st.cache_data
def load_data():
    df = pd.read_csv("MP_2031_table_new.csv")
    return df

df = load_data()

# Dropdown for villages (Column C)
villages = sorted(df.iloc[:, 2].dropna().unique())  # Column C
selected_village = st.selectbox("Select a Village", villages)

# Filter for selected village
village_data = df[df.iloc[:, 2] == selected_village]

# Text input for Khasra number (Column H)
khasra_input = st.text_input("Enter Khasra Number")

# Search and display
if khasra_input:
    result = village_data[village_data.iloc[:, 7].astype(str) == khasra_input]
    if not result.empty:
        st.write("### Search Result")
        st.dataframe(result[[result.columns[2], result.columns[5], result.columns[6], result.columns[8], result.columns[9]]])
    else:
        st.warning("No matching Khasra found in this village.")

# Expandable full dataset
with st.expander("View full dataset"):
    st.dataframe(df)
