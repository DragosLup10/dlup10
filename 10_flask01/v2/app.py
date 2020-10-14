# Team Gummy Bear : Dragos Lup, Kelly Huang
# SoftDev
# K10 -- Putting Little Pieces Together
# 2020-10-12


from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)   #where will this go?
    return "No hablo queso!"

app.run()

#This will also be similar to the v0, except before it prints __name__ it'll print "about to print __name__ "
#We were correct
