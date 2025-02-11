import streamlit as st
import pandas as pd
import plotly.express as px

# Título de la app
st.title("Water Impact App")

# Subir archivo XLSX
uploaded_file = st.file_uploader("Sube tu archivo Excel (.xlsx)", type=["xlsx"])

if uploaded_file:
    # Leer el archivo Excel
    data = pd.read_excel(uploaded_file)

    # Mostrar los primeros 5 registros del archivo subido
    st.subheader("Vista previa de los datos")
    st.dataframe(data.head())

    # Desplegables para filtrar según las 3 primeras columnas
    col1, col2, col3 = data.columns[:3]  # Las 3 primeras columnas

    # Desplegables interactivos
    option1 = st.selectbox(f"Selecciona {col1}", ["Todos"] + data[col1].dropna().unique().tolist())
    option2 = st.selectbox(f"Selecciona {col2}", ["Todos"] + data[col2].dropna().unique().tolist())
    option3 = st.selectbox(f"Selecciona {col3}", ["Todos"] + data[col3].dropna().unique().tolist())

    # Filtrado de datos según las selecciones
    filtered_data = data.copy()
    if option1 != "Todos":
        filtered_data = filtered_data[filtered_data[col1] == option1]
    if option2 != "Todos":
        filtered_data = filtered_data[filtered_data[col2] == option2]
    if option3 != "Todos":
        filtered_data = filtered_data[filtered_data[col3] == option3]

    # Gráfico de barras basado en la selección
    if len(filtered_data) > 0:
        fig = px.bar(filtered_data, x=filtered_data.columns[0], y=filtered_data.columns[1], color=filtered_data.columns[2],
                     title="Gráfico de Barras Interactivo")
        st.plotly_chart(fig)
    else:
        st.warning("No hay datos que coincidan con los filtros seleccionados.")
else:
    st.info("Sube un archivo Excel (.xlsx) para comenzar.")
