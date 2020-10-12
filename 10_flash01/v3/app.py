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

app.debug = True
app.run()

#This should turn on a sort of debug mode, which probably makes it easier to debug, maybe by printing out stuff from the terminal on the website.
#We didn't notice any differences, other than there being these messages in the terminal
# * Debug mode: on
# * Restarting with stat
# * Debugger is active!
# * Debugger PIN: 374-915-956
