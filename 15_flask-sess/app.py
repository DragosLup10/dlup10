#Team RIID - Ishita Gupta, Dragos Lup, Renee Mui, Ian Chen-Adamczyk
#SoftDev
#K15 -- Sessions Greetings/Authenticate user login using a webform and flask and create a session
#2020-12-11

from flask import Flask, render_template, request, session, redirect
import os

app = Flask(__name__)  
# generate random secret key
app.secret_key = os.urandom(10)


@app.route("/")
def welcome():
    # check if user has logged in correctly before in the same session
    if 'username' in session:
        username = session['username']
        # if user is logged in, return the welcome page
        return render_template('welcome.html', name = username)
    # if user has not logged in before in the same session, return the login page
    return render_template('login.html')

@app.route("/login", methods=['GET', 'POST']) 
def login():
    # if user has entered something in both fields, set inputs 
    if ('username' in request.form) and ('password' in request.form):
        username = request.form['username']
        password = request.form['password']
    # if either field is blank, redirect to login page
    else:
        return redirect('/')

    # check if username and password are correct
    validUsername = ("password" == username)
    validPassword = ("username" == password)

    # if both boolean values are true, return the welcome page
    if validUsername and validPassword:
        session['username'] = username
        return render_template('welcome.html', name = username)
        
    # if either boolean value is false, return the error page (jinja in html checks which value is incorrect)
    return render_template('error.html', user = validUsername, password = validPassword)

# when user logs out, remove username from session and return login page
@app.route("/logout")
def logout():
    if 'username' in session:
        session.pop('username')
        return render_template('login.html', msg="Successfully logged out!")
    # if user tries to access logout page without logging in first
    return redirect('/')


if __name__ == "__main__": 
    app.debug = True 
    app.run() 

