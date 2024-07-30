from tkinter import *
from PIL import ImageTk,Image
from functools import partial
import mysql.connector
import sqlite3
import mysql.connector as sqltor
from tkinter import messagebox
#import customtkinter

def search():
    window.destroy()
    import search
    return

def Ticket():
    
    window.destroy()
    import Ticket
    return

window=Tk()
window.title('MyRail')
window.geometry("990x660")
bgimage=ImageTk.PhotoImage(file='logggg.jpg')
bglabel=Label(window,image=bgimage)
bglabel.place(x=0,y=0)

loginButton = Button(window, text="Search Trains", command=search,width=11,height=2,bg='#ffffff',font=('Poppins','20','bold'),bd=0).place(x=500,y=160) 
loginButton2 = Button(window, text="Book Now!", command=Ticket,width=10,height=1,bg='#ffffff',font=('','20','bold'),bd=0).place(x=520,y=550) 

#window.state('zoomed')
window.mainloop()
