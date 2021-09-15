import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="",port=3306)
mycursor=mydb.cursor()
mycursor.execute("create database rail")

