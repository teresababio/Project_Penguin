from fastapi import APIRouter, HTTPException
from database.mongodb import db, find_collection, paginate
from bson import json_util
from json import loads
 


router = APIRouter()
# Mostrar todos los datos
@router.get("/penguins")
def get_penguins(num_page:int=0):

        # Validar page_number
        if num_page<0:
                raise HTTPException(status_code=400, detail="num_page debe ser positivo")


        page = paginate(num_page)
        res = page(find_collection("penguin_data"))
        return res



# Buscar un pinguino por su id
@router.get("/search/penguin/id/num/{_id}")
def get_penguins(_id: int):

        res = find_collection("penguin_data", {"ID_index" : {"$eq": _id}}) 
        return loads(json_util.dumps(res))

@router.get("/search/penguin/id/str/{_id}")
def get_penguins(_id: str):
        res =find_collection("penguin_data", {"Individual ID" : {"$eq": _id}}) 
        return loads(json_util.dumps(res))



# Mostrar los valores de cada una de las variables
@router.get("/distinct/penguin/{var}")
def get_penguins(var:str):
        res = list(db["penguin_data"].find({}).distinct(var))
        return res

# Mostrar todos los pinguinos de una especie determinada

@router.get("/penguins/species/{specie}")
def get_penguins(specie:str, num_page:int=0, var:str=""):
        dict_species = {"adelie": "Adelie Penguin (Pygoscelis adeliae)",
                "chinstrap": "Chinstrap penguin (Pygoscelis antarctica)",
                "gentoo": "Gentoo penguin (Pygoscelis papua)"}


        # Validar page_number
        if num_page<0:
                raise HTTPException(status_code=400, detail="num_page debe ser positivo")
        
        # Validar specie
        if specie not in dict_species.keys():
                raise HTTPException(status_code=400, detail="specie no incluida en la base de datos")

        page = paginate(num_page)
        res = page(find_collection("penguin_data",{"Species": dict_species[specie]}))
        return res



#Router para seleccionar una variable y la especie

@router.get("/penguins/clutch")
def get_penguins():
        res = find_collection("penguin_data", {}, {"_id":0 , "Species": 1 , 'Clutch Completion': 1})
        return loads(json_util.dumps(res))

@router.get("/penguins/island")
def get_penguins():
        res = find_collection("penguin_data", {}, {"_id":0 , "Species": 1 , 'Island': 1})
        return loads(json_util.dumps(res))

@router.get("/penguins/egg")
def get_penguins():
        res = find_collection("penguin_data", {}, {"_id":0 , "Species": 1 , 'Date Egg': 1})
        return loads(json_util.dumps(res))

@router.get("/penguins/length")
def get_penguins():
        res = find_collection("penguin_data", {}, {"_id":0 , "Species": 1 , 'Culmen Length (mm)': 1})
        return loads(json_util.dumps(res))

@router.get("/penguins/depth")
def get_penguins():
        res = find_collection("penguin_data", {}, {"_id":0 , "Species": 1 ,'Culmen Depth (mm)': 1})
        return loads(json_util.dumps(res))

@router.get("/penguins/flipper")
def get_penguins():
        res = find_collection("penguin_data", {}, {"_id":0 , "Species": 1 , 'Flipper Length (mm)': 1})
        return loads(json_util.dumps(res))

@router.get("/penguins/bodymass")
def get_penguins():
        res = find_collection("penguin_data", {}, {"_id":0 , "Species": 1 , 'Body Mass (g)': 1})
        return loads(json_util.dumps(res))

@router.get("/penguins/sex")
def get_penguins():
        res = find_collection("penguin_data", {}, {"_id":0, "Species": 1 , "Sex": 1})
        return loads(json_util.dumps(res))

@router.get("/penguins/delta15")
def get_penguins():
        res = find_collection("penguin_data", {}, {"_id":0, "Species": 1 , 'Delta 15 N (o/oo)': 1})
        return loads(json_util.dumps(res))

@router.get("/penguins/delta13")
def get_penguins():
        res = find_collection("penguin_data", {}, {"_id":0,  "Species": 1 , 'Delta 13 C (o/oo)': 1})
        return loads(json_util.dumps(res))

@router.get("/penguins/individualid")
def get_penguins():
        res = find_collection("penguin_data", {}, { "_id":0, 'Individual ID': 1})
        return loads(json_util.dumps(res))

@router.get("/penguins/idindex")
def get_penguins():
        res = find_collection("penguin_data", {}, { "_id":0, 'ID_index': 1})
        return loads(json_util.dumps(res))