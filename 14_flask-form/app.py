#Team RIID - Ishita Gupta, Dragos Lup, Renee Mui, Ian Chen-Adamczyk
#SoftDev
#K14 -- Form and Function/Echo user output received from html form 
#2020-12-8

from flask import Flask, render_template, request

app = Flask(__name__) 

@app.route("/", methods=['GET', 'POST'])
def disp_loginpage():
    return render_template( 'login.html' )


@app.route("/auth", methods=['GET', 'POST'])
def authenticate():
    username = request.form['username']
    return render_template('response.html', name = username, method = request.method)
    
if __name__ == "__main__": 
    app.debug = True 
    app.run()