from folium import Map, Marker
from data.get_data import get_all_data, get_species_data, dict_geo, get_2_var
import pandas as pd
import plotly.express as px
import seaborn as sns
#https://github.com/randyzwitch/streamlit-folium


#Función que permite representar las coordenadas de cada una de las islas.
def mapa_Palmer():


    m = Map(location=[-64.7333304,-64.2333324],
               zoom_start=8)

    for place in dict_geo.keys():
        m.add_child(Marker([dict_geo[place]["latitud"], dict_geo[place]["longitud"]]
                       , tooltip=place+' Island'))
    
    return m


#Esta función permitirá representar las variables para cada una de las especies lo que permitirá estudiar
#las diferencias entre cada una de ellas.

def graf_var(species, var):
    data = get_2_var(var)
    data = data [  data["Species"].isin(species)  ]
     
    # Gráfica que representar el numero de huevos puestos para cada especie. Se agrupan por meses para facilitar 
    # la comprensión 
    if var =="Date Egg":
        df = pd.DataFrame()
        data[var] = data[var].astype('datetime64[ns]')

        for sp in species:
            df_aux = ( data[data['Species'] == sp].groupby(by=var).count().reset_index() ).resample(rule='M', on=var).sum()
            df_aux.rename(columns = {'Species':'Number'}, inplace = True)
            df_aux["Species"] = sp
            df =pd.concat([df, df_aux], axis=0)
        
        df.reset_index(inplace=True)
        fig = px.line(df, x=var, y='Number', color="Species", title = var+ ' Distribution amongst each species')
        return fig

    #Estas son las gráficas para el resto de variables categóricas (gráfico de barras) 

    elif type(data.iloc[0][var])==str:
        df = data.groupby(by='Species').count()
        for value in list(data[var].unique()):
            
            df[value] =data[data[var] == value].groupby(by='Species').count()[var]
            
        df.drop(var, axis = 1, inplace = True)   
        df = df.reset_index()
     
        fig = px.bar(df, 
                    x='Species', 
                    y = list(data[var].unique()), 
                    title = var+ ' Distribution amongst each species'
                    )
    
    # Gráfico barras para las variables categóricas

    else: 
        fig = px.box(data, 
                    x="Species", 
                    y=var, 
                    points="all", 
                    color="Species" ,
                    title = var+ ' Distribution amongst each species', 
                    width=900, 
                    height = 970
                    )
    
    return fig


# Función que representa las correlaciones de las variables numéricas

def graf_corr():
    data = get_all_data()
    data = data.drop(["Individual ID"], axis=1)
    fig = px.imshow(data.corr(),
                    text_auto = True,
                    width=700, 
                    height = 770
                    )
    return fig 

# Función que permite enfrentar dos variables numéricas

def graf_2var(species, list_var):

    data = get_species_data(species)

    """
    if list_var[0]==list_var[1]:
        data = data[["Species", list_var[0]]]
        fig = sns.kdeplot(data[list_var[0]], hue = df["Species"], shade = True)
    else:
    """
    data = data[["Species", list_var[0], list_var[1]]]
    fig = px.scatter( data, 
                    x=list_var[0], 
                    y=list_var[1], 
                    color="Species", 
                    title ="Relación between "+list_var[0]+" y "+list_var[1])
    
    return fig 


    


        






    
    