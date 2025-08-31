import pymysql
from tkinter import messagebox
def connect_database():
    global mycursor,conn
    try:
        conn=pymysql.connect(host='localhost',port=3306,user='root',password='Moshim@123')
        mycursor=conn.cursor()
    except:
        messagebox.showerror('Error','Connection failed')
        return
        
    mycursor.execute('create database if not exists employee_data')
    mycursor.execute('use employee_data')
    mycursor.execute('''create table if not exists data (
        ID Varchar(20),
        Name varchar(40),
        Phone varchar(15),
        Role varchar(30),
        gender varchar(15),
        salary decimal(10,2)
        )''')
    


def insert(id,name,phone,role,gender,salary):
    mycursor.execute('insert into data values (%s,%s,%s,%s,%s,%s)',(id,name,phone,role,gender,salary))
    conn.commit()
    
def id_exists(id):
    mycursor.execute('select count(*) from data where id=%s',id)
    result=mycursor.fetchone()
    return result[0]>0


def fetch_employees():
    mycursor.execute('select * from data')
    result=mycursor.fetchall()
    return result
    
    
def update(id,new_name,new_phone,new_role,new_gender,new_salary):
    mycursor.execute('update data set name=%s,phone=%s,role=%s,gender=%s,salary=%s where id=%s',(new_name,new_phone,new_role,new_gender,new_salary,id))
    conn.commit()
    
def delete(id):
    mycursor.execute('delete from data where id=%s',id)
    conn.commit()
    
def search(option ,value):
    mycursor.execute(f'select * from  data where {option}=%s',value)
    result=mycursor.fetchall()
    return result
    
def deleteall_records():
    mycursor.execute('truncate  table data')
    conn.commit() 
    
    
connect_database()