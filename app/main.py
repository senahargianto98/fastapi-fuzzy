from fastapi import FastAPI
from blog import  models
from blog.database import engine
from blog.routers import user, authentication, test, fuzzy
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(test.router)
app.include_router(fuzzy.router)
