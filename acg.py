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

# URL de la imagen
image_url = "https://raw.githubusercontent.com/geociencias98/Proyecto/main/Grafico.png"

# Mostrar la imagen en Streamlit
st.image(image_url, caption='Gráfico', use_column_width=True)

# URL de la imagen
image_url = "https://raw.githubusercontent.com/geociencias98/Proyecto/main/Mapa.png"

# Mostrar la imagen en Streamlit
st.image(image_url, caption='Mapa de ubicación de avistamientos de mamíferos en el ACG', use_column_width=True)

