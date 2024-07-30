import mysql.connector

conn=mysql.connector.connect(host='localhost',username='root',password='#Divi4321',database='project')
my_cursor=conn.cursor()

conn.commit()
conn.close()

print("Connection successfull")