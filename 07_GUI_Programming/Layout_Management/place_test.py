import tkinter as tk

root = tk.Tk()
root.geometry("300x300")

my_button = tk.Button(root, text="Click Me!")
my_button.place(x=50, y=100) # The place() method allows you to specify the exact coordinates
# (x and y) where the button should be placed within the window.

root.mainloop()