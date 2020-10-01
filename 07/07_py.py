 # Ari Schechter, Dragos Lup and Jessica Yeung (Team Ohala)
# Soft Dev
# K07 -- StI/O: Divine your Destiny!
# 2020-10-02

# Organize the occupations.csv file into a dictionary and
# then create a function that returns the jobs weighted
# by the percentages given.

# Import the neccesary modules
import csv
import random

dic = {}  # Initializes the dictionary for jobs and percentages

with open('occupations.csv', 'r') as csv_file:  # opens the file
    # Uses the DictReader class to read the csv file into a dictionary like data structure
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:  # Loops through each line in the csv file
        # DictReader assigns each column a title based on the first row of the csv file.
        job_name = row['Job Class']
        # 'Job Class' for the title of each job and 'Percentage' for the percentage.
        if job_name == 'Total':  # Don't want to take the last line
            break
        # 'Percentage' is the second column
        percentage = float(row['Percentage'])
        # adding the names and percentages to our dictionary
        dic[job_name] = percentage


def random_occupation():
    # gets a random value from 0 to 100, includes decimals.
    num = random.uniform(0, 100)
    chance = 0  # initial min chance
    for occupation in dic:
        chance += dic[occupation]  # Percentage of occupation
        # We add the chance for every occupation to get to the chance we want for the occupations
        # This way each occupation has its own area and all have the correct chance for being chosen.
        # If the num we got lies in the current chance, we got our value.
        if(num <= chance):
            print(occupation)
            break


random_occupation()
