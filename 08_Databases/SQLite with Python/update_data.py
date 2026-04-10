import sqlite3

connection = sqlite3.connect("school.db")
cursor = connection.cursor()

cursor.execute("""
                UPDATE students
                SET grade = '13'
                WHERE name = 'Ramesh'
                """) 

connection.commit()
connection.close()

print("Updated data in the students table successfully.")