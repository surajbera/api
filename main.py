from fastapi import FastAPI
from pydantic import BaseModel, Field, HttpUrl
from typing import Set, List

from starlette.middleware import base

class Profile(BaseModel):
  name: str
  email: str
  age: int

class Image(BaseModel):
  url: HttpUrl
  name: str

class Product(BaseModel):
  name: str
  price: int = Field(title="title of the product", 
  description="description of the product",
  gt=0, lt=1000000)
  discount: int
  discounted_price: float
  tags: Set[str] = Field(default=["electronics", "fashion"])
  image: List[Image]

class Offer(BaseModel):
  name: str
  description: str
  price: float
  products: List[Product]

class User(BaseModel):
  name: str
  email: str

app = FastAPI()

@app.post('/offer')
def add_offer(offer: Offer):
  return { offer }

@app.post('/purchase')
def purchase(user: User, product: Product):
  return { "user": user, "product": product }