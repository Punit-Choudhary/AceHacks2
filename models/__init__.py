import config.secrets as secrets
from pymongo import MongoClient


mongo_client = MongoClient(secrets.MONGO_URI, serverSelectionTimeoutMS=5000)
