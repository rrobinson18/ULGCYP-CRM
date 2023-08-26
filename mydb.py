import mysql.connector

dataBase = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root',
    passwd = 'root',
)

# prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE uldatabase")

print("All Done!")