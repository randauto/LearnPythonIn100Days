import mysql.connector
from mysql.connector import errorcode

print("Introduction to Mysql Database in Python")

try:
    # Connect to mysql database.
    cnx = mysql.connector.connect(
        user="root",
        password="",
        host="127.0.0.1",
        database="my_dictionary"
    )
    cursor = cnx.cursor()
    word = input("Enter a word: ")
    query = cursor.execute("SELECT * FROM entries WHERE word = '%s'" % word)
    results = cursor.fetchall()
    # Duyet qua cac ket qua
    if results:
        for item in results:
            print(item[2])
    else:
        print("No word found")
    cnx.close()
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cnx.close()
