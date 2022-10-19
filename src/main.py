import os
from apiCall import get_fruit 

from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('API_KEY')
API_KEY_SECRET = os.getenv('API_KEY_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')

get_fruit("banana")
# Authenticate to Twitter , will add it when I am able to create a new twitter account and get the api keys
#auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
#auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

#api = tweepy.API(auth)

#try:
#    api.verify_credentials()
#    print("Authentication OK")
#except:
#    print("Error during authentication")