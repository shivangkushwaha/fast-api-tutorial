from fastapi import FastAPI,Response,status,HTTPException
from fastapi.params import Body
from validators.post import Post
app = FastAPI()

@app.get("/")
async def root():
    return   {"message": "Hello World"}


@app.get("/posts")
async def get_posts():
    return   {"message": "Hello World"}

@app.get("/posts/{id}")
async def get_posts_by_id(id:int):
    print("requested Id",id)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Not found with ID")
    return   {"message": "Hello World"}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
async def create_posts(post: Post):
    print('payload',post)
    print('post.dict()', post.dict())
    return   {"message": post.dict()}

