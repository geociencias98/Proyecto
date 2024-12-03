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

# Verificar que las columnas 'latitude' y 'longitude' existan
if 'latitude' in data.columns and 'longitude' in data.columns:
    # Crear un mapa centrado en la ubicación promedio
    map_center = [data['latitude'].mean(), data['longitude'].mean()]
    map_folium = folium.Map(location=map_center, zoom_start=6)

    # Agregar marcadores para cada animal
    for index, row in data.iterrows():
        folium.Marker(
            location=[row['latitude'], row['longitude']],
            popup=(
                f"<strong>Nombre Común:</strong> {row['common_name']}<br>"
                f"<strong>Nombre Científico:</strong> {row['scientific_name']}<br>"
                f"<strong>Año:</strong> {row['year']}"
            ),
            icon=folium.Icon(color="green")
        ).add_to(map_folium)

    # Renderizar el mapa en Streamlit
    st.subheader("Mapa Interactivo de Animales")
    st.components.v1.html(map_folium._repr_html_(), height=500)
else:
    st.write("Las columnas 'latitude' y 'longitude' no se encuentran en el DataFrame.")
