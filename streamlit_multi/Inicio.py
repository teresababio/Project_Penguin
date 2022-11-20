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

        Los pingüinos son especies recurrentes en estas islas. Por ello, se estudiará las características de la 
        población de tres especies de  pingüinos  de la familia Pygoscelis anidados en tres islas  del Archipiélago de Palmer.
        """)
map_palmer = st_folium(mapa_Palmer())

st.markdown("""
        En cada temporada, los nidos de estudio, donde se encuentran las parejas de adultos, 
        se marcan y se monitorizan  individualmente antes del inicio de la puesta de huevos. De cada uno de los
        individuos se toman muestras de sangre  y medidas del tamaño estructural y la masa corporal. 
        """)



click = st.button('Click me')
print(click)


