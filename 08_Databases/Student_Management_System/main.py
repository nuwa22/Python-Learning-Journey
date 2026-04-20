import sqlite3
import customtkinter as ctk
import tkinter as tk 
from tkinter import ttk

# Set the appearance and color theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Create the main window
root = ctk.CTk()
root.title("Student Management System")
root.geometry("1000x600")

# Create the database
def setup_database():
    connection = sqlite3.connect("school_db.db")
    cursor = connection.cursor()

    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS students(
                   student_id  INTEGER PRIMARY KEY,
                   name TEXT NOT NULL,
                   grade TEXT,
                   status TEXT
                   )
                   """)
    
    connection.commit()
    connection.close()

    print("Created the students table successfully.")

setup_database()

# Function to clear the entry fields
def clear_entries():
    name_entry.delete(0, tk.END)
    grade_entry.delete(0, tk.END)
    status_entry.delete(0, tk.END)

# Function to add a student to the database
def add_student():
    name = name_entry.get()
    grade = grade_entry.get()
    status = status_entry.get()

    if name and grade and status:
        connection = sqlite3.connect("school_db.db")
        cursor = connection.cursor()
        cursor.execute("""
                       INSERT INTO students (name, grade, status)
                       VALUES (?, ?, ?)
                       """,
                       (name, grade, status)
                       )
        connection.commit()
        connection.close()

        clear_entries()
        display_students()
        print("Added student successfully.")
        tk.messagebox.showinfo("Success", "Student added successfully.")
    else:
        print("Please fill in all fields to add a student.")
        tk.messagebox.showwarning("Input Error", "Please fill in all fields to add a student.")

# Function to display all students
def display_students():
    connection = sqlite3.connect("school_db.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    for record in table.get_children():
        table.delete(record)
    for row in rows:
        table.insert("", tk.END, values=row)
    connection.close()

# Function to delete a student
def delete_student():
    selected_item = table.selection()
    if selected_item:
        values = table.item(selected_item, "values")
        student_id = values[0]

        connection = sqlite3.connect("school_db.db")
        cursor = connection.cursor()

        cursor.execute("""
                       DELETE FROM students
                       WHERE student_id = ?
                       """,
                       (student_id,)
                       )
        connection.commit()
        connection.close()

        display_students()
        clear_entries()
        print("Deleted student successfully.")
        tk.messagebox.showinfo("Success", "Student deleted successfully.")
    else:
        print("Please select a student to delete.")
        tk.messagebox.showwarning("Selection Error", "Please select a student to delete.")

# Function to fill the entry fields with the selected student's data
def fill_entries(event):
    selected_item = table.selection()
    if selected_item:
        values = table.item(selected_item, "values")
        clear_entries()

        name_entry.insert(0, values[1])
        grade_entry.insert(0, values[2])
        status_entry.insert(0, values[3])

# Function to update a student's information
def update_student():
    selected_item = table.selection()
    if selected_item:
        values = table.item(selected_item, "values")
        student_id = values[0]

        new_name = name_entry.get()
        new_grade = grade_entry.get()
        new_status = status_entry.get()

        if new_name and new_grade and new_status:
            connection = sqlite3.connect("school_db.db")
            cursor = connection.cursor()

            cursor.execute("""
                           UPDATE students
                           SET name = ?, grade = ?, status = ?
                           WHERE student_id = ?
                           """,
                           (new_name, new_grade, new_status, student_id)
                           )
            connection.commit()
            connection.close()

            display_students()
            clear_entries()
            print("Updated student successfully.")
            tk.messagebox.showinfo("Success", "Student updated successfully.")
        else:
            print("Please fill in all fields to update a student.")
            tk.messagebox.showwarning("Input Error", "Please fill in all fields to update a student.")

# root window layout
root.grid_columnconfigure(0, weight=4)
root.grid_columnconfigure(1, weight=6)
root.grid_rowconfigure(0, weight=1)

h = 60
f = ("Arial", 20)

# style the treeview
style = ttk.Style()
style.theme_use("default")
style.configure("Treeview",
                background="#2b2b2b",
                foreground="white",
                rowheight=35,
                fieldbackground="#2b2b2b",
                font=("Arial", 14)
                )

style.configure("Treeview.Heading",
                background="#1f1f1f",
                foreground="white",
                hoverbackground="#1f1f1f",
                font=("Arial", 14)
                )

style.map("Treeview",
          background=[("selected", "#347083")]
          )
# Create the left and right frames
left_frame = ctk.CTkFrame(root, width=300)
left_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
left_frame.grid_columnconfigure(0, weight=1)

right_frame = ctk.CTkFrame(root)
right_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
right_frame.grid_columnconfigure(0, weight=1)
right_frame.grid_rowconfigure(0, weight=1)

# Create the left frame widgets
# name_entry
name_entry = ctk.CTkEntry(left_frame, placeholder_text="Name", height=h, font=f)
name_entry.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

# grade_entry
grade_entry = ctk.CTkEntry(left_frame, placeholder_text="Grade", height=h, font=f)
grade_entry.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

# status_entry
status_entry = ctk.CTkEntry(left_frame, placeholder_text="Status", height=h, font=f)
status_entry.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

# add_button
add_bt = ctk.CTkButton(left_frame, text="Add", height=h, font=f, fg_color="#28a745", hover_color="#218838", command=add_student)
add_bt.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

# update_button
update_bt = ctk.CTkButton(left_frame, text="Update", height=h, font=f, fg_color="#FF9500", hover_color="#CC7700", command=update_student)
update_bt.grid(row=4, column=0, padx=10, pady=10, sticky="ew")

# delete_button
delete_bt = ctk.CTkButton(left_frame, text="Delete", height=h, font=f, fg_color="#dc3545", hover_color="#c82333", command=delete_student)
delete_bt.grid(row=5, column=0, padx=10, pady=10, sticky="ew")

# clear_button
clear_bt = ctk.CTkButton(left_frame, text="Clear", height=h, font=f, fg_color="#6c757d", hover_color="#5a6268",command=clear_entries)
clear_bt.grid(row=6, column=0, padx=10, pady=10, sticky="ew")

# Create the right frame widgets
# table
table = ttk.Treeview(right_frame, columns=("Student_id", "Name", "Grade", "Status"), show="headings", height=15,)
table.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
table.heading("Student_id", text="Student ID")
table.heading("Name", text="Name")
table.heading("Grade", text="Grade")
table.heading("Status", text="Status")

table.column("Student_id", width=80, anchor="center")
table.column("Name", width=200, anchor="center")
table.column("Grade", width=100, anchor="center")
table.column("Status", width=100, anchor="center")

display_students()
table.bind("<ButtonRelease-1>", fill_entries)
root.mainloop()



