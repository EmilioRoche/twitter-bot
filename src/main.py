import logging
from apiCall import get_fruit
from config import create_api_object
logger = logging.getLogger()

def tweet_fruit(api):
    api.update_status(get_fruit("banana"))

def main():
    api = create_api_object()
    while True:
        tweet_fruit(api)
        logger.info("Waiting for tweet...")


if __name__ == "__main__":
    main()