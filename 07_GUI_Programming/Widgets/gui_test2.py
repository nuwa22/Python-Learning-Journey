import tkinter as tk

root = tk.Tk()
root.title("My First GUI")
root.geometry("500x500")

my_label = tk.Label(root, text="Hi there!. Welcome to my first GUI application.") # Create a label widget
#with the specified text and associate it with the root window.
my_label.pack() # The pack() method is used to add the label to the window and manage its layout.

my_button = tk.Button(root, text="Click Me!")
my_button.pack()

my_entry = tk.Entry(root)
my_entry.pack()

root.mainloop()