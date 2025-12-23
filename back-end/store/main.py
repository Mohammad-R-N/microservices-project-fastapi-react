from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import orders

app = FastAPI()

app.include_router(orders.router)

origins = [
    "http://localhost",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
