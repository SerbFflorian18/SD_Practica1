import redis

redis_client = redis.Redis(host='localhost', port=6379, db=0)

users = {
    "user1": "192.168.1.101",
    "user2": "192.168.1.102",
    "user3": "192.168.1.103",
}

for user, direccion in users.items():
    redis_client.hset("usuarios", user, direccion)

print("Usuarios registrados en Redis:")
