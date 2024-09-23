# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "26512964"))
API_HASH = getenv("API_HASH", "e5d187c6c7a0919ccb8866f76f655701")
BOT_TOKEN = getenv("BOT_TOKEN", "7797698648:AAHDcMWqqlirBcXPCgUYGK2ak7ky3kPGoqA")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6326227068").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://weloxa8533:WKmtuOzgMtTFGCrC@cluster0.jrz7hfn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", " -1002174768610")
CHANNEL_ID = int(getenv("CHANNEL_ID", " -1002471604336")
