from fastapi import FastAPI

from utils import get_items as load_items

app = FastAPI()

items = load_items()


@app.get("/items")
def get_items():
    return items
