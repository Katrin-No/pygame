import psycopg2, csv
import pandas as pd
import argparse

con = psycopg2.connect(database="aland", user="azubi", password="a1t1AZUBI", host="localhost", port="5432")
print("Database opened successfully", end='\n\n')

cursor = con.cursor()

# Initialize the parser
parser = argparse.ArgumentParser()
# Add the parameters
parser.add_argument("parameter", help="Type 1)name of continent, 2)first letter of land or 3)all - for the hole table, ", type=str)
# Parse the arguments
args = parser.parse_args()

if len(args.parameter) <3:
    query = "SELECT * FROM land WHERE name LIKE \'" + args.parameter + "%\'"
elif len(args.parameter) == 3:
    query = "SELECT * FROM land"
else:
    query = "SELECT * FROM land WHERE kontinent = \'" + args.parameter + "\'"
print("Query is: " + query)
print("Here the results:")

# Durchlaufen der Ergebnisse
cursor.execute(query)
row = cursor.fetchone()
while (row!=None):
    print(row)
    row = cursor.fetchone()

#export to csv without header
cursor.execute(query)
results = cursor.fetchall()
with open("" + args.parameter + ".csv", "w") as file:
    for row in results:
        csv.writer(file).writerow(row)
print()
print("A csv document successfully created")

# interactive
def interactive(parameter):
    parameter = ""
    parameter = input("Type:\n - name of continent or \n - first letter of land (A-D) or \n - 'all' for the hole table\n: ")
    print()
    if len(parameter) <3:
        query = "SELECT * FROM land WHERE name LIKE \'" + parameter + "%\'"
    elif len(parameter) == 3:
        query = "SELECT * FROM land"
    else:
        query = "SELECT * FROM land WHERE kontinent = \'" + parameter + "\'"
    print("Query is: " + query)
    print("Here the results:")

    # Durchlaufen der Ergebnisse
    cursor.execute(query)
    row = cursor.fetchone()
    while (row!=None):
        print(row)
        row = cursor.fetchone()

    #export to csv without header
    def save_csv(answer):
        answer= input("Do you want to save the results in csv document? y/n: ")
        if answer == "y":
            cursor.execute(query)
            results = cursor.fetchall()
            with open("" + parameter + ".csv", "w") as file:
                for row in results:
                    csv.writer(file).writerow(row)
            print()
            print("A csv document successfully created")
        else:
            print("Ok, they are not saved. Bye!")
    save_csv("y")

interactive("B")