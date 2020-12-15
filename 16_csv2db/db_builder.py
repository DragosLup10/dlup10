#Team RIID - Ishita Gupta, Dragos Lup, Renee Mui, Ian Chen-Adamczyk
#SoftDev
#K16 -- No Trouble/Write script to turn CSV files into a relational database using sqlite3
#2020-12-15

import sqlite3  
# allows use of DictReader() method, which simplifies the conversion of a csv file into a dictionary
import csv       

DB_FILE="data.db"
# create a database if it doesn't already exist
db = sqlite3.connect(DB_FILE)
# refer to cursor name to run commands
c = db.cursor()     

#############################################
# create a table in the database
command = "CREATE TABLE students (name TEXT, age INTEGER, id INTEGER);"         
c.execute(command)

# convert csv file into dictionary
input_file = csv.DictReader(open("students.csv"))
# for each entry, save the values as variables
for row in input_file:
    name, age, ids = (row.values())
    # add each entry into the table
    command = f"INSERT INTO students VALUES ('{name}', {age}, {ids});"
    c.execute(command)

# testing the database to make sure all entries are correct
command = "SELECT * FROM students;"
# diagnostic print statement
print("Student table: \n")
for row in c.execute(command):
    print(row)

#############################################

# create another table in the database
command = "CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER);"         
c.execute(command)

input_file = csv.DictReader(open("courses.csv"))
for row in input_file:
    code, mark, ids = (row.values())
    command = f"INSERT INTO courses VALUES ('{code}', {mark}, {ids});"
    c.execute(command)

# tested the courses table as well
command = "SELECT * FROM courses;"
# diagnostic print statement
print("Course table: \n")
for row in c.execute(command):
    print(row)

#==========================================================

# save changes made to database
db.commit() 
# close the database
db.close()  
