import sqlite3

conn = sqlite3.connect('database.db')
print ("Opened database successfully")

conn.execute('CREATE TABLE news (id INTEGER PRIMARY KEY, a TEXT, b TEXT, c TEXT, d TEXT, e TEXT)')
print ("Table created successfully")
conn.close()