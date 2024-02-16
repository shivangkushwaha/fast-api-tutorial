from pydantic import BaseModel
from typing import Optional

class Post (BaseModel):
    title:str
    content:str
    published:bool
    rating:Optional[int] = None
     