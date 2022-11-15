from folium import Map, Marker
from data.get_data import get_rest_data

#https://github.com/randyzwitch/streamlit-folium
def mapa_Palmer():
    dict_geo ={'Biscoe': {'latitud': -65.4333316, 'longitud': -65.499998},
        'Dream': {'latitud': -64.7333304, 'longitud': -64.2333324},
        'Torgersen': {'latitud': -64.7666636, 'longitud': -64.083333}}
    m = Map(zoom_start=500)
    for place in dict_geo.keys():
        m.add_child(Marker([dict_geo[place]["latitud"], dict_geo[place]["longitud"]]
                       , tooltip=place+' Island'))
    
    return m


#Esta función permitirá representar las variables para cada una de las especies lo que permitirá estudiar
#las diferencias entre cada una de ellas.

def graf_var(species, var):
    data = get_rest_data('?project={"_id":0, "Species":1,'+ f'"{var}"'+': 1}')
    if type(data[0][var]==str):
        print(1)






    
    