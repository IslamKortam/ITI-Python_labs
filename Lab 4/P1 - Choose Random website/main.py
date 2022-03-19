from random import random
import webbrowser

websites = ['http://www.google.com', 'https://www.linkedin.com', 'http://www.facebook.com', 'https://twitter.com']
randomIndex = round(random() * (len(websites) - 1))  #returns random number in range (0, len(websites list) - 1)

print(f"Opening website with random index = {randomIndex}, its url = {websites[randomIndex]}")
webbrowser.open(websites[randomIndex])