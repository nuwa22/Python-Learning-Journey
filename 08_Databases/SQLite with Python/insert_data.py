import sqlite3

connection = sqlite3.connect("school.db")
cursor = connection.cursor()

cursor.execute("""
               INSERT INTO students (name, grade, status)
               VALUES ('Suresh', 'Grade 12', 'Active'),
                      ('Ramesh', 'Grade 11', 'Active'),
                      ('Geeta', 'Grade 10', 'Inactive')
               """)

connection.commit()
connection.close()

print("Inserted data into the students table successfully.")