from fastapi import FastAPI, HTTPException

from .weather import fetch_weather

app = FastAPI()

@app.get("/")
def read_root():
    return {"Application": "weather API that fetches and returns weather data."}

@app.get("/{location}")
async def get_weather(location: str):
    try:
        data = fetch_weather(location)
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
