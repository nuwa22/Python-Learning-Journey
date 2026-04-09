import customtkinter as ctk
import tkinter as tk 

# Set the appearance and color theme
ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("blue")


root = ctk.CTk()
root.title("Modern Digital Calculator")

def button_click(number):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, str(current) + str(number))

def button_clear():
    display.delete(0, tk.END)

def button_delete():
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current[:-1])

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
    if key in '0123456789+-*/.':
        button_click(key)
    elif event.keysym == 'Return':
        button_equal()
    elif event.keysym == 'BackSpace':
        button_delete()
    elif event.keysym == 'Escape':
        button_clear()

root.bind('<Key>', key_press)

# Create the display and buttons
display = ctk.CTkEntry(root, width=310, height=60, font=("Arial", 30), justify="right")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

w = 70 # Button width
h = 60 # Button height
f = ("Arial", 20)

button_7 = ctk.CTkButton(root, text="7", width=w, height=h, font=f, command=lambda: button_click(7))
button_7.grid(row=1, column=0, padx=5, pady=5)

button_8 = ctk.CTkButton(root, text="8", width=w, height=h, font=f, command=lambda: button_click(8))
button_8.grid(row=1, column=1, padx=5, pady=5)

button_9 = ctk.CTkButton(root, text="9", width=w, height=h, font=f, command=lambda: button_click(9))
button_9.grid(row=1, column=2, padx=5, pady=5)


button_divide = ctk.CTkButton(root, text="/", width=w, height=h, font=f, fg_color="#FF9500", hover_color="#CC7700", command=lambda: button_click("/"))
button_divide.grid(row=1, column=3, padx=5, pady=5)

button_4 = ctk.CTkButton(root, text="4", width=w, height=h, font=f, command=lambda: button_click(4))
button_4.grid(row=2, column=0, padx=5, pady=5)

button_5 = ctk.CTkButton(root, text="5", width=w, height=h, font=f, command=lambda: button_click(5))
button_5.grid(row=2, column=1, padx=5, pady=5)

button_6 = ctk.CTkButton(root, text="6", width=w, height=h, font=f, command=lambda: button_click(6))
button_6.grid(row=2, column=2, padx=5, pady=5)

button_multiply = ctk.CTkButton(root, text="x", width=w, height=h, font=f, fg_color="#FF9500", hover_color="#CC7700", command=lambda: button_click("*"))
button_multiply.grid(row=2, column=3, padx=5, pady=5)

button_1 = ctk.CTkButton(root, text="1", width=w, height=h, font=f, command=lambda: button_click(1))
button_1.grid(row=3, column=0, padx=5, pady=5)

button_2 = ctk.CTkButton(root, text="2", width=w, height=h, font=f, command=lambda: button_click(2))
button_2.grid(row=3, column=1, padx=5, pady=5)

button_3 = ctk.CTkButton(root, text="3", width=w, height=h, font=f, command=lambda: button_click(3))
button_3.grid(row=3, column=2, padx=5, pady=5)

button_subtract = ctk.CTkButton(root, text="-", width=w, height=h, font=f, fg_color="#FF9500", hover_color="#CC7700", command=lambda: button_click("-"))
button_subtract.grid(row=3, column=3, padx=5, pady=5)

button_0 = ctk.CTkButton(root, text="0", width=w, height=h, font=f, command=lambda: button_click(0))
button_0.grid(row=4, column=0, padx=5, pady=5)

button_decimal = ctk.CTkButton(root, text=".", width=w, height=h, font=f, command=lambda: button_click("."))
button_decimal.grid(row=4, column=1, padx=5, pady=5)

button_equal_btn = ctk.CTkButton(root, text="=", width=w, height=h, font=f, fg_color="#28a745", hover_color="#218838", command=button_equal)
button_equal_btn.grid(row=4, column=2, padx=5, pady=5)

button_add = ctk.CTkButton(root, text="+", width=w, height=h, font=f, fg_color="#FF9500", hover_color="#CC7700", command=lambda: button_click("+"))
button_add.grid(row=4, column=3, padx=5, pady=5)

button_clear_btn = ctk.CTkButton(root, text="Clear", width=150, height=h, font=f, fg_color="#dc3545", hover_color="#c82333", command=button_clear)
button_clear_btn.grid(row=5, column=0, columnspan=2, padx=5, pady=10)

button_delete_btn = ctk.CTkButton(root, text="Delete", width=150, height=h, font=f, fg_color="#6c757d", hover_color="#5a6268", command=button_delete)
button_delete_btn.grid(row=5, column=2, columnspan=2, padx=5, pady=10)

root.mainloop()