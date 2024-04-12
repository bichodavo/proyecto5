import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('vehicles_us.csv') # leer los datos
title_header = st.header('Anuncios de vehículos en venta')
subtitle_header_1 = st.write('***Datos interesantes sobre los vehículos en venta***')
hist_checkbox = st.radio(label='Histogramas por característica',options=['color','cilindros','precio','modelo'], captions=['color de los vehículos','número de cilindros','precio de los vehículos','año de salida'])

if hist_checkbox == 'color':
    # crear un histograma
    fig = px.histogram(car_data, x="paint_color")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
elif hist_checkbox == 'cilindros':
    # crear un histograma
    fig = px.histogram(car_data, x="cylinders")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

elif hist_checkbox == 'precio':
    # crear un histograma
    fig = px.histogram(car_data, x="price")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

elif hist_checkbox == 'modelo':
    # crear un histograma
    fig = px.histogram(car_data, x="model_year")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

subtitle_header_2 = st.write('***Precio de los modelos dependiendo de sus características***')

scatter_checkbox = st.radio(label='Carácteristicas interesantes',options=['modelo','condición','odometro'])

if scatter_checkbox == 'modelo':
    # crear un gráfico de dispersión
    scatter_fig = px.scatter(car_data, x='model', y='price')

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(scatter_fig, use_container_width=True)

elif scatter_checkbox == 'condición':
    # crear un gráfico de dispersión
    scatter_fig = px.scatter(car_data, x='condition', y='price')

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(scatter_fig, use_container_width=True)

elif scatter_checkbox == 'odometro':
    # crear un gráfico de dispersión
    scatter_fig = px.scatter(car_data, x='odometer', y='price')

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(scatter_fig, use_container_width=True)
    