import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import plotly.graph_objs as go
from data.graficos import mapa_Palmer, graf_var
from data.get_data import dict_species, get_n_penguins
from streamlit_folium import st_folium


st.title('Los pingüinos del Archipiélago de Palmer')
st.text('El archipiélago Palmer es un grupo de islas montañosas ubicadas frente a la costa\n noroeste de la Península Antártica. Los estrechos de Gerlache y Bismarck separan el\n archipiélago de la costa del continente antártico. El archipiélago de Palmer se \nextiende entre 63 ° y 64 ° de latitud sur, entre la isla Torre (Tower) en el norte \n y la isla Anvers en el sur. Las islas del archipiélago Palmer son una de las partes\n más accesibles y espectaculares del continente antártico.\n ')
st.text('En este caso, se presentan tres especies de pingüinos ubicados en tres islas \n del Archipiérlago de Palmer.')
map_palmer = st_folium(mapa_Palmer())
st.text('Existen diferentes factores que caracterizan a cada una de las especies\n de pingüinos. Más aún, en una misma especie se puede dar lo que se conoce como\n dimorfismo sexual (variaciones en la fisonomía externa, como forma, coloración o\n tamaño, entre machos y hembras de una misma especie). ')  


############################################33

st.header('Variables')
st.text('En este apartado se podrán observar gráficas de los datos de cada una de las variables del dataset \n de las especies indicadas para su correspondiente comparación.')
chosen_multi = st.multiselect('Elige las especies de pingüinos', dict_species.values(), key="1")
list_var = [var for  var in get_n_penguins(1)[0].keys()][5:-1]
list_var.remove('Clutch Completion')
option = st.selectbox( 'Seleciona la variable a representar', list_var)
print(option, chosen_multi)
graf_var(chosen_multi, option)



click = st.button('Click me')
print(click)











