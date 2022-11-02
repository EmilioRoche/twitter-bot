def search_fruits(tweet):
    fruits = ['apple','apricot','avocado','banana','blackberry','blueberry','cherry','dragonfruit','durian','feijoa','fig','gooseberry','grape','grapes','greenapple','guava','kiwi','kiwifruit','lemon','lime','lingonberry','lychee','mango','melon','morus','orange','papaya','passionfruit','pear','persimmon','pineapple','pitahaya','plum','pomegranate','raspberry','strawberry','tangerine','tomato','watermelon']
    if any(fruit in tweet for fruit in fruits):
        return tweet
    else:
        return None