# this is main file 
from fastapi import FastAPI
from app.databse.db import Base ,engine
from app.models.user_model import User
from app.models.snippet_model import Snippet
from app.models.test_model import Test
from app.routes.authentication_route import auth

app = FastAPI(title="CodeSnippet")

app.include_router(auth)

print("app started now creating table")
Base.metadata.create_all(bind = engine)
print("table created")

@app.get("/")
def root():
    return "this is root"