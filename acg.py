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

# Normalizar nombres de columnas
data.columns = data.columns.str.strip().str.lower()

# Verificar que la columna 'year' exista
if 'year' in data.columns:
    # Crear un selectbox para el campo 'year'
    years = data['year'].unique()
    selected_year = st.selectbox("Selecciona un año:", years)

    # Filtrar los datos según el año seleccionado
    filtered_data = data[data['year'] == selected_year]

    # Mostrar tabla con los datos filtrados
    st.subheader("Datos Filtrados por Año")
    st.dataframe(filtered_data)
else:
    st.write("La columna 'year' no se encuentra en el DataFrame.")

