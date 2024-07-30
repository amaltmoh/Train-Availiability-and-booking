from tkinter import *
from PIL import ImageTk,Image
from functools import partial
import mysql.connector
import sqlite3
import mysql.connector as sqltor
from tkinter import messagebox
#import customtkinter
from datetime import datetime

def sching(source,destination,f):
    #f1=f.get()
    print(f)
    if(f==1):
        print("aaaaaa")
        Tno.after(1000,Tno.destroy())
        Tname.after(1000,Tname.destroy())
        tm.after(1000,tm.destroy())
    c=0
    s=source.get()
    d=destination.get()
    #t=dt.get()
    conn=mysql.connector.connect(host='localhost',username='root',password='#Divi4321',database='project')
    my_cursor=conn.cursor()
    my_cursor.execute(f"select TID,TName,time from v3 where SNAME='{s}' and DNAME='{d}'")
    records=my_cursor.fetchall();
    Tno = Label(window, text="Train No",font=('Open Sans','12'),bg='#000000',fg='#ffffff').place(x=80,y=320+c)
    Tname = Label(window, text="Train Name",font=('Open Sans','12'),bg='#000000',fg='#ffffff').place(x=200,y=320+c)
    tm = Label(window, text="Time",font=('Open Sans','12'),bg='#000000',fg='#ffffff').place(x=320,y=320+c)
    for i in records:
        now = datetime.now()
        current_time = now.strftime("%H")
        #print("Current Time =", current_time)
        #tom=i[2]
        #print(tom)
        #print(int(current_time))
        #if(int(current_time)<int(tom[0:2])):
            #print(int(tom[0:2]))
            #print(int(current_time))
        Tno = Label(window, text=i[0],font=('Open Sans','18'),bg='#000000',fg='#ffffff').place(x=80,y=360+c)
        Tname = Label(window, text=i[1],font=('Open Sans','18'),bg='#000000',fg='#ffffff').place(x=200,y=360+c)
        tm = Label(window, text=i[2],font=('Open Sans','18'),bg='#000000',fg='#ffffff').place(x=320,y=360+c)
        c+=40
        f=f+1
        print(f)
    return
f=0
window=Tk()
window.title('MyRail')
window.geometry("990x660")
#window.wm_attributes('-transparentcolor','black')
bgimage=ImageTk.PhotoImage(file='serch.jpg')
bglabel=Label(window,image=bgimage)
bglabel.place(x=0,y=0)

#usernameLabel1=Label(window,text="Login",font=('poppins','48','bold'),bg='#212f33',fg='#F2F7A1').place(x=135,y=100)
usernameLabel = Label(window, text="Source:",font=('Open Sans','16','bold'),fg='#ffffff',bg='#000000',bd=0).place(x=80,y=160)
source= StringVar()
usernameEntry = Entry(window, textvariable=source,bd=0,width=30).place(x=200,y=163)  

# Password label and password entry box
passwordLabel = Label(window,text="Destination:",font=('Open Sans','16','bold'),fg='#ffffff',bg='#000000',bd=0).place(x=560,y=160)  
destination = StringVar()
passwordEntry = Entry(window, textvariable=destination,bd=0,width=30).place(x=720,y=163)
#validateLogin = partial(validateLogin, username, password)
sching= partial(sching,source,destination,f)

# Login button
loginButton = Button(window, text="Search", command=sching,width=7,height=1,bg='#3e1af0',font=('Arial Black','22','bold'),bd=0).place(x=405,y=220) 

#window.state('zoomed')
window.mainloop()
