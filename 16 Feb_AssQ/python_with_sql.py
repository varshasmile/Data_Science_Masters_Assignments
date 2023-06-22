# Q6. Write a python code to connect MySQL to python. Explain the cursor() and execute() method.

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE if not exists test")
mydb.close()

'''
cursor(): The cursor() method is used to create a cursor object. The cursor allows you to execute SQL queries and fetch the results. It acts as a control structure that enables interaction with the database.

execute(): The execute() method is used to execute an SQL query or command. It takes the SQL query as a parameter and sends it to the MySQL server for execution. The query can be a SELECT, INSERT, UPDATE, DELETE, or any other valid SQL statement.
'''