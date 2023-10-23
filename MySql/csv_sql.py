import mysql.connector as connection
import pandas as pd
import csv

# Connecting to mysql database
mydb = connection.connect(
    host='localhost',
    user='root',
    passwd='password',
    database='database',  # Specify the database you want to use
    use_pure=True
)

query = 'INSERT INTO csvdata1 values (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
curr = mydb.cursor()

# Reading CSV file
with open('data.csv', 'r') as data:
    csvfile = csv.reader(data, delimiter=',')
    next(csvfile)
    csv_data = []
    for row in csvfile:
        value = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
        print(row)
        csv_data.append(value)
        

curr.executemany(query, csv_data)
mydb.commit()
