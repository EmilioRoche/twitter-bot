import logging
import tweepy
from apiCall import get_fruit
from config import create_api_object
logger = logging.getLogger()

def tweet_fruit(api):
    result = "apple has " + str(get_fruit("apple")) + " calories."
    # api.update_status(result)
def mentions(api, keywords, since_id):
    logger.info("Retrieving mentions")
    new_since_id = since_id
    for tweet in tweepy.Cursor(api.mentions_timeline, since_id=since_id).items():
        new_since_id = max(tweet.id, new_since_id)
        if tweet.in_reply_to_status_id is not None:
            continue
        if any(keyword in tweet.text.lower() for keyword in keywords):
            logger.info(f"Answering {tweet.user.name}")
            
            # reply back with the response we need from tweet_fruit api


def main():
    api = create_api_object()
    tweet_fruit(api)
    logger.info("Waiting for tweet...")


if __name__ == "__main__":
    main()