import requests
import json

def get_random_quote():
    #We are using the API from https://www.github.com/lukePeavey/quotable
    r = requests.get("https://api.quotable.io/random")
    if (r.status_code == requests.codes.ok):
        return json.loads(r.text)

def sentiment_analysis(quote):
    #TODO: Run Sentiment Analysis on quote
    #We need to find emotion of the quote and the message
    
    pass

def get_picture(results):
    #TODO: Find a relevent picture based on results of Sentiment Analysis
    pass

def find_text_color(picture):
    #TODO: Find the constasting color to the picture to use as text color
    pass

def combine(quote, picture):
    #TODO: Put the text on the picture
    pass

def export_into_file(new_picture):
    #TODO: Export into a file called quote.png
    pass
