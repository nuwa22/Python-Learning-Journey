import tkinter as tk

def button_clicked():
    print("Button was clicked!")
root = tk.Tk()
root.title("button clicked")
root.geometry("200x200")

btn = tk.Button(root, text="Click Me!", command=button_clicked) # The command parameter is used to
#specify the function that should be called when the button is clicked.
btn.pack()

root.mainloop()