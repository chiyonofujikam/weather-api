# weather-api

Solution to the roadmap.sh project Weather API : <https://roadmap.sh/projects/weather-api-wrapper-service>

## Setting Up the Virtual Environment and Running the Application

1- Ensure you're in the `./weather-api` directory, then run the following commands:

```bash
py -m venv .\.venv
.\.venv\Scripts\activate
.\.venv\Scripts\python.exe -m pip cache purge
.\.venv\Scripts\python.exe -m pip --no-cache-dir install -r ./requirements.txt
```

2- Cleaning "__pycache__" from the project:

```powershell
Get-ChildItem -Recurse -Directory -Filter "__pycache__" | Remove-Item -Recurse -Force
```

or

```bash
for /d /r %i in (__pycache__) do rmdir /s /q "%i"
```

3- Launching the Application, execute:

```bash
uvicorn weather:app --reload
```

## Features

* Weather Data Fetching: Retrieves weather data for a specified location using the Visual Crossing Weather API.
* Caching with Redis: Caches the weather data in Redis to reduce API calls and improve performance.
* Rate Limiting with Flask-Limiter: Limits the number of API requests a user can make to prevent abuse.

## Requirements

* FAST API
* Redis
* Visual Crossing Weather API Key
* upstash_redis
* uvicorn

## Environment variables

```bash
touch .env

KEY_WEATHER_API=your_visual_crossing_weather_api_key
UPSTASH_URL=your_upstash_url
UPSTASH_REDIS_TOKEN=your_upstash_token
```

if 'touch' cli isn't working:

```bash
npm install touch-cli -g
```

## Usage

```bash
curl "http://127.0.0.1:5000/London"
```
