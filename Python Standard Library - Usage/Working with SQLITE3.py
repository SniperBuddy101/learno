# In this program, we'll be working with SQLITE3

import sqlite3

# Creating a connection object - this will create a new database file if not already present.
with sqlite3.connect("database.sqlite3") as conn:
    db_cursor = conn.cursor()
    db_cursor.execute("""CREATE TABLE Superheroes(ID text, Name text, Contact_number integer)""")

    db_cursor.execute("""INSERT INTO Superheroes VALUES 
    (:ID, :Name, :Contact_number)""", {"ID": 1, "Name": "Iron Man", "Contact_number": 123456})

    iterable_rows = db_cursor.execute("SELECT * FROM Superheroes")
    for a in iterable_rows:
        print(a)
    conn.commit()
