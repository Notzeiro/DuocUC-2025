import tkinter as tk

root = tk.Tk()

root.geometry("800x500")
root.title("Etesech")

label= tk.Label(root, text="Hola Mundo!" , font=('Calibri' , 18))
label.pack(padx=20 , pady=20)

textbox= tk.Text(root , font = ('Arial' , 16) , height= 3)
textbox.pack(padx=10)

button = tk.Button(root , text="click me" , font = ('Arial' , 21))
button.pack(pady=10)


buttonframe=tk.Frame(root)
buttonframe.columnconfigure(0 , weight=1  )    
buttonframe.columnconfigure(1 , weight=1  )    
buttonframe.columnconfigure(2 , weight=1  )    

btn1 = tk.Button(buttonframe , text='1' , font= ('arial' , 16))
btn1.grid(row=0 , column=0 , sticky=tk.W+tk.E)

# if button:
#    congratulations= tk.Label(root , text = 'elpepe, gracias por clickear!' , font = ('calibri' , 18))
#    congratulations.pack(padx=10 , pady=10)

root.mainloop()


    