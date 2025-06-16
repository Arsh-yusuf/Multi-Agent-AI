import os
from dotenv import load_dotenv

load_dotenv()

WEATHERAPI_KEY = os.getenv("WEATHERAPI_KEY")
NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")
