import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="gamco_hospital_management")


def DB_Open_Connection():
    try:
        if not db.is_connected():
            db.connect()
    except Exception as err:
        print("You got some error", err)


def DB_Close_Connection():
    try:
        if db.is_connected():
            db.close()
    except Exception as err:
        print("You got some error", err)