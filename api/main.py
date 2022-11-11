from fastapi import FastAPI
from bson import json_util
from json import loads
from routers import penguin

app = FastAPI()


#Incluimos los endpoints de los ficheros
app.include_router(penguin.router)

@app.get("/")
def raiz():
    return {
        "message":"Bienvenido a la Api de los Pingüinos"
    }

@app.get("info")
def info():
    return{
        #explicar brevemente los router
    }
