import os
from dotenv import load_dotenv
load_dotenv()

print("loaded")

twitter = {
  "consumer_key": os.getenv("TWITTER_CONSUMER_KEY"),
  "consumer_secret": os.getenv("TWITTER_CONSUMER_SECRET"),
  "access_token_key": os.getenv("TWITTER_ACCESS_TOKEN_KEY"),
  "access_token_secret": os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
}

spotify = {
  "id": os.getenv("SPOTIFY_ID"),
  "secret": os.getenv("SPOTIFY_SECRET")
}

omdb = {
  "apikey" : os.getenv("OMDB_KEY"),
  "url":os.getenv("OMDB_URL")
}