from hashlib import blake2b
import tkinter
import random
from tkinter.ttk import Button, Label
from turtle import onclick 

root = tkinter.Tk()
root.geometry('400x400')
Title=root.title("                                                                  Dice Simulator     "  )
Title1=tkinter.Label(root , text=" ")



root.config(bg="Black")


image = []
img = tkinter.PhotoImage(file=r"C:\Users\win\Pictures\dice1.png")
image.append(img)
img = tkinter.PhotoImage(file=r"C:\Users\win\Pictures\dice2.png")
image.append(img)
img = tkinter.PhotoImage(file=r"C:\Users\win\Pictures\dice3.png")
image.append(img)
img = tkinter.PhotoImage(file=r"C:\Users\win\Pictures\dice4.png")
image.append(img)
img = tkinter.PhotoImage(file=r"C:\Users\win\Pictures\dice5.png")
image.append(img)
img = tkinter.PhotoImage(file=r"C:\Users\win\Pictures\dice6.png")
image.append(img)

label1=Label(root , image=img , font="Helvetica 16 bold italic")
label1.place(x=570,y=200)

def dice_number() :
 
          print(" Rolling .....")
          number=random.randint(0,5)
          print("Dice nu,ber : " , number)

          label1.config(image=image[number])
              

label=tkinter.Label(root , text="Let's roll a dice  ! ")
label.pack(ipadx=20,ipady=20 , pady=30 , padx=100)


button=tkinter.Button(root, text=" Click to roll ",command=dice_number)
button.place(x=650,y=550 )


root.mainloop()

