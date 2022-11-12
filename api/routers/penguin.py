from fastapi import APIRouter
from database.mongodb import db

from bson import json_util
from json import loads

router = APIRouter()
#Mostrar todos los datos
@router.get("/all/penguins")
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
        return loads(json_util.dumps(res))

#Mostrar todos los pinguinos de una especie determinada

@router.get("/species/penguins/{specie}")
def get_penguins(specie:str):
        res = list(db["penguin_data"].find({"Species": specie}))
        return loads(json_util.dumps(res))


#Mostrar todos los pinguinos de un sexo

@router.get("/species/penguins/{sexo}")
def get_penguins(sexo:str):
        res = list(db["penguin_data"].find({"Sex": sexo}))
        return loads(json_util.dumps(res))

#Preguntar si es posible añadir dos restricciones en la busqueda
