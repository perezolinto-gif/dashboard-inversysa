import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(page_title="Inversysa Nicaragua - Inteligencia de Compras", layout="wide")

# SUSTITUYE EL LINK DE ABAJO POR EL TUYO
# Importante: El link debe terminar en /export?format=csv
sheet_url = "https://docs.google.com/spreadsheets/d/TU_CODIGO_LARGO/export?format=csv"

st.title("📊 Control de Inventario Inversysa")

@st.cache_data
def load_data(url):
    return pd.read_csv(url)

try:
    df = load_data(sheet_url)
    
    # Métricas principales
    st.subheader("Análisis de Marcas (Shinko, Nayasa, Bajaj, EDGE)")
    
    # Selector de Marca para filtrar
    marca = st.selectbox("Seleccionar Marca:", df['MARCA'].unique())
    df_filtered = df[df['MARCA'] == marca]
    
    # Lógica de Semáforo de Inversysa
    def semaforo(row):
        if row['STOCK'] == 0 and row['VENTA_PROM'] > 0:
            return "🔴 COMPRAR (Escasez)"
        elif row['STOCK'] > (row['VENTA_PROM'] * 3):
            return "🟡 EXCESO (No pedir)"
        else:
            return "🟢 SALUDABLE"

    df_filtered['RECOMENDACIÓN'] = df_filtered.apply(semaforo, axis=1)
    
    # Tabla interactiva
    st.dataframe(df_filtered, use_container_width=True)
    
except Exception as e:
    st.error("Conectando con Google Sheets... asegúrate de que el link sea público.")
    st.info("Tip: El link en el código debe terminar en /export?format=csv")
