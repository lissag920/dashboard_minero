import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración de la página
st.set_page_config(page_title="Dashboard Minero", layout="wide")

# --- Título del Dashboard ---
st.markdown("<h1 style='text-align: center; color: #4B8BBE;'>Dashboard Interactivo del Sector Minero Colombiano</h1>", unsafe_allow_html=True)
st.markdown("### Análisis de Producción, Precios y Exportaciones (2020-2024)")
st.markdown("*Proyecto de Microeconomía con uso de Inteligencia Artificial*")

# --- Datos simulados ---
data = {
    "Año": [2020, 2021, 2022, 2023, 2024],
    "Producción_Carbón_Toneladas": [90000000, 85000000, 80000000, 78000000, 74000000],
    "Precio_Carbón_USD_Ton": [50, 70, 95, 110, 105],
    "Exportaciones_Mineras_USD_Mill": [5000, 5200, 5600, 6100, 6300],
}

df = pd.DataFrame(data)

# --- Crear pestañas interactivas ---
tab1, tab2, tab3 = st.tabs(["📊 Producción", "💰 Precio del Carbón", "🌍 Exportaciones"])

# Producción de carbón
with tab1:
    fig1 = px.line(df, x="Año", y="Producción_Carbón_Toneladas", markers=True,
                   title="Evolución de la Producción de Carbón",
                   labels={"Producción_Carbón_Toneladas": "Toneladas"})
    fig1.update_traces(line_color='brown')
    st.plotly_chart(fig1, use_container_width=True)

# Precio del carbón
with tab2:
    fig2 = px.bar(df, x="Año", y="Precio_Carbón_USD_Ton",
                  title="Precio Internacional del Carbón",
                  labels={"Precio_Carbón_USD_Ton": "USD por Tonelada"},
                  color_discrete_sequence=["gray"])
    st.plotly_chart(fig2, use_container_width=True)

# Exportaciones mineras
with tab3:
    fig3 = px.line(df, x="Año", y="Exportaciones_Mineras_USD_Mill", markers=True,
                   title="Exportaciones Mineras Totales",
                   labels={"Exportaciones_Mineras_USD_Mill": "Millones de USD"})
    fig3.update_traces(line_color='green')
    st.plotly_chart(fig3, use_container_width=True)

# --- Predicción IA ---
st.markdown("### 🔮 Predicción 2025 (Simulada con IA)")
st.info("Si las restricciones ambientales continúan, se espera que la producción caiga a 70 millones de toneladas y el precio suba a 115 USD por tonelada.")

# --- Conclusión ---
st.markdown("""
**📌 Conclusión Microeconómica:**    
El sector minero colombiano enfrenta un escenario de escasez creciente, con efectos sobre el precio y la competitividad.  
La Inteligencia Artificial puede ayudar a anticipar estos movimientos y diseñar mejores políticas públicas.
""")