import streamlit as st
import pandas as pd

st.set_page_config(page_title="Inversysa Nicaragua - Inventario", layout="wide")

# SUSTITUYE ESTE LINK POR EL TUYO TERMINANDO EN /export?format=csv
sheet_url ="https://docs.google.com/spreadsheets/d/TU_CODIGO_LARGO/export?format=csv"

st.title("📊 Control de Inventario Inversysa")

@st.cache_data
def load_data(url):
    # Esto lee tu Google Sheet directamente
    return pd.read_csv(url)

try:
    df = load_data(sheet_url)
    st.success("✅ Datos cargados correctamente desde Google Sheets")
    
    # Aquí puedes ver tus marcas: Shinko, Nayasa, Bajaj, etc.
    st.dataframe(df, use_container_width=True)
    
except Exception as e:
    st.error("⚠️ Error: Asegúrate de que el link en el código termine en /export?format=csv y que la hoja sea pública.")
