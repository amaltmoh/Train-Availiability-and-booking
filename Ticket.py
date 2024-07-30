from tkinter import *
from PIL import ImageTk,Image
from functools import partial
import mysql.connector
import sqlite3
import mysql.connector as sqltor
from tkinter import messagebox
#import customtkinter
from datetime import datetime,date,timedelta

def ticket(trainno,dt):
    t=trainno.get()
    d=dt.get()
    conn=mysql.connector.connect(host='localhost',username='root',password='#Divi4321',database='project')
    my_cursor=conn.cursor()
    to=datetime.today()
    t1=datetime.today()+timedelta(1)
    t2=datetime.today()+timedelta(2)
    t3=datetime.today()+timedelta(3)
    t4=datetime.today()+timedelta(4)
    t5=datetime.today()+timedelta(5)
    my_cursor.execute("select TNo from route")
    rec=my_cursor.fetchall()
    f=0
    for i in rec:
        if(int(t)==i[0]):
            print("Train available")
            f=1
    if(f==1):
        #print("Train not available")
        print(type(to))
        d1=datetime.strptime(d,'%Y-%m-%d')
        print(type(d1))
        print(d1.date())
        print(to.date())
        if(to.date()==d1.date()):
            my_cursor.execute(f"select today from route where TNo='{t}'")
            records=my_cursor.fetchall()
            if((records[0][0])>0):
                usernameLabel = Label(window, text="Booked Successfully!",font=('Open Sans','22','bold'),bg='#000000',fg='#ffffff').place(x=80,y=320)
                my_cursor.execute(f"update route set today=today-1 where TNo='{t}'")
            else:
                usernameLabel = Label(window, text="Tickets are filled up!",font=('Open Sans','22','bold'),bg='#000000',fg='#ffffff').place(x=80,y=320)
        elif(t1.date()==d1.date()):
            my_cursor.execute(f"select first from route where TNo='{t}'")
            records=my_cursor.fetchall()
            if((records[0][0])>0):
                usernameLabel = Label(window, text="Booked Successfully!",font=('Open Sans','22','bold'),bg='#000000',fg='#ffffff').place(x=80,y=320)
                my_cursor.execute(f"update route set first=first-1 where TNo='{t}'")
            else:
                usernameLabel = Label(window, text="Tickets are filled up!",font=('Open Sans','22','bold'),bg='#000000',fg='#ffffff').place(x=80,y=320)
        elif(t2.date()==d1.date()):
            my_cursor.execute(f"select second from route where TNo='{t}'")
            records=my_cursor.fetchall()
            if((records[0][0])>0):
                usernameLabel = Label(window, text="Booked Successfully!",font=('Open Sans','22','bold'),bg='#000000',fg='#ffffff').place(x=80,y=320)
                my_cursor.execute(f"update route set second=second-1 where TNo='{t}'")
            else:
                usernameLabel = Label(window, text="Tickets are filled up!",font=('Open Sans','22','bold'),bg='#000000',fg='#ffffff').place(x=80,y=320)
        elif(t3.date()==d1.date()):
            my_cursor.execute(f"select third from route where TNo='{t}'")
            records=my_cursor.fetchall()
            if((records[0][0])>0):
                usernameLabel = Label(window, text="Booked Successfully!",font=('Open Sans','22','bold'),bg='#000000',fg='#ffffff').place(x=80,y=320)
                my_cursor.execute(f"update route set third=third-1 where TNo='{t}'")
            else:
                usernameLabel = Label(window, text="Tickets are filled up!",font=('Open Sans','22','bold'),bg='#000000',fg='#ffffff').place(x=80,y=320)
        elif(t4.date()==d1.date()):
            my_cursor.execute(f"select fourth from route where TNo='{t}'")
            records=my_cursor.fetchall()
            if((records[0][0])>0):
                usernameLabel = Label(window, text="Booked Successfully!",font=('Open Sans','22','bold'),bg='#000000',fg='#ffffff').place(x=80,y=320)
                my_cursor.execute(f"update route set fourth=fourth-1 where TNo='{t}'")
            else:
                usernameLabel = Label(window, text="Tickets are filled up!",font=('Open Sans','22','bold'),bg='#000000',fg='#ffffff').place(x=80,y=320)
        elif(t5.date()==d1.date()):
            my_cursor.execute(f"select fifth from route where TNo='{t}'")
            records=my_cursor.fetchall()
            if((records[0][0])>0):
                usernameLabel = Label(window, text="Booked Successfully!",font=('Open Sans','22','bold'),bg='#000000',fg='#ffffff').place(x=80,y=320)
                my_cursor.execute(f"update route set fifth=fifth-1 where TNo='{t}'")
            else:
                usernameLabel = Label(window, text="Tickets are filled up!",font=('Open Sans','22','bold'),bg='#000000',fg='#ffffff').place(x=80,y=320)
        else:
            usernameLabel = Label(window, text="Date invalid",font=('Open Sans','22','bold'),bg='#000000',fg='#ffffff').place(x=80,y=320)
    else:
        usernameLabel = Label(window, text="Train not available",font=('Open Sans','22','bold'),bg='#000000',fg='#ffffff').place(x=80,y=320)
    conn.commit()
    return

window=Tk()
window.title('MyRail')
window.geometry("990x660")
bgimage=ImageTk.PhotoImage(file='serch.jpg')
bglabel=Label(window,image=bgimage)
bglabel.place(x=0,y=0)


#usernameLabel1=Label(window,text="Login",font=('poppins','48','bold'),bg='#212f33',fg='#F2F7A1').place(x=135,y=100)
usernameLabel = Label(window, text="Train No",font=('Open Sans','11','bold'),bg='#212f33',fg='#ffffff').place(x=80,y=160)
trainno= StringVar()
usernameEntry = Entry(window, textvariable=trainno,bd=0,width=30).place(x=200,y=163)  

#validateLogin = partial(validateLogin, username, password)
datelabel = Label(window,text="YYYY-MM-DD",font=('Open Sans','11','bold'),bg='#212f33',fg='#ffffff').place(x=560, y=160)  
dt = StringVar()
passwordEntry = Entry(window, textvariable=dt,bd=0,width=30).place(x=720,y=163)

ticket= partial(ticket,trainno,dt)

# Login button
loginButton = Button(window, text="Book Tickets", command=ticket,width=10,height=1,bg='#0870e4',font=('Open Sans','22','bold')).place(x=370,y=220) 



#window.state('zoomed')
window.mainloop()
