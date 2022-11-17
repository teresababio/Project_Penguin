import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import plotly.graph_objs as go
from data.graficos import mapa_Palmer, graf_var, graf_corr, graf_2var
from data.get_data import dict_species, get_page_penguins
from streamlit_folium import st_folium


st.title('Los pingüinos del Archipiélago de Palmer')
st.text('El archipiélago Palmer es un grupo de islas montañosas ubicadas frente a la costa\n noroeste de la Península Antártica. Las islas del archipiélago Palmer son unas de las partes\n más accesibles y espectaculares del continente antártico.\n ')
st.text('En este caso, se presentan tres especies de pingüinos ubicados en tres islas \n del Archipiérlago de Palmer.')
map_palmer = st_folium(mapa_Palmer())
st.text('Existen diferentes factores que caracterizan a cada una de las especies\n de pingüinos. Más aún, en una misma especie se puede dar lo que se conoce como\n dimorfismo sexual (variaciones en la fisonomía externa, como forma, coloración o\n tamaño, entre machos y hembras de una misma especie). ')  


############################################33

st.header('Variables')
st.text('En este apartado se podrán observar gráficas de los datos de cada una de las variables del dataset \n de las especies indicadas para su correspondiente comparación.')
chosen_multi = st.multiselect('Elige las especies de pingüinos', dict_species.values(), key="1")
list_var = [var for  var in get_page_penguins()[0].keys()][5:-1]
list_var.remove('Clutch Completion')
list_var.remove('Stage')
option = st.selectbox( 'Seleciona la variable a representar', list_var)


if chosen_multi:
    fig = graf_var(chosen_multi, option)

    if fig != None:
        st.plotly_chart(fig)

st.header('Estudio de las relaciones entre las variables')

st.subheader("Gráfica de correlaciones entre variables numéricas")
st.plotly_chart(graf_corr())



list_num = ['Culmen Length (mm)', 'Culmen Depth (mm)', 'Flipper Length (mm)', 'Body Mass (g)',  'Delta 15 N (o/oo)', 'Delta 13 C (o/oo)']

st.subheader("Enfrentamiento de variables")

chosen_multi = st.multiselect('Elige las dos variables a enfrentar', list_num, key="2", max_selections = 2)
chosen_multi2 = st.multiselect('Elige las especies de pingüinos que se presentarán', dict_species.values(), key="3")

if len(chosen_multi)==2 and chosen_multi2!=[]:
    fig = graf_2var(chosen_multi2, chosen_multi)
    if fig != None:
        st.plotly_chart(fig)




click = st.button('Click me')
print(click)


