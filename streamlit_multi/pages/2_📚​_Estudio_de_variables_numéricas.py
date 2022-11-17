import streamlit as st
from data.graficos import graf_corr, graf_2var 
from data.get_data import dict_species, get_page_penguins

st.set_page_config(page_title="Estudio de variables numéricas")

st.markdown("# Estudio de variables numéricas")
st.sidebar.header("# Estudio de variables numéricas")

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

