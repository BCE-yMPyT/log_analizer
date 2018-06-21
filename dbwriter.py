'''
module dbwriter.py was created to record information about requests to the database:
date of analysis, number of requests, requests per second\minute\hour
'''
#-----import working stuff--------------------------

from getter import Getter
import sqlite3
import os

def DBwriter():
    result = Getter()
    #print(result)
    #result=[('start_day', req_count, req_per_sec, req_per_min, req_per_hour)]

    #-------------------------------------------------------------------------------------------
                                                 # if DB not exist, create and connect
    if not os.path.exists("mydatabase.db"):
        conn = sqlite3.connect("mydatabase.db")  # creating DB
        cursor = conn.cursor()                   # creating cursor
        cursor.execute('''CREATE TABLE results
                                  (analize_date text, requests_count real, request_per_second real,
                                   request_per_minute real, request_per_hour real)
                               ''')
                                                 # If DB exist - connecting
    else:
        conn = sqlite3.connect("mydatabase.db")
        cursor = conn.cursor()                   # making cursor
    #-------------------------------------------------------------------------------------------
                                             # Insert data to DB table safely
    cursor.execute('INSERT INTO results VALUES (?, ?, ?, ?, ?)', (result[0][0], result[0][1], result[0][2], result[0][3], result[0][4]))

    #-------------------------------------------------------------------------------------------
                                             # Save changes
    conn.commit()
    #------------------------------------------------------------------------------------------
                                             # Checking (output) results
    sql = "SELECT * FROM results"
    cursor.execute(sql)
    print(cursor.fetchall())

if __name__ == '__main__':
    one_more = DBwriter()