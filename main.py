from fastapi import FastAPI # type: ignore

app = FastAPI()

@app.get("/about")
def about():
    return {"data": {"name": "Shubho"}}

@app.get("/home")
def home():
    return "this is home page!!"

@app.get("/about/blog")
def blog():
    return "this is blob page!! \n choose the number {1,2,3}"

@app.get("/blog/published")
def published(limit=10, published: bool = True):
    if published:
        return {f"{limit} published blog from db"}
    else:
        return {f"{limit} unpublished blog from db"}

@app.get("/about/blog/{id}")
def id(id:int):
    return {"data": {"id": id}}

@app.get("/about/blog/{id}/comments")
def comments(id:int):
    if id==1:
        return "comment_1"
    elif id==2:
        return "comment_2"
    else:
        return "no comment"