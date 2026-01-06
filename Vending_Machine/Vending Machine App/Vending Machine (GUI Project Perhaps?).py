import tkinter as tk
from tkinter import *
from Vend_backend import *
import Vend_backend

window = tk.Tk()
window.title("Vending Machine App")
window.geometry("400x300")
window.configure(bg='lightgray') #Can change later



label = Label(window,
            text="Welcome to the weird Vending Machine!",
            font=("Times New Roman", 16,'bold'),
            fg="black",
            bg="lightgray", #match with window bg color
            relief=RAISED,
            bd=10,
)

if vend_item():
    label.pack


button = Button(window,
                text="Vend Item",
                font=("Arial", 14),
                fg="white",
                bg="blue",
                relief=RAISED,
                bd=5,
                command=Vend_backend.vend_item
)
button.pack(pady=20)
    
#FIX THIS WAATCH YOUTUBE TUTORIALS

exit_button = Button(window,
    text="Exit",
    font=("Arial", 14),
    fg="white",
    bg="red",
    relief=RAISED,
    bd=5,
    command=window.quit
)

window.mainloop()
