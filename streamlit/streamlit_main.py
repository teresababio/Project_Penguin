import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import plotly.graph_objs as go
from data.graficos import mapa_Palmer
from streamlit_folium import st_folium


st.title('Los pingüinos del Archipiélago de Palmer')
st.text('El archipiélago Palmer es un grupo de islas montañosas ubicadas frente a la costa\n noroeste de la Península Antártica. Los estrechos de Gerlache y Bismarck separan el\n archipiélago de la costa del continente antártico. El archipiélago de Palmer se \nextiende entre 63 ° y 64 ° de latitud sur, entre la isla Torre (Tower) en el norte \n y la isla Anvers en el sur. Las islas del archipiélago Palmer son una de las partes\n más accesibles y espectaculares del continente antártico.\n ')
st.text('En este caso, se presentan tres especies de pingüinos ubicados en tres islas \n del Archipiérlago de Palmer.')
map_palmer = st_folium(mapa_Palmer())
st.text('Existen diferentes factores que caracterizan a cada una de las especies\n de pingüinos. Más aún, en una misma especie se puede dar lo que se conoce como\n dimorfismo sexual (variaciones en la fisonomía externa, como forma, coloración o\n tamaño, entre machos y hembras de una misma especie). ')  

st.header('Variables')
chosen_one = st.multiselect('Elige pokemon', [p["name"] for p in pokemons], key="1")