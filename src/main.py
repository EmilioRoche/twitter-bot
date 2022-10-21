import logging
from apiCall import get_fruit
from config import create_api_object
logger = logging.getLogger()

def tweet_fruit(api):
    result = "banana has " + str(get_fruit("banana")) + " calories."
    api.update_status(result)

def main():
    api = create_api_object()
    tweet_fruit(api)
    logger.info("Waiting for tweet...")


if __name__ == "__main__":
    main()