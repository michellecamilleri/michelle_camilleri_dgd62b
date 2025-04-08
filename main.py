from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel, Field, constr
from motor.motor_asyncio import AsyncIOMotorClient
import base64
import os
import re
from dotenv import load_dotenv

# Loading connection string from the .env file 
load_dotenv()
app = FastAPI()

# Initialize MongoDB connection
def get_db():
    client = AsyncIOMotorClient(os.getenv("MONGODB_CONNECTION_STRING"))
    return client["multimedia_db"]

# Close MongoDB connection
async def shutdown_db():
    client = AsyncIOMotorClient(os.getenv("MONGODB_CONNECTION_STRING"))
    client.close()

# Validate player name and score input
class PlayerScore(BaseModel):
    player_name: constr(min_length=1, max_length=50, pattern=r"^[a-zA-Z0-9_ ]+$")
    score: int

# Sanitize file names to reduce injection risks
def sanitize_input(input_str: str) -> str:
    return re.sub(r"[^\w\s.-]", "", input_str).strip()


@app.post("/upload_sprite/")
async def upload_sprite(file: UploadFile = File(...)):
    '''
    enpoint to upload sprite files
    - encodes the file in base64
    - saves it to the database, using the file name, encoded data, and a description in the 'sprites' collection
    - returns a message and the id of the inserted document
    '''

    try:
        db = get_db()
        content = await file.read()
        encoded = base64.b64encode(content).decode("utf-8")

        sprite_doc = {
            "file_name": file.filename,
            "file_data": encoded,
            "description": "Sprite uploaded via Base64"
        }

        result = await db.sprites.insert_one(sprite_doc)
        return {"message": "Sprite uploaded", "id": str(result.inserted_id)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Sprite upload failed: {str(e)}")
    finally:
        await shutdown_db()

@app.post("/upload_audio/")
async def upload_audio(file: UploadFile = File(...)):
    '''
    enpoint to upload audio files
    - encodes the file in base64
    - saves it to the database, using the file name, encoded data, and a description in the 'audio' collection
    - returns a message and the id of the inserted document
    '''
    try:
        db = get_db()
        content = await file.read()
        encoded = base64.b64encode(content).decode("utf-8")

        audio_doc = {
            "file_name": file.filename,
            "file_data": encoded,
            "description": "Audio uploaded via Base64"
        }

        result = await db.audio.insert_one(audio_doc)
        return {"message": "Audio uploaded", "id": str(result.inserted_id)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Audio upload failed: {str(e)}")
    finally:
        await shutdown_db()

@app.post("/player_score")
async def add_score(score: PlayerScore):
    '''
    enpoint to player score files
    - validates the player name and score using the PlayerScore model
    - saves it to the database, using the player name and score in the 'scores' collection
    - returns a message and the id of the inserted document
    '''
    try:
        db = get_db()
        score_doc = score.dict()
        result = await db.scores.insert_one(score_doc)
        return {"message": "Score recorded", "id": str(result.inserted_id)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Score submission failed: {str(e)}")
    finally:
        await shutdown_db()
