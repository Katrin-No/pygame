import psycopg2
import csv
import pandas as pd
import argparse


def connection():
    global con
    con = psycopg2.connect(database="aland", user="azubi",
                           password="a1t1AZUBI", host="localhost", port="5432")
    print("Database opened successfully", end='\n\n')


connection()

# Durchlaufen der Ergebnisse


def here_the_results():
    global row, cursor
    print("Here the results:")
    cursor = con.cursor()
    cursor.execute(query)
    row = cursor.fetchone()
    while (row != None):
        print(row)
        row = cursor.fetchone()


# export to csv without header


def save_ohne_header():
    answer = input("Do you want to save the results in csv document? y/n: ")
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


# export to csv with header


def save_with_header():
    annoing = input("Maybe with header? y/n: ")
    if annoing == "y":
        sql_query = pd.read_sql_query(query, con)
        df = pd.DataFrame(sql_query)
        # place 'r' before the path name to avoid any errors in the path
        df.to_csv(r'with-header-' + parameter + '.csv', index=False)
        print("A csv document with header successfully created")
    else:
        print("Ok, ok. Buy!")


def ask_parameter():
    global parameter, query
    parameters = ["A", "B", "C", "D", "all", "Europa",
                  "Asien", "Afrika", "Nordamerika", "Südamerika", "Australien"]
    parameter = input(
        "Type:\n - name of continent or \n - first letter of land (A-D) or \n - 'all' for the hole table\n: ")
    print()
    if parameter in parameters:
        if len(parameter) < 3:
            query = "SELECT * FROM land WHERE name LIKE \'" + parameter + "%\'"
        elif len(parameter) == 3:
            query = "SELECT * FROM land"
        else:
            query = "SELECT * FROM land WHERE kontinent = \'" + parameter + "\'"
        print("Query is: " + query)
        here_the_results()
        save_ohne_header()
        save_with_header()

    else:
        print("Sorry, this parameter is wrong")


ask_parameter()
