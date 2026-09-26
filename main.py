from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
	return {"message": "Hello World!"}

@app.get("/about")
def about():
    return {"message": "This is About page"}
    
#Path parameter
@app.get("/users/{user_name}")
def user(user_name):
    return {"Name": user_name}

#Path parameter with validation
@app.get("/users_/opt/{name_id}")
def get_user(name_id: int):
    return {"Name Id": name_id}

#Query parameter
@app.get("/_users_/query")
def user_get(names):
    return {"message": names}
 
#Optional query parameter
@app.get("/opt/query")
def opt_query(opt_name: str = None):
    return {"Name": opt_name}
    
#multiple Query parameter
@app.get("/items")
def get_item(item: str = None, price: int = 0):
    return {
        "Item": item,
        "Price": price
    }
