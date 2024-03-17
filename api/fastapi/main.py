from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import auth, user

app = FastAPI()
app.include_router(user.router)
app.include_router(auth.router)


allow_origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allow_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}
