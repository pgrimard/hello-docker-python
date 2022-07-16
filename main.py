import sys
from dataclasses import dataclass

from fastapi import FastAPI, HTTPException, Response

app = FastAPI()

items_raw = [
    {
        "item_number": "cofmac",
        "description": "Coffee Machine"
    },
    {
        "item_number": "cofbea",
        "description": "Coffee Beans"
    },
    {
        "item_number": "espresso_mac",
        "description": "Espresso Machine"
    },
]

@dataclass
class Item:
    item_number: str
    description: str

items: dict = {}

for item_raw in items_raw:
    item = Item(**item_raw)
    items[item.item_number] = item

@app.get("/")
def root() -> Response:
    return Response("The server is running!")

@app.get("/items/{item_number}")
def get_item(item_number: str) -> Item:
    if item_number not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_number]

@app.get("/about")
def get_about():
    return sys.version