from customtkinter import *
from  PIL import Image
from tkinter import ttk,messagebox
import database as db


# Funtions

def delete_all():
    result=messagebox.askyesno('Confitmation','Do you really want to delete all records?')
    if result:
        db.deleteall_records()
def show_all():
    tree_view()
    searchEntry.delete(0,END)
    searchbox.set('Search by')

def search_employee():
    if searchEntry.get()=='':
        messagebox.showerror('Error','Enter value to search')
        
    elif searchbox.get()=='Search by':
        messagebox.showerror('Error','Select an option to search')
        
    else:
        search_data=db.search(searchbox.get(),searchEntry.get())
        tree.delete(*tree.get_children())
        for employee in search_data:
            tree.insert('',END,values=employee)


def delete_employee():
    selected_item=tree.selection()
    if not selected_item:
        messagebox.showerror('Error','Select Data to delete')
    else:
        db.delete(idEntry.get())
        tree_view()
        clear()
        messagebox.showinfo('Success','Data is deleted Successfully')

def update_employee():
    selected_item=tree.selection()
    if not selected_item:
        messagebox.showerror('Error','Select Data to update')
        
    else:
        db.update(idEntry.get(),nameEntry.get(),phoneEntry.get(),rolebox.get(),genderbox.get(),salaryEntry.get())
        tree_view()
        clear()
        messagebox.showinfo('Success','Data is updated')

def selection(event):
    selected_item=tree.selection()
    if selected_item:
        row=tree.item(selected_item)['values']
        clear()
        idEntry.insert(0,row[0])
        nameEntry.insert(0,row[1])
        phoneEntry.insert(0,row[2])
        rolebox.set(row[3])
        genderbox.set(row[4])
        salaryEntry.insert(0,row[5])
    
    
def clear(value=False):
    if value:
        tree.selection_remove(tree.focus())
    idEntry.delete(0,END)
    nameEntry.delete(0,END)
    phoneEntry.delete(0,END)
    rolebox.set('Web Developer')
    genderbox.set('Male')
    salaryEntry.delete(0,END)
    
def tree_view():
    employees=db.fetch_employees()
    tree.delete(*tree.get_children())
    for employee in employees:
        tree.insert('',END,values=employee)

def add_employee():
    if idEntry.get()=='' or nameEntry.get()=='' or salaryEntry.get()=='' or phoneEntry.get()=='':
        messagebox.showerror('Error','All fields are required')
        
    elif db.id_exists(idEntry.get()):
        messagebox.showerror('Error','ID already exists')
        
    elif not idEntry.get().startswith('EMP'):
        messagebox.showerror('Error','Invalid ID format')
    else:
        db.insert(idEntry.get(),nameEntry.get(),phoneEntry.get(),rolebox.get(),genderbox.get(),salaryEntry.get())
        tree_view()
        clear()
        messagebox.showinfo('Success','Data is  succesfully added.')
    

# GUIS
window=CTk()
window.title("Employee Managemenet System")
window.geometry('930x582+100+100')
window.resizable(0,0)
window.configure(fg_color='#161C30')

image1=CTkImage(Image.open('D:/Projects/Employee Management System/21405.png'),size=(930,158))
image1Label=CTkLabel(window,image=image1,text='')
image1Label.grid(row=0,column=0,columnspan=2)


leftframe=CTkLabel(window,text='',fg_color='#161C30')
leftframe.grid(row=1,column=0,stick='w')


idLabel=CTkLabel(leftframe,text='ID',font=('arial',18,'bold'),text_color='white')
idLabel.grid(row=0,column=0,padx=20,pady=15,sticky='w')

idEntry=CTkEntry(leftframe,font=('arial',15,'bold'),width=180)
idEntry.grid(row=0,column=1)


nameLabel=CTkLabel(leftframe,text='Name',font=('arial',18,'bold'),text_color='white')
nameLabel.grid(row=1,column=0,padx=20,pady=15,sticky='w')

nameEntry=CTkEntry(leftframe,font=('arial',15,'bold'),width=180)
nameEntry.grid(row=1,column=1)


phoneLabel=CTkLabel(leftframe,text='Phone',font=('arial',18,'bold'),text_color='white')
phoneLabel.grid(row=2,column=0,padx=20,pady=15,sticky='w')

phoneEntry=CTkEntry(leftframe,font=('arial',15,'bold'),width=180)
phoneEntry.grid(row=2,column=1)

roleLabel=CTkLabel(leftframe,text='Role',font=('arial',18,'bold'),text_color='white')
roleLabel.grid(row=3,column=0,padx=20,pady=15,sticky='w')

role_Options=['Web Developer','Cloud Architect','Netowrk Engineer','Technical Writer',
              'DevOps Engineer','Data Scientist','Business Analyst','IT Consultant','UI/UX Designer']

rolebox=CTkComboBox(leftframe,values=role_Options,width=180,font=('arial',15,'bold'),state='readonly')
rolebox.grid(row=3,column=1)
rolebox.set(role_Options[0])

genderLabel=CTkLabel(leftframe,text='Gender',font=('arial',18,'bold'),text_color='white')
genderLabel.grid(row=4,column=0,padx=20,pady=15,sticky='w')

gender_Options=['Male','Female','Other']

genderbox=CTkComboBox(leftframe,values=gender_Options,width=180,font=('arial',15,'bold'),state='readonly')
genderbox.grid(row=4,column=1)
genderbox.set(gender_Options[0])

salaryLabel=CTkLabel(leftframe,text='Salary',font=('arial',18,'bold'),text_color='white')
salaryLabel.grid(row=5,column=0,padx=20,pady=15,sticky='w')

salaryEntry=CTkEntry(leftframe,font=('arial',15,'bold'),width=180)
salaryEntry.grid(row=5,column=1)

rightframe=CTkLabel(window,text='',fg_color='#161C30')
rightframe.grid(row=1,column=1)


search_Options=['ID','Gender','Salary','Role','Name','Phone']
searchbox=CTkComboBox(rightframe,values=search_Options,state='readonly')
searchbox.grid(row=0,column=0)
searchbox.set('Search by')

searchEntry=CTkEntry(rightframe)
searchEntry.grid(row=0,column=1,stick='w',padx=5)

searchButton=CTkButton(rightframe,text='Search',width=100,command=search_employee)
searchButton.grid(row=0,column=2,padx=5,stick='w')

showButton=CTkButton(rightframe,text='Show All',width=100,command=show_all)
showButton.grid(row=0,column=3,pady=5,padx=5,stick='w')

tree=ttk.Treeview(rightframe,height=13)
tree.grid(row=1,column=0,columnspan=4)

tree['column']=('ID','Name','Phone','Role','Gender','Salary')

tree.heading('ID',text='ID')
tree.heading('Name',text='Name')
tree.heading('Phone',text='Phone')
tree.heading('Role',text='Role')
tree.heading('Gender',text='Gender')
tree.heading('Salary',text='Salary')

tree.config(show='headings')
tree.column('ID',anchor=CENTER,width=80)
tree.column('Name',anchor=CENTER,width=135)
tree.column('Phone',anchor=CENTER,width=135)
tree.column('Role',anchor=CENTER,width=175)
tree.column('Gender',anchor=CENTER,width=95)
tree.column('Salary',anchor=CENTER,width=140)

style=ttk.Style()
style.configure('Treeview.Heading',font=('arial',18,'bold'))
style.configure('Treeview',font=('arial',12,'bold'),rowheight=24,background='#161C30',foreground='white')

scrollbar=ttk.Scrollbar(rightframe,orient=VERTICAL,command=tree.yview)
scrollbar.grid(row=1,column=4,sticky='ns')

tree.config(yscrollcommand=scrollbar.set)

buttonframe=CTkFrame(window,fg_color='#161C30')
buttonframe.grid(row=2,column=0,columnspan=2,pady=10)

newButton=CTkButton(buttonframe,text='New Employee',font=('arial',15,'bold'),width=160,corner_radius=15,command=lambda: clear(True))
newButton.grid(row=0,column=0,pady=5,padx=5)

addButton=CTkButton(buttonframe,text='Add Employee',font=('arial',15,'bold'),width=160,corner_radius=15,command=add_employee)
addButton.grid(row=0,column=1,pady=5,padx=5)

updateButton=CTkButton(buttonframe,text='Update Employee',font=('arial',15,'bold'),width=160,corner_radius=15,command=update_employee)
updateButton.grid(row=0,column=2,pady=5,padx=5)

deleteButton=CTkButton(buttonframe,text='Delete Employee',font=('arial',15,'bold'),width=160,corner_radius=15,command=delete_employee)
deleteButton.grid(row=0,column=3,pady=5,padx=5)

delete_allButton=CTkButton(buttonframe,text='Delete All ',font=('arial',15,'bold'),width=160,corner_radius=15,command=delete_all)
delete_allButton.grid(row=0,column=4,pady=5,padx=5)

tree_view()

window.bind('<ButtonRelease>',selection)
window.mainloop()