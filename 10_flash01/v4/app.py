# Team Gummy Bear : Dragos Lup, Kelly Huang
# SoftDev
# K10 -- Putting Little Pieces Together
# 2020-10-12

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route

def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    return "No hablo queso!"

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()

#We figured out what debug mode does, we found that when a file gets edited while its being run, and then its saved, debug mode automagically reloads it, instead of having to restart the process.

#This file seemed very similar to the last one, we assumed there was gonna be no difference when ran, because __name__ IS equal to __main__
#We were right, it was mostly the same, but if the file is imported it doesn't turn on debug mode.
