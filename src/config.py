import os
import logging
import tweepy
from dotenv import load_dotenv
load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def create_api_object():
    API_KEY = os.getenv('TWITTER_API_KEY')
    API_KEY_SECRET = os.getenv('TWITTER_API_KEY_SECRET')
    ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN')
    ACCESS_TOKEN_SECRET = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')

    # Authenticate to Twitter , will add it when I am able to create a new twitter account and get the api keys
    auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth, wait_on_rate_limit=True)
    try:
        api.verify_credentials()
        print("Authentication Good, Created API")
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API has been created")
    return api
