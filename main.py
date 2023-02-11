from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {'message': 'welcome to monopoly. to start a game, follow the link', 'link': 'http://localhost:8000/start'}


@app.get("/start")
def start():
    return {'message': 'if you want to override the default settings, please follow the link. otherwise, POST the current link.', 'link': 'http://localhost:8000/config'}

@app.post("/start")
def start_post():
    return {}