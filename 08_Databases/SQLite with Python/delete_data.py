import sqlite3

connection = sqlite3.connect("school.db")
cursor = connection.cursor()

cursor.execute("""
                DELETE FROM students
                WHERE student_id = 2
                """)

connection.commit()
connection.close()

print("Deleted data from the students table successfully.")