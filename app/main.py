from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
import json

app = FastAPI()

frontendUrl = os.getenv("FRONTEND_URL", "http://localhost:5173/")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[frontendUrl],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def Home():
    return {"massage": "Hello Saiful Islam Rafi!"}

def projects():
    with open('projects.json', 'r') as f:
        return json.load(f)

@app.get("/projects")
def get_projects(): 
    return projects()


def achivements():
    with open('achivement.json', 'r') as f:
        return json.load(f)

@app.get("/achivements")
def get_achivements(): 
    return achivements()


