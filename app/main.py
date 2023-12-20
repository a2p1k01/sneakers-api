from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from models.models import items

app = FastAPI(title='Sneaker API', version='1.0.0')
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items")
async def get_items(sortBy: str = 'name', title: str = ""):
    items_searched = [item for item in items if title.upper() in item['title'].upper()]
    if sortBy == 'name':
        sneakers = sorted(items_searched, key=lambda d: d['title'])
    elif sortBy == 'price':
        sneakers = sorted(items_searched, key=lambda d: d['price'])
    else:
        sneakers = sorted(items_searched, key=lambda d: d['price'], reverse=True)
    return sneakers
