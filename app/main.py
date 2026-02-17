from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return "this is root"