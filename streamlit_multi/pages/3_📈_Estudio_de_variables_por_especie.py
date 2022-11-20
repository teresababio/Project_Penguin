import streamlit as st
from data.graficos import  graf_var
from data.get_data import dict_species, get_page_penguins
from c_sidebar.sidebar import Sidebar

st.set_page_config(page_title="Estudio de variables ", page_icon="📈")

st.markdown("# Estudio de variables según la especie")




st.header("Variables")
st.markdown('''En este apartado se grafican para cada una de las especies especificadas
                los datos de una de las  variables seleccionadas del conjunto de datos.''')
                
list_var = [var for  var in get_page_penguins()[0].keys()][5:-1]
list_var.remove("Stage")
list_var.remove("Individual ID")

family=Sidebar.var()
chosen_multi = family[0]
family = family [1:]
index_selec = [i for i in range(len(family)) if family[i]==True]

if chosen_multi and index_selec:
    for i in index_selec:
        fig = graf_var(chosen_multi, list_var[i])

        if fig != None:
            st.plotly_chart(fig)

click = st.button("Click me")
print(click)
