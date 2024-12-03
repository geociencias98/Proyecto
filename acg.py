import streamlit as st
import pandas as pd

# Configuración de la aplicación
st.title("Explorador de Datos de Especies")
st.write("Cargue un archivo CSV con datos de especies.")

# Cargar el CSV desde el repositorio
@st.cache
def load_data():
    url = "https://raw.githubusercontent.com/geociencias98/Proyecto/acg.csv"
    data = pd.read_csv(url)
    return data

# Cargar los datos
data = load_data()

# Mostrar los datos
st.subheader("Datos Cargados")
st.write(data)

# Opcional: Gráficos o análisis
st.subheader("Análisis de Datos")
year = st.selectbox("Selecciona un año:", data['year'].unique())
filtered_data = data[data['year'] == year]
st.write(filtered_data)

# Mapa de ubicaciones
st.subheader("Mapa de Ubicaciones")
st.map(data[['latitude', 'longitude']])
