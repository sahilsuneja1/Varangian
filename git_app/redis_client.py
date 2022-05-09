import redis
import json

class RedisClient():
    def __init__(self, serverIP=None):
        self.redis_client = None
        if not serverIP:
            return
        try:
            self.redis_client = redis.Redis(host=serverIP, port=6379)
        except redis.RedisError as e:
            print(f"Error connecting to redis: {e}")
            return


    def get_json(self, key):
        try:
            val = self.get(key)
            if not val:
                return
            return json.loads(val)
        except( ValueError, TypeError) as e:
            print(f"Json read error: {e}")
            return False
    
    
    def set_json(self, key, val):
        try:
            return self.set(key, json.dumps(val))
        except( ValueError, TypeError) as e:
            print(f"Json error: {e}")
            return False


    def get(self, key):
        if not self.redis_client:
            return
        try:
            val = self.redis_client.get(key)
            return val.decode()
        except redis.RedisError as e:
            print(f"Error getting key: {e}")
            return False


    def set(self, key, val):
        if not self.redis_client:
            return
        try:
            self.redis_client.set(key, val)
            return True
        except redis.RedisError as e:
            print(f"Error setting key: {e}")
            return False



