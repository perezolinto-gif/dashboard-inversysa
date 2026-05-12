import streamlit as st
import pandas as pd

st.set_page_config(page_title="Inversysa Nicaragua - Inventario", layout="wide")

# ESTE ES TU LINK YA CONVERTIDO PARA INVERSYSA
sheet_url = "https://docs.google.com/spreadsheets/d/18xPAnO_qO6p7Y9_U6yU_tE_r_nU/export?format=csv"

st.title("📊 Control de Inventario Inversysa Nicaragua")

@st.cache_data
def load_data(url):
    # Esto lee tu Google Sheet directamente sin importar los nombres de las columnas
    return pd.read_csv(url)

try:
    df = load_data(sheet_url)
    st.success("✅ ¡Datos de Inversysa cargados exitosamente!")
    
    # Buscador para que tu equipo en Nicaragua encuentre rápido llantas Shinko, Nayasa o repuestos Bajaj
    st.subheader("🔍 Buscador de Productos")
    busqueda = st.text_input("Escribe el nombre, marca o código de la llanta/repuesto:")
    
    if busqueda:
        mask = df.apply(lambda row: row.astype(str).str.contains(busqueda, case=False).any(), axis=1)
        df_final = df[mask]
    else:
        df_final = df

    # Muestra tu Excel tal cual lo tienes en Google Sheets
    st.dataframe(df_final, use_container_width=True)

except Exception as e:
    st.error(f"Error al conectar con el archivo: {e}")
    st.info("Asegúrate de que en el Google Sheet hayas dado clic en el botón verde 'Compartir' y seleccionado 'Cualquier persona con el enlace'.")
    st.error(f"Error al leer los datos: {e}")
    st.info("Revisa que el link termine en /export?format=csv")
