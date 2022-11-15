from fastapi import APIRouter
from database.mongodb import db
from bson import json_util
from json import loads

router = APIRouter()
#Mostrar todos los datos
@router.get("/penguins")
def get_penguins():
        res = list(db["penguin_data"].find({}))
        return loads(json_util.dumps(res))

#Mostrar los n primeros pinguinos
@router.get("/range/penguins/{numero}")
def get_penguins(numero:int):
        res = list(db["penguin_data"].find({}).limit(numero))
        return loads(json_util.dumps(res))

#Buscar un pinguino por su id
@router.get("/search/penguin/id/{_id}")
def get_penguins(_id: int):
        res = list(db["penguin_data"].find({"Individual ID" : {"$eq": _id}}))
        return loads(json_util.dumps(res))

#Mostrar las especies de pinguinos que hay
@router.get("/distinct/penguin/species")
def get_penguins():
        res = list(db["penguin_data"].find({}).distinct("Species"))
        return res

#Mostrar todos los pinguinos de una especie determinada

@router.get("/species/penguins/{specie}")
def get_penguins(specie:str):
        res = list(db["penguin_data"].find({"Species": specie}))
        return loads(json_util.dumps(res))


#Mostrar todos los pinguinos de un sexo

@router.get("/sex/penguins/{sexo}")
def get_penguins(sexo:str):
        print(sexo.upper())
        res = list(db["penguin_data"].find({"Sex": sexo.upper()}))
        return loads(json_util.dumps(res))


#El siguiente router nos permite hacer operaciones que contengan más de una restricción. Poner comillas dobles en los
#string al pasar por los web parameters

#Ejemplo:  http://127.0.0.1:8000/rest_dict/penguins/?list_rest=[{"Sex": "MALE"}, {"Species":   "Adelie Penguin (Pygoscelis adeliae)" 

@router.get("/rest_dict/penguins/")
def get_penguins(list_rest: str ='{}', operator:str ="$and", project : str =""):
        if list_rest=='{}':
                filt={}
        else:
                if "," not in list_rest:
                        list_rest = list_rest.strip('][')
                        filt = loads(list_rest)
                else:
                        list_rest = list_rest.strip('][').split(', ')
                        list_rest = [loads(elem) for elem in list_rest]
                        filt ={ operator: list_rest}
        if not project:
                project={}
        else:
                project = loads(project)

        res = list(db["penguin_data"].find(filt , project))
        return loads(json_util.dumps(res))

 
#Falta router para geoqueries que se deja para cuando se haga