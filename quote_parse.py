import random
import json

quotes = []

def get_quote():
    with open('quotes.json') as file:
        parser = json.load(file)
        quotes = parser
        return random.choice(quotes)
        print(parser)

if __name__ == "__main__":
    get_quote()