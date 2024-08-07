# sqlite comes by default with python
import sqlite3

# you can connect to a existing database, if one doesn't exist, it'll create one
db = sqlite3.connect('instance/test.db')

# You need a  cursor to be able to interact with the database
cursor = db.cursor()

# Now you can execute sql scripts
try:
    cursor.execute(
        "CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
except sqlite3.OperationalError:
    print("Table already exists")

cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', 4)")

# Changes need to be comitted
db.commit()

result = cursor.fetchall()

print("insert", result)
