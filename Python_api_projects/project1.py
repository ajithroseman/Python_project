from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()
My_post = [{"id":1,"Title":"slime isekai","Description":"Demon lord"},
           {"id":2,"Title":"Overlord","Description":"Isekai to video game"}]
class Post(BaseModel):
    Title : str
    Anime_Type : str
    Description : str
    Published :bool = True
    Rating : Optional[int] = None
@app.get("/")
async def root():
    return {"message":"hello world"}
@app.get("/a_post")
def anime_post():
    return {"Post:":My_post}
@app.post("/post")
def post_post(post : Post):
    print(post)
    print(post.dict())
    return {"Post:NewPost"}
