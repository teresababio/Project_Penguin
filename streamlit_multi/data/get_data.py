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




# Esta función nos permite obtener ciertos valores del dataframe

def get_all_data():
    return iter_pages( "http://127.0.0.1:8000/penguins" ) 

# Función que devuelve los datos de las species indicadas


def get_species_data(species):
    df = pd.DataFrame()
    for sp in species :
        key_sp=list(dict_species.keys())[list(dict_species.values()).index(sp)]
        df_sp = iter_pages('http://127.0.0.1:8000/penguins/species/'+key_sp)

        df = pd.concat([df,df_sp], axis=0)

    df.reset_index(drop=True, inplace =True)
    return df



