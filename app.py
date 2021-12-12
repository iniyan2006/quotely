from fastapi import FastAPI
import quote_parse
import requests
app = FastAPI()

@app.get('/')

def quote():
    return quote_parse.get_quote()

@app.get('/random')

def random_quote():
    quotes = requests.get('http://127.0.0.1:8000').json()
    quote = quotes['quoteText'] + "\n - by " + quotes["quoteAuthor"]
    return quote