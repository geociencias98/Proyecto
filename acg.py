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

# Verificar que la columna 'common_name' exista
if 'common_name' in data.columns:
    # Crear un selectbox para el campo 'common_name'
    common_name = data['common_name'].unique()
    selected_common_name = st.selectbox("Selecciona un nombre común:", common_name)

    # Filtrar los datos según el nombre común seleccionado
    filtered_data = data[data['common_name'] == selected_common_name]

    # Mostrar tabla con los datos filtrados
    st.subheader("Datos Filtrados por Nombre Común")
    st.dataframe(filtered_data)
else:
    st.write("La columna 'common_name' no se encuentra en el DataFrame.")


