import streamlit as st
from data.graficos import graf_corr, graf_2var 
from data.get_data import dict_species, get_page_penguins
from c_sidebar.sidebar import Sidebar

st.set_page_config(page_title="Representación de variables numéricas", page_icon="📚")

st.markdown("# Representación de variables numéricas")
st.markdown('''En este apartado se entrará más en profundidad en ñas reñaciones que existen entre cada una de las
variables numéricas''')

chosen_multi , chosen_multi2 = Sidebar.var_num()

print(chosen_multi, chosen_multi2)

st.subheader("Gráfica de correlaciones entre variables numéricas")

st.markdown('''
La correlación es una medida estadística que expresa hasta qué punto dos variables están relacionadas linealmente (esto es, cambian conjuntamente a una tasa constante). 
Es una herramienta común para describir relaciones simples.
''')

st.plotly_chart(graf_corr())

st.subheader("Enfrentamiento de variables")
st.markdown('''
    Ahora se enfrentarán dos de las variables para observar cómo se distribuyen cada una de ellas según lo que valga la otra
    y la especie de pingüino a la que hagan referencia los datos
''')


if len(chosen_multi)==2 and chosen_multi2!=[]:
    fig = graf_2var(chosen_multi2, chosen_multi)
    if fig != None:
        st.plotly_chart(fig)




click = st.button('Click me')
print(click)

