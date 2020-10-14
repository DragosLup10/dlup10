# Clyde 'Thluffy' Sinclair
# SoftDev -- Rona Ed.
# Oct 2020

from flask import Flask, render_template #Q0: What happens if you remove render_template from this line?
#we don't know what render_template does, but it doesn't matter because render_template is used later and it couldn't be used if it wasn't imported.
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "No hablo queso!"

coll = [0,1,1,2,3,5,8]

@app.route("/my_foist_template") #Q1: Can all of your teammates confidently predict the URL to use to load this page?
# yes we can, http://localhost:5000/my_foist_template
def test_tmplt():
    return render_template( 'model_tmplt.html', foo="fooooo", collection=coll) #Q2: What is the significance of each argument?
    #The first argument is the template we are running, in this case "model_tmplt.html", foo and collection are variables in that template which we are replacing with our own values.
    
if __name__ == "__main__":
    app.debug = True
    app.run()
