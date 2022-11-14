from folium import Map, Marker

#https://github.com/randyzwitch/streamlit-folium
def mapa_Palmer():
    dict_geo ={'Biscoe': {'latitud': -65.4333316, 'longitud': -65.499998},
        'Dream': {'latitud': -64.7333304, 'longitud': -64.2333324},
        'Torgersen': {'latitud': -64.7666636, 'longitud': -64.083333}}
    m = Map(location =[ -64.7333304, -64.2333324], zoom_start=500)
    for place in dict_geo.keys():
        m.add_child(Marker([dict_geo[place]["latitud"], dict_geo[place]["longitud"]]
                       , tooltip=place+' Island'))
    
    return m

    