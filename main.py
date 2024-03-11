# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "Python FastAPI Is Running..."}


@app.get("/test/call")
def read_root():
    return {"Hello": "this is a test endpoint"}

@app.get("/test/call2")
def read_root():
    return {"Hello": "this is a test endpoint 2"}