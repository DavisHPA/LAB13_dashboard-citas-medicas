import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('citas_medicas.csv')

st.title('Dashboard de Gestión de Citas Médicas')

st.subheader('Citas por Especialidad')
conteo_especialidad = df['especialidad'].value_counts().reset_index()
conteo_especialidad.columns = ['especialidad', 'Cantidad']

fig1 = px.bar(
    conteo_especialidad,
    x='especialidad',
    y='Cantidad',
    labels={'especialidad': 'Especialidad', 'Cantidad': 'Cantidad'}
)
st.plotly_chart(fig1)

st.subheader('Estado de las Citas')
fig2 = px.pie(
    df,
    names='estado'
)
st.plotly_chart(fig2)

df['fecha'] = pd.to_datetime(df['fecha'])
df['mes'] = df['fecha'].dt.month

citas_mes = df.groupby('mes').size().reset_index(name='cantidad').sort_values('mes')

st.subheader('Citas por Mes')
fig3 = px.line(
    citas_mes,
    x='mes',
    y='cantidad',
    markers=True
)
st.plotly_chart(fig3)