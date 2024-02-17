from fastapi import FastAPI
from .routes import users
from config.openapi import tags_metadata

app = FastAPI(
    title="Users API",
    description="a REST API using python and mysql",
    version="0.0.1",
    openapi_tags=tags_metadata,

    
)

app.include_router(users.users)