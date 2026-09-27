from fastapi import FastAPI

app = FastAPI()


@app.post("/create-users")
def create_user(name: str, age: int, ph_no: int):
	return {
		"message": "User create successfully",
		"name": name,
		"age": age,
		"ph_no": ph_no
		}

#use dictionary		
@app.post("/create-users/inf")
def create_user_inf(user: dict):
    return {
        "message": "User created",
        "data": user
        }

