from fastapi import FastAPI  # uvicorn main:app --reload
from data_base.data_base import SessionLocal
from table.user import UserTable
from models.user import UserModel

app = FastAPI()


@app.get("/")
def getAllUsers():
    bd = SessionLocal()
    users = bd.query(UserTable).all()
    bd.close()
    return users


# cretae user
@app.post("/")
def createUser(user: UserModel):
    bd = SessionLocal()
    newUser = UserTable(**user.dict())
    bd.add(newUser)
    bd.commit()
    bd.close()
    return {"message": "User created successfully", "user": user}
