import streamlit as st
import pandas as pd
import folium
from folium import plugins

# Configuración de la aplicación
st.title("Avistamientos de mamíferos en el Área de Conservación Guanacaste")
st.write("Registros de avistamientos de 3 especies de mamiferos (danta, venado cola blanca y coyote) en el Área de Conservación Guanacaste.")

# Cargar el CSV desde el repositorio
@st.cache
def load_data():
    url = "https://raw.githubusercontent.com/geociencias98/Proyecto/main/acg.csv"
    data = pd.read_csv(url)
    return data

# Cargar los datos
data = load_data()

# Mostrar los datos
st.subheader("Base de datos")
st.write(data)

# Normalizar nombres de columnas
data.columns = data.columns.str.strip().str.lower()

# Mostrar la tabla
st.subheader('Casos totales y muertes totales por país y por día')
st.dataframe(data, hide_index=True)

# Agrupar por fecha y sumar los casos totales
casos_totales_por_fecha = (
    datos_filtrados
    .groupby('year')['common_name']
    .sum()
    .reset_index()
)

# Crear el gráfico de líneas para casos totales
fig_casos = px.line(
    casos_totales_por_fecha, 
    x='year', 
    y='common_name', 
    title='Casos totales a lo largo del tiempo',
    labels={'Casos totales': 'Cantidad de casos totales', 'Fecha': 'Fecha'}
