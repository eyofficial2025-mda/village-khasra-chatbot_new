import streamlit as st
import pandas as pd

# Load your updated CSV file
df = pd.read_csv("MP 2031 table_new.csv")

# Clean column names and values to remove hidden spaces
df.columns = df.columns.str.strip()
df["Village"] = df["Village"].astype(str).str.strip()
df["Khasra"] = df["Khasra"].astype(str).str.strip()

# Streamlit UI
st.set_page_config(page_title="Village Khasra Search Chatbot", layout="centered")

st.markdown("<h1 style='text-align: center;'>Village Khasra Search Chatbot</h1>", unsafe_allow_html=True)

# Dropdown for village selection
village = st.selectbox("Select a Village", sorted(df["Village"].unique()))

# Input for khasra number
khasra = st.text_input("Enter Khasra Number")

# Search logic
if khasra:
    khasra = khasra.strip()
    result = df[(df["Village"] == village) & (df["Khasra"] == khasra)]

    if not result.empty:
        st.success("✅ Khasra details found:")
        st.table(result[["Village", "Khasra", "Land use", "Sub class", "Latitude", "Longitude"]])
    else:
        st.warning("⚠️ No matching Khasra found in this village.")
else:
    st.info("Enter a Khasra number to begin the search.")

# Optional: expandable section to view full dataset
with st.expander("📘 View full dataset"):
    st.dataframe(df)

