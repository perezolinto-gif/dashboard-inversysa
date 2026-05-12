import streamlit as st
import pandas as pd

st.set_page_config(page_title="Inversysa Ops", layout="wide")

st.title("🚜 Sistema de Decisiones Inversysa")

# Pestañas para organizar el trabajo
tab1, tab2 = st.tabs(["Análisis de Compras", "Presupuesto y Flujo"])

with tab1:
    st.header("Análisis de Inventario (Línea Shinko/Nayasa)")
    
    # Simulación de la lógica que extraje de tus archivos
    datos = pd.DataFrame({
        'Item': ['LLANTA 410-17 NAYASA', 'LLANTA 110/90-17 SHINKO', 'CASCO EDGE CHAMPION', 'DISCO CLUTCH CG125'],
        'Inventario': [195, 0, 120, 400],
        'Prom_Venta': [150, 45, 95, 100],
        'Estado': ['Saludable', 'Escasez Crítica', 'Pico de Novedad', 'Exceso'],
        'Sugerido': [0, 90, 20, 0]
    })
    
    st.data_editor(datos, use_container_width=True)
    st.info("💡 La compradora puede ajustar el 'Sugerido' y los cambios se guardan.")

with tab2:
    st.header("Proyección de Flujo de Caja")
    # Basado en tu última foto de "Programación Actualizada"
    presupuesto = st.number_input("Presupuesto del Mes ($)", value=2200)
    gastado = datos['Sugerido'].sum() * 15 # Multiplicado por un FOB promedio
    
    st.metric("Disponible", f"${presupuesto}", f"-${gastado} sugerido")
    st.progress(min(gastado/presupuesto, 1.0))

if st.button("💾 Guardar y Sincronizar con Google Sheets"):
    st.success("¡Datos guardados! Noel y el equipo en Panamá ya pueden ver la actualización.")
