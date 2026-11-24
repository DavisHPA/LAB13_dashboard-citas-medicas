import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Activar pantalla completa rectangular (panorámica)
st.set_page_config(
    page_title="Dashboard de Gestión de Citas Médicas",
    layout="wide"
)

# Reducir márgenes superiores para que quepa todo en una sola pantalla
st.markdown("""
    <style>
        .block-container {
            padding-top: 1.5rem;
            padding-bottom: 1rem;
        }
    </style>
""", unsafe_allow_html=True)

df = pd.read_csv('citas_medicas.csv')

st.title('Dashboard de Gestión de Citas Médicas')

# 2. Dividir la pantalla rectangular en 3 columnas iguales
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader('Citas por Especialidad')
    conteo_especialidad = df['especialidad'].value_counts().reset_index()
    conteo_especialidad.columns = ['especialidad', 'Cantidad']
    fig1 = px.bar(
        conteo_especialidad,
        x='especialidad',
        y='Cantidad',
        labels={'especialidad': 'Especialidad', 'Cantidad': 'Cantidad'},
        height=380
    )
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.subheader('Estado de las Citas')
    fig2 = px.pie(
        df,
        names='estado',
        height=380
    )
    st.plotly_chart(fig2, use_container_width=True)

with col3:
    df['fecha'] = pd.to_datetime(df['fecha'])
    df['mes'] = df['fecha'].dt.month
    citas_mes = df.groupby('mes').size().reset_index(name='cantidad').sort_values('mes')
    
    st.subheader('Citas por Mes')
    fig3 = px.line(
        citas_mes,
        x='mes',
        y='cantidad',
        markers=True,
        labels={'mes': 'Mes', 'cantidad': 'Cantidad'},
        height=380
    )
    st.plotly_chart(fig3, use_container_width=True)
