from fastapi import FastAPI

from app.databse.db import Base, engine
from app.models.redistest_model import Test
from app.models.snippet_model import Snippet
from app.models.user_model import User
from app.routes.authentication_route import auth
from app.routes.snippet_route import snippet

app = FastAPI(
    title="CodeSnippet",
)

app.include_router(auth)
app.include_router(snippet)

print("app started now creating table")
Base.metadata.create_all(
    bind=engine
)  # ye kehta h ki base k andar jis jis bi table ka metadata h wo wo table bna do agr pehle se ni h toh
print("table created")


@app.get("/")
def root():
    return "this is root"
