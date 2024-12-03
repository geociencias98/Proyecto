import streamlit as st
import pandas as pd
import folium
from folium import plugins

# Configuración de la aplicación
st.title("Explorador de Datos de Especies")
st.write("Cargue un archivo CSV con datos de especies.")

# Cargar el CSV desde el repositorio
@st.cache
def load_data():
    url = "https://raw.githubusercontent.com/geociencias98/Proyecto/main/acg.csv"
    data = pd.read_csv(url)
    return data

# Cargar los datos
data = load_data()

# Mostrar los datos
st.subheader("Datos Cargados")
st.write(data)

# Crear un mapa centrado en una ubicación específica
map_center = [49.255, -123.13]  # Coordenadas de Vancouver
map_folium = folium.Map(location=map_center, zoom_start=12)

# Agregar un marcador
folium.Marker(
    location=[49.255, -123.13],
    popup="Ubicación de Ejemplo",
    icon=folium.Icon(color="blue")
).add_to(map_folium)

# Agregar un cluster de marcadores (opcional)
marker_cluster = plugins.MarkerCluster().add_to(map_folium)

# Agregar más marcadores al cluster
for i in range(10):  # Ejemplo de 10 marcadores
    folium.Marker(
        location=[49.25 + i * 0.01, -123.13 + i * 0.01],
        popup=f"Marcador {i + 1}",
        icon=folium.Icon(color="green")
    ).add_to(marker_cluster)

# Renderizar el mapa en Streamlit
st.subheader("Mapa Interactivo")
st.components.v1.html(map_folium._repr_html_(), height=500)
