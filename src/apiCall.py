import requests

def get_fruit(fruit):
    api = "https://www.fruityvice.com/api/fruit/" + fruit
    response = requests.get(api)
    print(response.json())