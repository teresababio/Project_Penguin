from fastapi import APIRouter, HTTPException
from database.mongodb import db, find_collection, paginate

 


router = APIRouter()
#Mostrar todos los datos
@router.get("/penguins")
def get_penguins(num_page:int=0):

        # Validar page_number
        if num_page<0:
                raise HTTPException(status_code=400, detail="num_page debe ser positivo")


        page = paginate(num_page)
        res = page(find_collection("penguin_data"))
        return res



#Buscar un pinguino por su id
@router.get("/search/penguin/id/{_id}")
def get_penguins(_id: int):
        page = paginate()
        res = page( find_collection("penguin_data", {"Individual ID" : {"$eq": _id}}) )
        return res

#Mostrar los valores de cada una de las variables
@router.get("/distinct/penguin/{var}")
def get_penguins(var:str):
        res = list(db["penguin_data"].find({}).distinct(var))
        return res

#Mostrar todos los pinguinos de una especie determinada

@router.get("/penguins/species/{specie}")
def get_penguins(specie:str, num_page:int=0):
        dict_species = {"adelie": "Adelie Penguin (Pygoscelis adeliae)",
                "chinstrap": "Chinstrap penguin (Pygoscelis antarctica)",
                "gentoo": "Gentoo penguin (Pygoscelis papua)"}


        # Validar page_number
        if num_page<0:
                raise HTTPException(status_code=400, detail="num_page debe ser positivo")
        
        #Validar specie
        if specie not in dict_species.keys():
                raise HTTPException(status_code=400, detail="specie no incluida en la base de datos")

        page = paginate(num_page)
        res = page(find_collection("penguin_data",{"Species": dict_species[specie]}))
        return res


#Mostrar todos los pinguinos de un sexo

@router.get("/penguins/sex/{sexo}")
def get_penguins(sexo:str, num_page:int=0):
        # Validar page_number
        if num_page<0:
                raise HTTPException(status_code=400, detail="num_page debe ser positivo")
        
        #Validar specie
        if sexo not in ["MALE", "FEMALE"]:
                raise HTTPException(status_code=400, detail="No existe ese genero")

        page = paginate(num_page)
        res = page(find_collection("penguin_data",{"Sex": sexo.upper()}))
        return res

