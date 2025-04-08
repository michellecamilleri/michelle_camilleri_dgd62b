from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient
import base64
import os
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()


# Connect to Mongo Atlas
MONGODB_CONNECTION_STRING = os.getenv("MONGODB_CONNECTION_STRING")
client = AsyncIOMotorClient(MONGODB_CONNECTION_STRING)
db = client.multimedia_db

class PlayerScore(BaseModel):
    player_name: str
    score: int

@app.post("/upload_sprite/")
async def upload_sprite(file: UploadFile = File(...)):
    content = await file.read()
    encoded = base64.b64encode(content).decode("utf-8")

    sprite_doc = {
        "file_name": file.filename,
        "file_data": encoded,
        "description": "Sprite uploaded via Base64"
    }

    result = await db.sprites.insert_one(sprite_doc)
    return {"message": "Sprite uploaded", "id": str(result.inserted_id)}

@app.post("/upload_audio/")
async def upload_audio(file: UploadFile = File(...)):
    content = await file.read()
    encoded = base64.b64encode(content).decode("utf-8")

    audio_doc = {
        "file_name": file.filename,
        "file_name": encoded,
        "description": "Audio uploaded via Base64"
    }

    result = await db.audio.insert_one(audio_doc)
    return {"message": "Audio uploaded", "id": str(result.inserted_id)}

@app.post("/player_score")
async def add_score(score: PlayerScore):
    score_doc = score.dict()
    result = await db.scores.insert_one(score_doc)
    return {"message": "Score recorded", "id": str(result.inserted_id)}
