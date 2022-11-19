import re
import requests
import json
import pandas as pd

# diccionarios

dict_geo = {'Biscoe': {'latitud': -64.7999968, 'longitud': -63.83333},
        'Dream': {'latitud': -64.7333304, 'longitud': -64.2333324},
        'Torgersen': {'latitud': -64.7666636, 'longitud': -64.083333}}

dict_species = {"adelie": "Adelie Penguin (Pygoscelis adeliae)",
                "chinstrap": "Chinstrap penguin (Pygoscelis antarctica)",
                "gentoo": "Gentoo penguin (Pygoscelis papua)"}

dict_router ={'island': 'Island', 
    'clutch': 'Clutch Completion',
    'egg':  'Date Egg',
    'length': 'Culmen Length (mm)', 
    'depth' : 'Culmen Depth (mm)',
    "flipper" : 'Flipper Length (mm)',
    'bodymass' : 'Body Mass (g)', 
    'sex': 'Sex', 
    'delta15': 'Delta 15 N (o/oo)', 
     'delta13' : 'Delta 13 C (o/oo)'
     }

list_num = ['Culmen Length (mm)', 'Culmen Depth (mm)', 'Flipper Length (mm)', 'Body Mass (g)',  'Delta 15 N (o/oo)', 'Delta 13 C (o/oo)']


# funcion que te devuelve un numero determinado de elementos de la base de datos
def get_page_penguins(page_number=0):
    return requests.get("http://127.0.0.1:8000/penguins?num_page="+str(page_number)).json()["results"]


# Funcion que itera por las páginas de datos de Mongo db y devuelve todos los datos
def iter_pages(url):
    n =0
    df =pd.DataFrame()
    while (True):

        res = requests.get(url+"?num_page="+str(n)).json()["results"] 
        if res == []:
            break
        
        df = pd.concat([df, pd.DataFrame(res)], axis=0)

        
        n += 1
    return df




# Esta función nos permite obtener todos valores del dataframe

def get_all_data():
    return iter_pages( "http://127.0.0.1:8000/penguins" ) 

#Esta función devuelve un df que contiene la variable species y la indicada en el url

def get_2_var(name):
    key_var = list(dict_router.keys())[list(dict_router.values()).index(name)] #devuelve la key de la variable pasada
    return pd.DataFrame(requests.get("http://127.0.0.1:8000/penguins/"+str(key_var)).json())

# Función que devuelve todos  los datos de las species indicadas
def get_species_data(species):
    df = pd.DataFrame()
    for sp in species :
        key_sp=list(dict_species.keys())[list(dict_species.values()).index(sp)]
        df_sp = iter_pages('http://127.0.0.1:8000/penguins/species/'+key_sp)

        df = pd.concat([df,df_sp], axis=0)

    df.reset_index(drop=True, inplace =True)
    return df



