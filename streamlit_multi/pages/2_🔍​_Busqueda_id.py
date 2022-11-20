import streamlit as st
from data.graficos import  graf_var
from data.get_data import dict_species, get_page_penguins, get_distinct_ID, get_id_index, get_id_individual
import pandas as pd


st.set_page_config(page_title="Búsqueda de pingüinos", page_icon="🔍​")

st.markdown("# Búsqueda de pingüinos")
st.markdown(
    '''La base de datos proporcionaba un Individual ID que en algunos casos estaba asignado a individuo distintos.
     Por ello, se ha creado otro ID_index para cada uno de los datos recogidos (es único). '''
    )

st.sidebar.header("Búsqueda de pingüinos")
option = st.sidebar.selectbox( "Seleciona la variable ID por la que buscar", ["Individual ID", "ID_index"])

df_ID , df_index= get_distinct_ID()



if option == "ID_index" :

    user_input = st.text_input("Introduce el código", 0)

    if 0<=int(user_input)<df_index.shape[0]:

        df_id = pd.DataFrame(get_id_index(user_input))
        aux = df_id.iloc[0]["Individual ID"]
        st.markdown(f"## id={user_input} e Individual ID = {aux}")
        df_id = df_id.drop(["_id", "location", "Individual ID", "ID_index"], axis=1)
        st.table(df_id)

    else:
        st.text(f"Hay que introducir un número entre 0 y {df_index.shape[0]}")

else :

    user_input = st.text_input("Introduce el código", "N1A1")

    if user_input in df_ID["Individual ID"].unique():

        df_ind = pd.DataFrame(get_id_individual(user_input))

        for i in range(df_ind.shape[0]):
            penguin = df_ind.iloc[i]            
            aux = penguin["ID_index"]
            st.markdown(f"## id={aux} e Individual ID = {user_input}")
            penguin = penguin.drop(["_id", "location", "Individual ID", "ID_index"], axis=0)
            st.table(penguin)

    else:
        st.markdown("No existe ningún pingüino con ese ID")

