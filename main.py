from typing import Optional
from fastapi import FastAPI
from enum import Enum
import requests

app = FastAPI()

# hello world
@app.get('/')
async def root():
    return {"message": "hello world!!!"}

# router with params
@app.get('/teste/{i}/')
async def teste(i:str):
    return {"id": i}


# using enum
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


# i can use one paht parameter in my response json
@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


# using query params
fake_items_db = [
                    {"item_name": "Foo"},
                    {"item_name": "Bar"},
                    {"item_name": "Baz"}
                ]

@app.get("/users/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]


# testing call one api with requests im my api code
@app.get("/pokemon/")
async def get_pokemon_name(name: str):
    pokedict = requests.get(
                                f"https://pokeapi.co/api/v2/pokemon/{name}"
                            ).json()
    return {"pokemon_name": pokedict["forms"][0]["name"]}


# i can set the optional query params to None follow this way
@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Optional[str] = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}


# use boolean
@app.get("/items2/{item_id}")
async def read_item2(item_id: str, q: Optional[str] = None, short: bool = False):
    item = {"item": item_id}
    if q:
        item.update({"q": q})
    
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}    
        )
    
    return item


    


