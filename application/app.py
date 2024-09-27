from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

app = FastAPI()

# Sample data
items = {"hi", "there", "donot know why its been added"}

# Define a model for POST request data
class Item(BaseModel):
    name: str
    description: str

# GET endpoint 1: Retrieve an item by its key
@app.get("/items/{item_name}")
async def get_item(item_name: str):
    if item_name in items:
        return {"item_name": item_name, "description": items[item_name]}
    else:
        raise HTTPException(status_code=404, detail="Item not found")

# GET endpoint 2: Retrieve all items
@app.get("/items/")
async def get_all_items():
    return items

# POST endpoint 1: Create a new item
@app.post("/items/")
async def create_item(item: Item):
    if item.name in items:
        raise HTTPException(status_code=400, detail="Item already exists")
    items[item.name] = item.description
    return {"message": "Item created", "item": item}

# POST endpoint 2: Update an existing item
@app.post("/items/{item_name}")
async def update_item(item_name: str, item: Item):
    if item_name not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_name] = item.description
    return {"message": "Item updated", "item": item}

# Endpoint to call an external URL
@app.get("/external/")
async def call_external_url():
    external_url = "https://jsonplaceholder.typicode.com/todos/1"  # Example URL
    response = requests.get(external_url)
    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=response.status_code, detail="External request failed")

