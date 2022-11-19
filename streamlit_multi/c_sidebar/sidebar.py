import streamlit as st
from data.get_data import dict_species, list_num


class Sidebar:   
    def var():
        with st.sidebar:
            st.header("Estudio de variables según la especie")
            chosen_multi = st.multiselect('Elige las especies de pingüinos', dict_species.values())
            st.header("Mostrar gráficos necesitados")
            info = st.checkbox("Island")
            info2 = st.checkbox('Clutch Completion')
            info3 = st.checkbox('Date Egg')
            info4 = st.checkbox('Culmen Length (mm)')
            info5 = st.checkbox('Culmen Depth (mm)')
            info6 = st.checkbox('Flipper Length (mm)')
            info7 = st.checkbox('Body Mass (g)')
            info8 = st.checkbox('Sex')
            info9 = st.checkbox('Delta 15 N (o/oo)')
            info10 = st.checkbox('Delta 13 C (o/oo)')

            return chosen_multi, info, info2, info3, info4, info5, info6, info7, info8, info9, info10
    def var_num():
        with st.sidebar:
            st.header(" Selecciona dos variables y las especies")
            chosen_multi =st.multiselect('Elige las dos variables a enfrentar', list_num, max_selections = 2, key="1")
            chosen_multi2 = st.multiselect('Elige las especies de pingüinos que se presentarán', dict_species.values(), key="2")
            return chosen_multi, chosen_multi2
 
    

