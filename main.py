from fastapi import FastAPI
from pydantic import BaseModel

class Profile(BaseModel):
  name: str
  email: str
  age: int

class Product(BaseModel):
  name: str
  price: float
  discount: int
  discounted_price: float

class User(BaseModel):
  name: str
  email: str

app = FastAPI()

@app.post('/purchase')
def purchase(user: User, product: Product):
  return { "user": user, "product": product }