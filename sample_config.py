import os

api_id = 26548330
api_hash = os.environ.get("API_HASH", "244c3afd019c7b0cd1a8184cd2be2495")
bot_token = os.environ.get("7112965184:AAFOcOPfUswSABurDw99UryOU471fDoS0_4")
auth_users = os.environ.get("AUTH_USERS", "6890753169")
sudo_users = [int(num) for num in auth_users.split("6890753169")]
osowner_users = os.environ.get("OWNER_USERS", "6890753169")
owner_users = [int(num) for num in osowner_users.split("6890753169")]
