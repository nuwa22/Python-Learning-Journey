import tkinter as tk

root = tk.Tk()
root.title("Grid Layout")
root.geometry("300x200")

label1 = tk.Label(root, text="Label 1")
label1.grid(row=0, column=0)

label2 = tk.Label(root, text="Label 2")
label2.grid(row=0, column=1)

label3 = tk.Label(root, text="Label 3")
label3.grid(row=1, column=0)

button = tk.Button(root, text="Button")
button.grid(row=1, column=1)

root.mainloop()