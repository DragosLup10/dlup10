# Team Gummy Bear : Dragos Lup, Kelly Huang
# SoftDev
# K10 -- Putting Little Pieces Together
# 2020-10-12


from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    return "No hablo queso!"

app.run()

#This file should be similar to the last one, the only difference being that this one doesn't print something in the terminal
#We were correct
