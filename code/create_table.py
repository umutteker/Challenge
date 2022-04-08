import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

# MUST BE INTEGER
# This is the only place where int vs INTEGER matters—in auto-incrementing columns
create_table = "CREATE TABLE IF NOT EXISTS plates (id INTEGER PRIMARY KEY, plate text ,owner text ,start_date timestamp,end_date timestamp price real)"
cursor.execute(create_table)

connection.commit()

connection.close()
