import redis
import os
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

redis_client = redis.Redis.from_url(REDIS_URL , decode_responses = True )

# # Test write
# redis_client.set("test_key", "hello")

# # Test read
# print(redis_client.get("test_key"))