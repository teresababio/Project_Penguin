import streamlit as st
from data.graficos import  graf_var
from data.get_data import dict_species, get_page_penguins


st.set_page_config(page_title="Búsqueda de pingüinos", page_icon="🔍​")

st.markdown("# Búsqueda de pingüinos")
st.sidebar.header("Búsqueda de pingüinos")
option = st.sidebar.selectbox( 'Seleciona la variable ID por la que buscar', list_var)

