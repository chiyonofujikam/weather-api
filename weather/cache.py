import os

from dotenv import load_dotenv
from upstash_redis import Redis

load_dotenv(r"../.")

upstash_url = os.getenv('UPSTASH_URL')
upstash_token = os.getenv('UPSTASH_REDIS_TOKEN')

cache = Redis(url=upstash_url, token=upstash_token)

def set_cache(key, value, expire):
    cache.set(key, value, ex=expire)

def get_cache(key):
    return cache.get(key)
