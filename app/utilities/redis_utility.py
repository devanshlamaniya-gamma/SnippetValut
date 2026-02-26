import os

import redis
from dotenv import load_dotenv

load_dotenv()

# redis_client = redis.Redis(
#     # host="localhost",
#     host="127.0.0.1",
#     port=6379,
#     decode_responses=True,
# )
REDIS_URL = os.getenv("REDIS_URL")
print(REDIS_URL)
# REDIS_SECRET_TOKEN = os.getenv("UPSTASH_REDIS_REST_TOKEN")

# redis_client = redis.Redis(url=REDIS_URL, token= REDIS_SECRET_TOKEN , host=6379 , decode_responses=True)

redis_client = redis.Redis.from_url(REDIS_URL, decode_responses=True)


# redis_client.set("test", "hello")


# print(redis_client.get("test"))
