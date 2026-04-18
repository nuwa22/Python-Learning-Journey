import sqlite3
import customtkinter as ctk
import tkinter as tk 
from tkinter import ttk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Student Management System")
root.geometry("1000x600")

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
root.grid_columnconfigure(0, weight=4)
root.grid_columnconfigure(1, weight=6)

root.grid_rowconfigure(0, weight=1)

h = 60
f = ("Arial", 20)

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

left_frame = ctk.CTkFrame(root, width=300)
left_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
left_frame.grid_columnconfigure(0, weight=1)

right_frame = ctk.CTkFrame(root)
right_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
right_frame.grid_columnconfigure(0, weight=1)
right_frame.grid_rowconfigure(0, weight=1)

name_entry = ctk.CTkEntry(left_frame, placeholder_text="Name", height=h, font=f)
name_entry.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

grade_entry = ctk.CTkEntry(left_frame, placeholder_text="Grade", height=h, font=f)
grade_entry.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

status_entry = ctk.CTkEntry(left_frame, placeholder_text="Status", height=h, font=f)
status_entry.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

add_bt = ctk.CTkButton(left_frame, text="Add", height=h, font=f, fg_color="#28a745", hover_color="#218838",)
add_bt.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

update_bt = ctk.CTkButton(left_frame, text="Update", height=h, font=f, fg_color="#FF9500", hover_color="#CC7700")
update_bt.grid(row=4, column=0, padx=10, pady=10, sticky="ew")

delete_bt = ctk.CTkButton(left_frame, text="Delete", height=h, font=f, fg_color="#dc3545", hover_color="#c82333")
delete_bt.grid(row=5, column=0, padx=10, pady=10, sticky="ew")

clear_bt = ctk.CTkButton(left_frame, text="Clear", height=h, font=f, fg_color="#6c757d", hover_color="#5a6268")
clear_bt.grid(row=6, column=0, padx=10, pady=10, sticky="ew")

table = ttk.Treeview(right_frame, columns=("Student_id", "Name", "Grade", "Status"), show="headings", height=15)
table.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
table.heading("Student_id", text="Student ID")
table.heading("Name", text="Name")
table.heading("Grade", text="Grade")
table.heading("Status", text="Status")

table.column("Student_id", width=80, anchor="center")
table.column("Name", width=200, anchor="center")
table.column("Grade", width=100, anchor="center")
table.column("Status", width=100, anchor="center")


root.mainloop()



