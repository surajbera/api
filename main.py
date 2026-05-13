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

app = FastAPI()

@app.post('/addproduct/{product_id}')
def addproduct(product: Product, product_id: int, category: str):
  product.discounted_price = product.price - (product.discount / 100 * product.price)
  return { "product_id": product_id, "product": product, "category": category }