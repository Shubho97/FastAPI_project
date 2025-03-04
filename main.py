from fastapi import FastAPI

app = FastAPI()

@app.get("/about")
def about():
    return {"data": {"name": "Shubho", "id": 2}}

@app.get("/home")
def home():
    return "this is home page!!"

@app.get("/about/blob")
def bob():
    return "this is blob page!! \n choose the number {1,2,3}"

@app.get("/about/blob/{id}")
def id(id):
    return {"data": {"id": id}}
