# Team Gummy Bear : Dragos Lup, Kelly Huang
# SoftDev
# K10 -- Putting Little Pieces Together
# 2020-10-13
import csv
import random
from flask import Flask
app = Flask(__name__) #create instance of class Flask

#original occupations file
dictio = {}
with open('occupations.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        job_name = row['Job Class']
        if job_name == 'Total':
            break
        percentage = float(row['Percentage'])
        dictio[job_name] = percentage

def random_occupation():
    return random.choices(list(dictio.keys()), list(dictio.values()), k=1)[0]

#This just runs through the dictionary and puts all the keys into a string so we can print it
def occupation_runthrough():
    stringo = ""
    for x in dictio:
        stringo += x + "<br>"
    return stringo
print(random_occupation())

@app.route("/")
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    #Really long return, we didn't really know another way we could do this.
    return """
    Team Gummy Bear - Dragos Lup, Kelly Huang<br><br>Your occupation is: <b>""" + random_occupation() + """</b>
    <br><br>Chosen from this list <br>""" + occupation_runthrough()

#kept this cause we thought it was cool
if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
