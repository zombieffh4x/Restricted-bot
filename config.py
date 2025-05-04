# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "28280833"))
API_HASH = getenv("API_HASH", "2b5552b757a5a0c775723bcddbbfa6be")
BOT_TOKEN = getenv("BOT_TOKEN", "7484660141:AAGJXpM-VNfIIP-nSpK8N0tjFJnTtBRPAP8")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7758430598").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://sujay5372222222:sujay5372222222@cluster0000007.fdufm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0000007")
LOG_GROUP = getenv("LOG_GROUP", "-1002262545667")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002483720229"))
