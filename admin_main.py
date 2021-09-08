import math,random,os
from tkinter import messagebox
import barcode
import errno
import os
from tkinter import*
import webbrowser
import tkinter as tk
import datetime
import tkinter.messagebox
from tkinter import ttk
from ivm import *


def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Patient Register")
    register_screen.geometry("500x300")

    global username
    global password
    global age
    global bg
    global ol
    global username_entry
    global password_entry
    global age_entry
    global bg_entry
    global ol
    username = StringVar()
    password = StringVar()
    age = StringVar()
    bg = StringVar()
    ol = StringVar()
    Label(register_screen,width="300", text="Please enter details below", bg="blue",fg="white",font=("Calibri", 17)).pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Mobile number or email address* ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    age_lable = Label(register_screen, text="Enter Age * ")
    age_lable.pack()
    age_entry = Entry(register_screen, textvariable=age)
    age_entry.pack()
    bg_lable = Label(register_screen, text="Enter Blood Group * ")
    bg_lable.pack()
    bg_entry = Entry(register_screen, textvariable=bg)
    bg_entry.pack()
    ol_lable = Label(register_screen, text="Enter Oxygen Level * ")
    ol_lable.pack()
    ol_entry = Entry(register_screen, textvariable=ol)
    ol_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Button(register_screen, text="Register", width=10, height=1, bg="blue",fg="white", command = register_user).pack(pady=10)
 
# Designing window for login 

def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Patient Login")
    login_screen.geometry("400x225")
    Label(login_screen, text="Please enter details below to login",bg="blue", width="300",fg="white",font=("Calibri", 17)).pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry
    
    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, bg="blue",fg="white", command = login_verify).pack()
    
# Implementing event on register button

def register_user():

    username_info = username.get()
    age_info =age.get()
    bg_info= bg.get()
    ol_info=ol.get()
    password_info = password.get() 
    
    
   
    list_of_files = os.listdir("./patients")
    if username_info in list_of_files:
        messagebox.showinfo("Title", "User exist")
    elif username_info not in list_of_files:
       if(username_info=="" and password_info==""):
           messagebox.showinfo("Title", "No details entered")
       elif(username_info=="" or password_info==""):
           messagebox.showinfo("Title", "Insufficient details")
       else:
           username_info = username.get()
           age_info =age.get()
           bg.get=bg.get()
           ol.get=ol.get()
           password_info = password.get()
           
           file = open("./patients/"+username_info+".txt", "w")
           file.write("Username: "+username_info + "\n")
           file.write("Age: "+age_info + "\n")
           file.write("BloodGroup: "+bg_info + "\n")
           file.write("OxygenLevel: "+ol_info + "\n")
           file.write("Password: "+password_info)
           messagebox.showinfo(title=None, message="Patient registered successfully")
           file.close()
           


    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
    register_screen.destroy()
    

# Implementing event on login button 

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    # username_login_entry.delete(0, END)
    # password_login_entry.delete(0, END)


    list_of_files = os.listdir("./patients")
    list_of_files = [username[:-4] for username in list_of_files]
    print(list_of_files)
    if username1 in list_of_files:
        file1 = open("./patients/"+username1+".txt", "r")
        verify = file1.read().splitlines()
        verify = verify[-1].split(":")[1]
        if password1 in verify:
            login_sucess()   
        else:
            password_not_recognised()
    else:
        user_not_found()

def patients_details():
    global list_patients_details
    list_patients_details = Toplevel(main_screen)
    list_patients_details.title("Patient Details")
    list_patients_details.geometry("250x600")
    files = os.listdir('./patients')
    x_axis = 0
    y_axis = 0
    for file in files:
        if(y_axis >= 500):
            y_axis = 0
            x_axis = 250
        Label(list_patients_details, text=file).place(x=x_axis,y=y_axis)
        Button(list_patients_details, text="Open", bg="grey",fg="white",command=lambda file = file:open_file('./patients/'+file)).place(x=x_axis+150,y=y_axis)
        Button(list_patients_details, text="Delete",bg="grey",fg="white",command=lambda file = file:delete_file('./patients/'+file)).place(x=x_axis+200,y=y_axis)
        y_axis += 50
     
def open_file(file_name):
    global file_win
    file_win = Toplevel(list_patients_details)
    global edited
    edited = StringVar()
    file_win.geometry('500x250')
    with open(file_name,'r') as f:
        #print(f.read().splitlines())
        details = f.read().splitlines()
        x_axis = 0
        y_axis = 0
        for det in details:
            #print(det)
            globals()[f'label{det.split(":")[0]}']=Label(file_win,text=det)
            eval("label"+det.split(":")[0]+".place(x=x_axis,y=y_axis)")
            globals()[f'button{det.split(":")[0]}']=Button(file_win,bg="grey",fg="white",text="Edit",command=lambda det = det:show_entry(details.index(det),file_name,det,x_axis,y_axis))
            # Entry(file_win,textvariable=edited).pack_forget()
            eval("button"+det.split(":")[0]+".place(x=x_axis+200,y=y_axis)")
            y_axis += 50
            globals()[f'entry{det.split(":")[0]}']=Entry(file_win,textvariable=edited)
            
def delete_file(filename):
    global list_patients_details
    os.remove(filename)
    list_patients_details.destroy()
    patients_details()

def show_entry(index,filename,det,x_axis,y_axis):
    global file_win
    global edit
    edit=StringVar()
    y_index = {0:0,1:50,2:100,3:150,4:200,5:250,6:300,7:350}
    y_axis = y_index[index]
    eval("button"+det.split(":")[0]+".place_forget()")
    eval("entry"+det.split(":")[0]+".place(x="+str(x_axis+250)+",y="+str(y_axis)+")")  
    globals()[f'confirm{det.split(":")[0]}'] = Button(file_win,text="OK",command=lambda det = det:edit_details(index,filename,det,x_axis,y_axis))
    eval("confirm"+det.split(":")[0]+".place(x=x_axis+400,y=y_axis)")

def edit_details(index,filename,det,x_axis,y_axis):
    global edited
    edit = edited.get()
    print(edit)
    file = open(filename, "r")
    list_of_lines = file.readlines()
    update = det.split(":")[0]+": "+edit+"\n"
    list_of_lines[index] = update
    globals()[f'label{det.split(":")[0]}']['text'] = update.strip()
    eval("button"+det.split(":")[0]+".place(x=x_axis+250,y=y_axis)")
    eval("confirm"+det.split(":")[0]+".place_forget()")
    eval("entry"+det.split(":")[0]+".delete(0,END)")
    eval("entry"+det.split(":")[0]+".place_forget()")
    file = open(filename, "w")
    file.writelines(list_of_lines)
    file.close()

def patients_removeall():
    dir_name = "./patients/"
    test = os.listdir(dir_name)

    for item in test:
        if item.endswith(".txt"):
         os.remove(os.path.join(dir_name, item))
    messagebox.showinfo(title=None, message="Patients removed successfully")
  
    # Designing popup for login success
def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=open1).pack()

def open1():
    
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Book Resource")
    login_success_screen.geometry("800x800")
    Label(login_success_screen, text="Only one click at a time allowed, kindly re-login if required").pack()
    Label(login_success_screen,text="").pack() 
    globals()['btn1']=Button(login_success_screen,command = lambda: resource_dashboard(0),text="covishield",height="2", width="30")
    globals()['btn1'].pack()
    Label(login_success_screen,text="").pack() 
    globals()['btn2']=Button(login_success_screen,command= lambda: resource_dashboard(1),text="covaxin",height="2", width="30")
    globals()['btn2'].pack()
    Label(login_success_screen,text="").pack() 
    globals()['btn3']=Button(login_success_screen,command= lambda: resource_dashboard(2),text="sputnik",height="2", width="30")
    globals()['btn3'].pack()
    Label(login_success_screen,text="").pack()  
    globals()['btn4']=Button(login_success_screen,command= lambda: resource_dashboard(3),text="Beds",height="2", width="30")
    globals()['btn4'].pack()
    Label(login_success_screen,text="").pack()  
    globals()['btn5']=Button(login_success_screen,command= lambda: resource_dashboard(4),text="OxygenCylinder",height="2", width="30")
    globals()['btn5'].pack()

def resource_dashboard(index):

    file_name='./Resource/resource.txt'
    file = open(file_name,"r")
    list_of_lines = file.readlines()
    update = list_of_lines[index].split(":")[0]+":"+str(int(list_of_lines[index].split(":")[1]) - 1)+"\n"
    list_of_lines[index] = update
    file = open(file_name, "w")
    file.writelines(list_of_lines)
    file.close()
    
    globals()['btn1']['state'] = 'disabled'
    globals()['btn2']['state'] = 'disabled'
    globals()['btn3']['state'] = 'disabled'
    globals()['btn4']['state'] = 'disabled'
    globals()['btn5']['state'] = 'disabled'
    login_success_screen.destroy()
    login_screen.destroy()
    main_screen.destroy()
    main_account_screen()
    
 
def display_resource():
    global list_resource_details
    list_resource_details = Toplevel(main_screen)
    list_resource_details.title("Resource Details")
    list_resource_details.geometry("400x40")
    files = os.listdir('./Resource/')
    x_axis = 0
    y_axis = 0
    for file in files:
        if(y_axis >= 500):
            y_axis = 0
            x_axis = 250
        Label(list_resource_details,width="300", text="Click    open   to view resource dashboard", bg="blue",fg="white").pack()
        Label(list_resource_details, text="").pack()
        Button(list_resource_details, text="Open",height="1", command=lambda file = file:open_file1('./Resource/'+file)).place(x=x_axis+120,y=y_axis)
        y_axis += 50
    
    
def open_file1(file_name):
    global file_win
    file_win = Toplevel(list_resource_details)
    global edited
    edited = StringVar()
    file_win.geometry('500x250')
    with open(file_name,'r') as f:
        #print(f.read().splitlines())
        details = f.read().splitlines()
        x_axis = 0
        y_axis = 0
        for det in details:
            #print(det)
            globals()[f'label{det.split(":")[0]}']=Label(file_win,text=det)
            eval("label"+det.split(":")[0]+".place(x=x_axis,y=y_axis)")
            globals()[f'button{det.split(":")[0]}']=Button(file_win,bg="grey",fg="white",text="Edit",command=lambda det = det:show_entry1(details.index(det),file_name,det,x_axis,y_axis))
            # Entry(file_win,textvariable=edited).pack_forget()
            eval("button"+det.split(":")[0]+".place(x=x_axis+200,y=y_axis)")
            y_axis += 50
            globals()[f'entry{det.split(":")[0]}']=Entry(file_win,textvariable=edited)
            
# Designing popup for login invalid password

def show_entry1(index,filename,det,x_axis,y_axis):
    global file_win
    global edit
    edit=StringVar()
    y_index = {0:0,1:50,2:100,3:150,4:200,5:250,6:300,7:350}
    y_axis = y_index[index]
    eval("button"+det.split(":")[0]+".place_forget()")
    eval("entry"+det.split(":")[0]+".place(x="+str(x_axis+250)+",y="+str(y_axis)+")")  
    globals()[f'confirm{det.split(":")[0]}'] = Button(file_win,text="OK",command=lambda det = det:edit_details1(index,filename,det,x_axis,y_axis))
    eval("confirm"+det.split(":")[0]+".place(x=x_axis+400,y=y_axis)")


def edit_details1(index,filename,det,x_axis,y_axis):
    global edited
    edit = edited.get()
    print(edit)
    file = open(filename, "r")
    list_of_lines = file.readlines()
    update = det.split(":")[0]+": "+edit+"\n"
    list_of_lines[index] = update
    globals()[f'label{det.split(":")[0]}']['text'] = update.strip()
    eval("button"+det.split(":")[0]+".place(x=x_axis+250,y=y_axis)")
    eval("confirm"+det.split(":")[0]+".place_forget()")
    eval("entry"+det.split(":")[0]+".delete(0,END)")
    eval("entry"+det.split(":")[0]+".place_forget()")
    file = open(filename, "w")
    file.writelines(list_of_lines)
    file.close()
    list_resource_details.destroy()
    
    
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()

# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()

def delete_login_success():
    
    login_success_screen.destroy()
    login_screen.destroy()
    main_screen.destroy()

def delete_password_not_recognised():
    password_not_recog_screen.destroy()

def delete_user_not_found_screen():
    user_not_found_screen.destroy()

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("500x500")
    main_screen.title("Admin Panel")
    Label(text="Hello Admin!", bg="blue", width="300", height="2",fg="white", font=("Calibri", 17)).pack()
    Label(text="").pack()
    Button(text=" Patient Register", height="2", width="30", command=register).pack()
    Label(text="").pack()
    Button(text="Patient Login", height="2", width="30", command = login).pack()
    Label(text="").pack()
    Button(text="Patient Details", height="2", width="30", command = patients_details).pack()
    Label(text="").pack()
    Button(text="Resource Dashboard", height="2", width="30", command = display_resource).pack()
    Label(text="").pack()
    Button(text="Remove All Patients' Database", height="2", width="30", command = patients_removeall).pack()

    main_screen.mainloop()
    