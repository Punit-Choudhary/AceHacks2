from dotenv import load_dotenv
from os import environ


load_dotenv()


SECRET_KEY = environ['SECRET_KEY']
MONGO_URI = environ['MONGO_URI']
