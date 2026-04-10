import  sqlite3
# Connect to the database (or create it if it doesn't exist)
connection = sqlite3.connect("school.db")
cursor = connection.cursor()

# Create a table for students
cursor.execute("""
               CREATE TABLE IF NOT EXISTS students (
                   student_id INTEGER PRIMARY KEY,
                   name TEXT NOT NULL,
                   grade TEXT,
                   status TEXT
                )
                   
               """)

# save the changes and close the connection
connection.commit()
connection.close()

print("Created the students table successfully.")