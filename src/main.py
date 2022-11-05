import logging
import tweepy
import time
from apiCall import get_fruit
from searchFruits import search_fruits
from config import create_api_object
logger = logging.getLogger()
# this will be what provides info for our tweet mentions
def tweet_fruit(foundFruit):
    fruit = foundFruit[0]
    result = "@{} The fruit, " + fruit + ", has " + str(get_fruit(fruit)) + " calories."
    return result
    # api.update_status(result)
def mentions(api, keywords, mention_id):
    logger.info("Retrieving mentions....")
    new_mention_id = mention_id
    # gets the tweets and looks for latest mention
    for tweet in tweepy.Cursor(api.mentions_timeline, since_id = mention_id).items():
        logger.info("A mention has been found!")
        # assigns our mention id as either the tweet id or the mention id
        new_mention_id = max(tweet.id, new_mention_id)
        # make sure that the tweet is not a reply to another tweet
        if tweet.in_reply_to_status_id is not None:
            continue
        # we see if the tweet contains any of the keywords we have specified
        if any(keyword in tweet.text.lower() for keyword in keywords):
            foundFruit = search_fruits(tweet.text.lower())
            logger.info(foundFruit)
            if foundFruit is False:
                no_fruit_message = "@{} Sorry, no data on the fruit specified was found."
                logger.info("No data on that fruit")
                try:
                    api.update_status(no_fruit_message.format(tweet.author.screen_name), in_reply_to_status_id = tweet.id)
                except Exception as exc:
                    logger.info(exc)
            else:
                logger.info("Replying to user with fruit data")
                fruit_message = tweet_fruit(foundFruit)
                try:
                    api.update_status(fruit_message.format(tweet.author.screen_name), in_reply_to_status_id = tweet.id)
                except Exception as exc:
                    logger.info(exc)
            logger.info("Replied successfully")
    return new_mention_id


def main():
    # call from config
    api = create_api_object()
    keywords = ['calories']
    #tweet_fruit(api)
    # set an id so we don't keep replying to tweets we've already replied to
    mention_id = 1
    while True:
        logger.info("Waiting for any tweets...")
        mention_id = mentions(api, keywords, mention_id)
        #add delay for searching
        time.sleep(75)


if __name__ == "__main__":
    main()