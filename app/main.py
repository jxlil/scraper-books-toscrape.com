#!/usr/bin/env python3.10

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

from api.v1.scrape.router import router as scrape_router


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(scrape_router)
