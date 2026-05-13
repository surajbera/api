from fastapi import FastAPI

app = FastAPI()

@app.get('/user/admin')
def admin():
  return {"This is an admin page"}

@app.get('/user/{username}')
def profile(username: str):
  return {f"This is a profile page for the user: {username}"}

@app.get('/products')
def products(id: int = 1, price: float = 22.222): # these are query parameters not path parameters
  return {f"Product with an id: {id} and price: {price}"}

@app.get('/profile/{userid}/comments')
def comments(userid: int, commentid: int):
  return {f"Profile page for user: {userid} and comment with id: {commentid}"}