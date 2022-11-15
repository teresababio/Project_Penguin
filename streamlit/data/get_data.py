import re
import requests
import json
import ast

#dict que contiene las especies
dict_species = {"Adelie Penguin": "Adelie Penguin (Pygoscelis adeliae)",
                "Chinstrap penguin": "Chinstrap penguin (Pygoscelis antarctica)",
                "Gentoo penguin": "Gentoo penguin (Pygoscelis papua)"}

#funcion que te devuelve un numero determinado de elementos de la base de datos
def get_n_penguins(n):
    return requests.get(f"http://127.0.0.1:8000/range/penguins/{n}").json()



#Esta función nos permite obtener ciertos valores del dataframe
def get_rest_data(rest):
    return requests.get("http://127.0.0.1:8000/rest_dict/penguins/"+rest).json()
    



