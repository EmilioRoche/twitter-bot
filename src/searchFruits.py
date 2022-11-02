def search_fruits(tweet):
    fruits = ['apple','apricot','avocado','banana','blackberry','blueberry','cherry','dragonfruit','durian','feijoa','fig','gooseberry','grape','grapes','greenapple','guava','kiwi','kiwifruit','lemon','lime','lingonberry','lychee','mango','melon','morus','orange','papaya','passionfruit','pear','persimmon','pineapple','pitahaya','plum','pomegranate','raspberry','strawberry','tangerine','tomato','watermelon']
    #if a fruit is found in the tweet
    if any(fruit in tweet for fruit in fruits):
        #return the actual fruit found in the tweet
        return [fruit for fruit in fruits if fruit in tweet]
    else:
        return False