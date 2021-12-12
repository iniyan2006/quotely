from fastapi import FastAPI
import quote_parse
import requests
app = FastAPI()

@app.get('/')

def quote():
    return quote_parse.get_quote()

@app.get('/random')

def random_quote():
    quotes = requests.get('https://quoteli.herokuapp.com/').json()
    quote = quotes['quoteText'] + "\n - by " + quotes["quoteAuthor"]
    return quote