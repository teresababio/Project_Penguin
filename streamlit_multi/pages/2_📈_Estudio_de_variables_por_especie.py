import streamlit as st
from data.graficos import  graf_var
from data.get_data import dict_species, get_page_penguins


st.set_page_config(page_title="Estudio de variables ", page_icon="📈")

st.markdown("# Estudio de variables según la especie")
st.sidebar.header("Estudio de variables según la especie")

st.header('Variables')
st.markdown('''En este apartado se grafican para cada una de las especies especificadas
                los datos de una de las  variables del conjunto de datos seleccionadas.''')
                
chosen_multi = st.multiselect('Elige las especies de pingüinos', dict_species.values(), key="1")
list_var = [var for  var in get_page_penguins()[0].keys()][5:-1]
#list_var.remove('Clutch Completion')
list_var.remove('Stage')
option = st.selectbox( 'Seleciona la variable a representar', list_var)


if chosen_multi:
    fig = graf_var(chosen_multi, option)

    if fig != None:
        st.plotly_chart(fig)

click = st.button('Click me')
print(click)
