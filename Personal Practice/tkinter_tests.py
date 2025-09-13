import tkinter as tk

root = tk.Tk()

root.geometry("800x500")
root.title("Test program")

label= tk.Label(root, text="Hello world!" , font=('Calibri' , 18))
label.pack(padx=20 , pady=20)

# textbox= tk.Text(root , font = ('Arial' , 16) , height= 3)
# textbox.pack(padx=10)

# button = tk.Button(root , text="click me" , font = ('Arial' , 21))
# button.pack(pady=10)


# buttonframe=tk.Frame(root)
# buttonframe.columnconfigure(0 , weight=1  )    
# buttonframe.columnconfigure(1 , weight=1  )    
# buttonframe.columnconfigure(2 , weight=1  )    

# btn1 = tk.Button(buttonframe , text='1' , font= ('arial' , 16))
# btn1.grid(row=0 , column=0 , sticky=tk.W+tk.E)

# if button:
#    congratulations= tk.Label(root , text = 'elpepe, gracias por clickear!' , font = ('calibri' , 18))
#    congratulations.pack(padx=10 , pady=10)

label_2=tk.Label(root , text="Enter your user: ")
label_2.pack()

user_entry = tk.Entry()
user_entry.pack(padx=10 , pady=10)


buttonframe=tk.Frame(root)
buttonframe.columnconfigure(0 , weight=1)
buttonframe.columnconfigure(1 , weight=1)
buttonframe.columnconfigure(2 , weight=1)
button1=tk.Button(buttonframe , text="HOLA", font=("Arial" , 18))
button1.grid(column=0 , row=0 , sticky=tk.W + tk.E)

button2=tk.Button(buttonframe , text="2" , font=("Arial" , 18))
button2.grid(column=1 , row=0 , sticky=tk.W + tk.E)

button3=tk.Button(buttonframe , text="3", font=("Arial" , 18))
button3.grid(column=2 , row=0 , sticky=tk.W + tk.E)

button4=tk.Button(buttonframe , text="4", font=("Arial" , 18))
button4.grid(column=0 , row=1 , sticky=tk.W + tk.E)

button5=tk.Button(buttonframe , text="5", font=("Arial" , 18))
button5.grid(column=1 , row=1 , sticky=tk.W + tk.E)

button6=tk.Button(buttonframe , text="6", font=("Arial" , 18))
button6.grid(column=2 , row=1 , sticky=tk.W + tk.E)


buttonframe.pack(fill="x")




root.mainloop()

