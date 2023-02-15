from fastapi import FastAPI
import model
from config import engine
import router
from fastapi.middleware.cors import CORSMiddleware

model.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def home():
    return {"Home": "/"}


app.include_router(router=router.router, prefix="/user", tags=["user"])
