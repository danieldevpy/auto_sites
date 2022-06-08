from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import asyncio
from playwright.async_api import async_playwright
from pydantic import BaseModel
from multiprocessing import Process, Queue
from playwright.sync_api import sync_playwright
import time

origins = ["*"]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Badge(BaseModel):
    site: str
    time: str

def abrir()

class Chave(url, queue)

    site = {'site':site, 'url':url}

while: True
    if site:
        print('tem')
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(url.site)
            titulo = page.title()
            queue.put(titulo)
            time.sleep(3)
            browser.close()


@app.post('/')
def action(url: Badge):
    queue = Queue()
    p = Process(target=clicar, args=(url,queue))
    p.start()
    return {'title':queue.get()}
    p.join()

@app.post('/create')
def create_badge(create: Badge):
    return create

