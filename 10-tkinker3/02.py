import tkinter as tk 
import random
root = tk.Tk()
root.geometry("200x200")

pokus = 1
def akcia():
    global pokus
    CisloMoje = text = textbox.get()
    if int(CisloMoje) < random_cislo:
        label.config(text=f"dal si menšie číslo pokus:{pokus}")
        pokus +=1
    elif int(CisloMoje) > random_cislo:
        label.config(text= f"dal si väčšie číslo pokus:{pokus}")
        pokus +=1
    elif int(CisloMoje) == random_cislo:
        label.config(text=f"Uhádol si pokus:{pokus}")

    
    


   

random_cislo=random.randint(0,9)

label= tk.Label(root,text="hádaj")
label.pack()

textbox=tk.Entry(root)
textbox.pack()



button=tk.Button(root, command=akcia)
button.pack()

if textbox == random_cislo:
    label3=tk.Label(root,text="Správne!")
    label3.pack()




root.mainloop()