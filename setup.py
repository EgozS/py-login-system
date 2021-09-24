import mysql.connector
import databaseInfo as info
import sys
import os

mydb = mysql.connector.connect(
    host=info.host,
    user=info.user,
    password=info.password,
)

mycursor = mydb.cursor(buffered=True)

def cls():
    if sys.platform == "linux":
        os.system("clear")
    else:
        os.system("cls")

def setup():
    try:
        mycursor.execute("CREATE DATABASE IF NOT EXISTS logintest")
        mycursor.execute("USE logintest")
        mycursor.execute("CREATE TABLE `users` (`id` int(11) NOT NULL AUTO_INCREMENT, `username` text COLLATE utf8mb4_unicode_ci DEFAULT NULL, `email` text COLLATE utf8mb4_unicode_ci DEFAULT NULL, `password` binary(32) DEFAULT NULL, `salt` binary(32) DEFAULT NULL, PRIMARY KEY (`id`));")
        print("table built succssfully!")
        input("click enter to go back to main screen...")
        cls()
        options()
    except Exception as e: 
        print(e)
        input("click enter to continue...")
        cls()
        options()

def drop():
    try:
        confrim = input("are you sure you want to delete the database? this action cannot be undoed. y/n ")
        if confrim == "y":
            mycursor.execute("USE logintest")
            mycursor.execute("DROP DATABASE logintest")
            print("database dropped!")
            input("click enter to go back to main screen...")
            cls()
            options()
        elif confrim == "n":
            print("task failed succssfully!")
            input("click enter to go back to main screen...")
            cls()
            options()
        else:
            cls()
            print("please only pick y or n!")
            input("click enter to go back")
            drop()
    except Exception as e:
        print(e)
        input("click enter to continue...")
        cls()
        options()

def options():
    try:
        print("1. Setup")
        print("2. Delete database and all info | run at your own risk!")
        options = input("please pick 1 or 2: ")
        if options == "1":
            cls()
            setup()
        elif options == "2":
            cls()
            drop()
        else:
            cls()
            print("please only pick 1 or 2")
            input("click enter to continue...")
            cls()
            options()
    except: 
        cls()
        print("please only pick 1 or 2")
        input("click enter to continue...")
        options()
options()