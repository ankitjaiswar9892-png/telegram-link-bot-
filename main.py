import os
import logging
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

logging.basicConfig(level=logging.INFO)
log = logging.getLogger("worker")

app = FastAPI()

class Update(BaseModel):
    update_id: int | None = None
    message: dict | None = None

TOKEN = os.getenv("BOT_TOKEN", "")

@app.post("/webhook")
async def webhook(update: Update):
    log.info("Received update: %s", update.model_dump())
    return {"ok": True}

@app.get("/")
async def root():
    return {"status": "running"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
