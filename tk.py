from tkinter import *
from PIL import ImageTk,Image
from functools import partial
import mysql.connector
import sqlite3
import mysql.connector as sqltor
from tkinter import messagebox
#import customtkinter

def validateLogin(username, password):
	conn=mysql.connector.connect(host='localhost',username='root',password='#Divi4321',database='project')
	my_cursor=conn.cursor()
	u=username.get()
	p=password.get()
	print("Username:",u)
	print("Password:",p)
	str="""select * from login"""
	my_cursor.execute(str)
	records=my_cursor.fetchall()
	f=0;
	for i in records:
		if(u==i[0] and p==i[1]):
			print("Access granted")
			f=1
			window.destroy()
			import user
		else:
			continue
	if(f==0):
		print("Access denied")
		messagebox.showerror("Login Failed", "Invalid username or password")
	conn.commit()
	conn.close()
	
	return




window=Tk()
window.title('MyRail')
window.geometry("990x660")
#img=Image.open("train.jpg")
#img=img.resize((1550,400))
#bg1=bg.copy()
#bg=ImageTk.PhotoImage(img)
#label=Label(window,image=bg,width=0,height=0)
#label.pack()

#l1=Label(window,background='black',width=50,height=50)
#l1.pack()

#frame= Frame(window, relief= 'raised', bg= "#3C2A21",width=400,height=400)
#frame.pack()
#frame.config(width=100)
bgimage=ImageTk.PhotoImage(file='logon.jpg')
bglabel=Label(window,image=bgimage)
bglabel.place(x=0,y=0)

usernameLabel1=Label(window,text="Login",font=('poppins','48','bold'),bg='#212f33',fg='#F2F7A1').place(x=135,y=100)
usernameLabel = Label(window, text="User Name",font=('Open Sans','11','bold'),bg='#212f33',fg='#ffffff').place(x=80,y=280)
username = StringVar()
usernameEntry = Entry(window, textvariable=username,bd=0,width=30).place(x=190,y=285)  

# Password label and password entry box
passwordLabel = Label(window,text="Password",font=('Open Sans','11','bold'),bg='#212f33',fg='#ffffff').place(x=80, y=320)  
password = StringVar()
passwordEntry = Entry(window, textvariable=password, show='*',bd=0,width=30).place(x=190,y=325)

validateLogin = partial(validateLogin, username, password)

btnimg=PhotoImage(file='btn1.png')
imglbl=Label(image=btnimg)
# Login button
loginButton = Button(window, text="Login", command=validateLogin,width=5,height=1,font=('Open Sans','22','bold'),bd=0,bg='#5FBDFF',fg='#000000').place(x=170,y=380) 
window.resizable(False, False)
#window.state('zoomed')
window.mainloop()
