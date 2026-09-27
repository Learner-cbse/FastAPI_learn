
from fastapi import FastAPI

app = FastAPI()


@app.post("/create-users")
def create_user(name: str, age: int):
	return {
		"message": "User create successfully",
		"name": name,
		"age": age
		}
