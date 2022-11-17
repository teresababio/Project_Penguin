import streamlit as st
import streamlit.components.v1 as components
import numpy as np
from data.graficos import mapa_Palmer, graf_var, graf_corr, graf_2var
from data.get_data import dict_species, get_page_penguins
from streamlit_folium import st_folium
from PIL import Image


st.title('Los pingüinos del Archipiélago de Palmer')
st.sidebar.success("Selecciona una opción")
st.markdown("""
        El archipiélago Palmer es un grupo de islas montañosas ubicadas frente a la costa noroeste de la 
        Península Antártica. Las islas del archipiélago Palmer son unas de las partes más accesibles y espectaculares
        del continente antártico.

        Se estudiará la población de pingüinos de tres islas  del Archipiélago de Palmer.
        """)
map_palmer = st_folium(mapa_Palmer())

st.markdown("""
        Concretamente, las características de tres especies de pingüinos.
        """)


st.markdown("""Existen diferentes factores que caracterizan a cada una de las especies de pingüinos.
                A continuación, se mostrarán gráficas de las variables recogidas de cada una de las especies.  """) 





click = st.button('Click me')
print(click)


Adelie Penguin (Pygoscelis adeliae)
Chinstrap penguin (Pygoscelis antarctica)
Gentoo penguin (Pygoscelis papua)