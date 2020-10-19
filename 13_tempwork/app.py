# Team Bad (Ari Schechter, Dragos Lup, Benjamin Gallai)
# K13: Template for success - Display a random job occupation at the top of the page and
# display a table of all job occupations
# 2020-10-19

import csv
import random
from flask import Flask, render_template
app = Flask(__name__)

# original occupations file
dictio = {}
with open('data/occupations.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        job_name = row['Job Class']
        if job_name == 'Total':
            break
        percentage = float(row['Percentage'])
        dictio[job_name] = percentage


def random_occupation():
    return random.choices(list(dictio.keys()), list(dictio.values()), k=1)[0]


@app.route("/")
def something():
    return "<h1>Team Bad (Ari Schechter, Dragos Lup, Benjamin Gallai)</h1><br><a href='/occupyflaskst'>thislinktho</a>"


@app.route("/occupyflaskst")
def hello_world():
    return render_template('tablified.html', random_job=random_occupation(), dictt=dictio, dicct_values=dictio.values)


if __name__ == "__main__":
    app.debug = True
    app.run()
