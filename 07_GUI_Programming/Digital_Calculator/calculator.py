import tkinter as tk

root = tk.Tk()
root.title("Digital Calculator")

# Functions for button clicks
def button_click(number):
    current = display.get()
    display.insert(tk.END, number)

# Function to clear the display
def button_clear():
    display.delete(0, tk.END)

# Function to delete the last character
def button_delete():
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current[:-1])

# Function to calculate the result
def button_equal():
    try:
        math_expression = display.get()
        answer = eval(math_expression)

        display.delete(0, tk.END)
        display.insert(0, answer)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

def key_press(event):
    key = event.char

    if key in "0123456789+-*/.": # Allow digits and operators
        button_click(key)
    elif event.keysym == "Return": # Press Enter to calculate
        button_equal()
    elif event.keysym == "BackSpace": # Press Backspace to delete the last character
        button_delete()
    elif event.keysym == "Escape": # Press Escape to clear the display
        button_clear()

display = tk.Entry(root, width=24, borderwidth=5, font=("Arial", 24), justify="right")
display.grid(row=0, column=0, columnspan=4)

button_7 = tk.Button(root, text="7", padx=40, pady=20, font=("Arial", 12), command=lambda: button_click(7))
button_7.grid(row=1, column=0)

button_8 = tk.Button(root, text="8", padx=40, pady=20, font=("Arial", 12), command=lambda: button_click(8))
button_8.grid(row=1, column=1)

button_9 = tk.Button(root, text="9", padx=40, pady=20, font=("Arial", 12), command=lambda: button_click(9))
button_9.grid(row=1, column=2)

button_divide = tk.Button(root, text="/", padx=40, pady=20, font=("Arial", 12), bg="yellow", fg="black", command=lambda: button_click("/"))
button_divide.grid(row=1, column=3)

button_4 = tk.Button(root, text="4", padx=40, pady=20, font=("Arial", 12), command=lambda: button_click(4))
button_4.grid(row=2, column=0)

button_5 = tk.Button(root, text="5", padx=40, pady=20, font=("Arial", 12), command=lambda: button_click(5))
button_5.grid(row=2, column=1)

button_6 = tk.Button(root, text="6", padx=40, pady=20, font=("Arial", 12), command=lambda: button_click(6))
button_6.grid(row=2, column=2)

button_multiply = tk.Button(root, text="x", padx=40, pady=20, font=("Arial", 12), bg="yellow", fg="black", command=lambda: button_click("*"))
button_multiply.grid(row=2, column=3)

button_1 = tk.Button(root, text="1", padx=40, pady=20, font=("Arial", 12), command=lambda: button_click(1))
button_1.grid(row=3, column=0)

button_2 = tk.Button(root, text="2", padx=40, pady=20, font=("Arial", 12), command=lambda: button_click(2))
button_2.grid(row=3, column=1)

button_3 = tk.Button(root, text="3", padx=40, pady=20, font=("Arial", 12), command=lambda: button_click(3))
button_3.grid(row=3, column=2)

button_subtract = tk.Button(root, text="-", padx=40, pady=20, font=("Arial", 12), bg="yellow", fg="black", command=lambda: button_click("-"))
button_subtract.grid(row=3, column=3)

button_0 = tk.Button(root, text="0", padx=40, pady=20, font=("Arial", 12), command=lambda: button_click(0))
button_0.grid(row=4, column=0)

button_decimal = tk.Button(root, text=".", padx=40, pady=20, font=("Arial", 12), command=lambda: button_click("."))
button_decimal.grid(row=4, column=1)

btn_equal = tk.Button(root, text="=", padx=40, pady=20, font=("Arial", 12), command=button_equal)
btn_equal.grid(row=4, column=2)

button_add = tk.Button(root, text="+", padx=40, pady=20, font=("Arial", 12), bg="yellow", fg="black", command=lambda: button_click("+"))
button_add.grid(row=4, column=3)

button_clear_btn = tk.Button(root, text="Clear", padx=80, pady=20, font=("Arial", 12), bg="red", fg="white", command=button_clear)
button_clear_btn.grid(row=5, column=0, columnspan=2)

button_delete_btn = tk.Button(root, text="Delete", padx=77, pady=20, font=("Arial", 12), bg="orange", fg="black", command=button_delete)
button_delete_btn.grid(row=5, column=2, columnspan=2)

root.bind("<Key>", key_press)
root.mainloop()