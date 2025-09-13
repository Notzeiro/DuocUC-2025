import tkinter as tk
from tkinter import messagebox

class MyGUI:
    def __init__(self):
        
        self.root = tk.Tk()

        self.root.title("Program")
        self.label = tk.Label(self.root, text="your message" , font=("arial" , 18))
        self.label.pack(padx=10 , pady=10)

        self.textbox = tk.Text(self.root , font=("arial" , 18)) 
        self.textbox.pack(padx=10 , pady=10)

        self.check_state = tk.IntVar()

        self.check = tk.Checkbutton(self.root , text="show messagebox" , font=("arial" , 16) , variable=self.check_state)
        self.check.pack(padx=10 , pady=10)


        self.button = tk.Button(self.root , text="show message" , font=("arial" , 18) , command=self.show_message)
        self.button.pack(padx=10 , pady=10)

        self.root.mainloop()
    def show_message(self):
        print("momos en video")

MyGUI()