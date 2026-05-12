import streamlit as st
import pandas as pd

st.set_page_config(page_title="Inversysa Nicaragua - Inventario", layout="wide")

# 1. PEGA TU LINK AQUÍ (Asegúrate de que termine en /export?format=csv)
sheet_url = "TU_LINK_AQUI"

st.title("📊 Control de Inventario Inversysa")

@st.cache_data
def load_data(url):
    return pd.read_csv(url)

try:
    df = load_data(sheet_url)
    st.success("✅ ¡Datos cargados exitosamente!")
    
    # 2. BUSCADOR SIMPLE
    st.subheader("Buscador de Productos")
    busqueda = st.text_input("Escribe el nombre de la llanta o repuesto:")
    
    if busqueda:
        # Filtra en todas las columnas por lo que escribas
        mask = df.apply(lambda row: row.astype(str).str.contains(busqueda, case=False).any(), axis=1)
        df_final = df[mask]
    else:
        df_final = df

    # 3. MUESTRA TU EXCEL TAL CUAL ES
    st.dataframe(df_final, use_container_width=True)

except Exception as e:
    st.error(f"Error al leer los datos: {e}")
    st.info("Revisa que el link termine en /export?format=csv")
