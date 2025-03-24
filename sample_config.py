import os

api_id = 29683927
api_hash = os.environ.get("API_HASH", "b2eb32ac1030edd8bc36c7b554ef6fc3")
bot_token = os.environ.get("7903348261:AAHboLSnCbsiWxEHlQLnOFv8D7ptkraC_xw")
auth_users = os.environ.get("AUTH_USERS", "5583858510")
sudo_users = [int(num) for num in auth_users.split(",")]
osowner_users = os.environ.get("OWNER_USERS", "5583858510")
owner_users = [int(num) for num in osowner_users.split(",")]
