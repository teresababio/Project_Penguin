import streamlit as st
import pandas as pd
from data.get_data import get_page_penguins, dict_species
from imageio.v2 import imread

st.set_page_config(page_title="Datos", page_icon="🐧")
st.markdown("# Presentación de los datos")
st.sidebar.header("Datos")

st.markdown('''La base de datos que se emplea para el estudio de los pingüinios es la siguiente''')
                

df=pd.DataFrame(get_page_penguins(0))
df = df.drop(["location", "_id", "Stage"], axis=1)
st.write(df.head(10))

list_var = ["Species", "Clutch Completion", "Date Egg", "Culmen", "Flipper Length", 
            "Body Mass", "Sex", "Delta 15 N y Delta 13 C"]

st.subheader("Species")
print(list(df["Species"].unique()))

url = [ "./images/Adelie_Penguin.jpg", "./images/IMG_4381.jpg", "./images/gento_penguin.jpg"]


images = [imread(i) for i in url]
st.image(images, width = 200, caption=["Adelie Penguin (Pygoscelis adeliae)", "Chinstrap penguin (Pygoscelis antarctica)",
                 "Gentoo penguin (Pygoscelis papua)"])



st.subheader("Culmen")
st.markdown('''Las variables Culmen hacen refencia a características del pico de los pingüinos.''')
st.image(imread("./images/culmen.jpg_small"), width = 500)

st.subheader("Delta")
st.markdown('''
    Los valores de isótopos estables de carbono (delta13C) y nitrógeno (delta15N) en sangre, plumas, cáscara de huevo y
    huesos se han utilizado en estudios de aves marinas desde la década de 1980, proporcionando una valiosa fuente de
    información sobre la dieta, los patrones de alimentación y el comportamiento migratorio de las aves.
    ''')


st.subheader("Date Egg")
st.markdown('''
    Indica la fecha en la que el nido y, por consecuencia, los datos fueron tomados para los individuos
    ''')

st.subheader("Clutch completion")
st.markdown('''
    Indica si en el momento de estudiar el nido habían dos huevos 
    ''')

 #date Egg stage

st.subheader("Study Name")
st.markdown('''
    Código de la expedición en la que fueron recolectados los datos 
    ''')



click = st.button('Click me')
print(click)