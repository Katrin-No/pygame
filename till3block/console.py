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


def parameters():
    global args, query
    # Initialize the parser
    parser = argparse.ArgumentParser()
    # Add the parameters
    parser.add_argument(
        "parameter", help="Type 1)name of continent, 2)first letter of land or 3)all - for the hole table, ", type=str)
    # Parse the arguments
    args = parser.parse_args()

    if len(args.parameter) < 3:
        query = "SELECT * FROM land WHERE name LIKE \'" + args.parameter + "%\'"
    elif len(args.parameter) == 3:
        query = "SELECT * FROM land"
    else:
        query = "SELECT * FROM land WHERE kontinent = \'" + args.parameter + "\'"
    print("Query is: " + query)


parameters()

# Durchlaufen der Ergebnisse


def your_results():
    global cursor, row
    print("Here the results:")
    cursor = con.cursor()
    cursor.execute(query)
    row = cursor.fetchone()
    while (row != None):
        print(row)
        row = cursor.fetchone()


your_results()

# export to csv without header


def save_without_header():
    cursor.execute(query)
    results = cursor.fetchall()
    with open("" + args.parameter + ".csv", "w") as file:
        for row in results:
            csv.writer(file).writerow(row)
    print()
    print("A csv document successfully created")


save_without_header()
