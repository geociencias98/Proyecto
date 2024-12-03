import streamlit as st
import pandas as pd

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

# Mostrar las columnas del DataFrame
st.write("Columnas disponibles en el DataFrame:", data.columns.tolist())

# Opcional: Gráficos o análisis
if 'year' in data.columns:
    st.subheader("Análisis de Datos")
    year = st.selectbox("Selecciona un año:", data['year'].unique())
    filtered_data = data[data['year'] == year]
    st.write(filtered_data)

data['latitude'] = pd.to_numeric(data['latitude'], errors='coerce')
data['longitude'] = pd.to_numeric(data['longitude'], errors='coerce')

    # Mapa de ubicaciones
    st.subheader("Mapa de Ubicaciones")
    if not filtered_data.empty and 'latitude' in filtered_data.columns and 'longitude' in filtered_data.columns:
        st.map(filtered_data[['latitude', 'longitude']])
    else:
        st.write("No hay datos disponibles para mostrar en el mapa.")
else:
    st.write("La columna 'year' no se encuentra en el DataFrame.")
