from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
	return {"message": "Hello World!"}

@app.get("/about")
def about():
    return {"message": "This is About page"}
    
@app.get("/users")
def user(user_name: str):
    return {"Name": user_name}

    

