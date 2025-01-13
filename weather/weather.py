import json
import os

import requests
from dotenv import load_dotenv

from .cache import get_cache, set_cache

load_dotenv(r"../.")

api_key = os.getenv("KEY_WEATHER_API")
base_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline"

def fetch_weather(location):
    cache_key = f"weather_{location}"
    cache_data = get_cache(cache_key)

    if cache_data:
        print("Cache hit")
        return json.loads(cache_data)

    url = f"{base_url}/{location}?unitGroup=metric&include=days&key={api_key}&contentType=json"
    response = requests.get(url)
    data = response.json()

    print("Cache miss")
    set_cache(cache_key, json.dumps(data), 60 * 60 * 2)
        
    return data