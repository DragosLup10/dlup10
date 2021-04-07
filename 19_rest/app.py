#Team Decidophobia -- Madelyn Mao, Dragos Lup 
#SoftDev
#K19 -- API key
#2021-04-06

from flask import Flask            #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
import urllib.request
import json

key = open("key_nasa.txt", "r").read()
app = Flask(__name__)

@app.route('/')
def index():
    url = urllib.request.urlopen('https://api.nasa.gov/planetary/apod?api_key=' + key) # combine nasa url with key
    now_json = json.load(url) # url -> json

    image = now_json['url'] # image url
    description = now_json['explanation'] # image description

    return render_template('main.html', image = image, description = description)

if __name__ == "__main__": #false if this file imported as module
    app.debug = True 
    app.run()