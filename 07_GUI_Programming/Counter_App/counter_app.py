import tkinter as tk

count = 0 # This variable will keep track of the count. It is initialized to 0.
def button_clicked():
    # The button_clicked function is called whenever the button is clicked.
    # It increments the count variable by 1 and updates the text of label1 to display the current count.
    # The global keyword is used to indicate that we are referring to the global variable count,
    # allowing us to modify its value within the function.
    global count
    count = count + 1
    label1.config(text=str(count))
    print(count)

root = tk.Tk()
root.title("Counter App")
root.geometry("300x200")
# This creates a label widget that will display the count. It is initialized with the text
# "0" and a font size of 24.
label1 = tk.Label(root, text="0", font=("Arial", 24)) 
label1.pack()

# This creates a button widget with the text "Add1". When the button is clicked,
# it will call the button_clicked function.Command parameter is used to specify the function that
# should be called when the button is clicked.
button = tk.Button(root, text="Add1", command=button_clicked)
button.pack()

root.mainloop()
