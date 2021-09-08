from tkinter import*
import math,random,os
from tkinter import messagebox
import time
import barcode
import os
import webbrowser
import tkinter as tk
import datetime
import tkinter.messagebox
from register import *
from _tkinter import TclError
from admin_main import *
#
def login():
    #getting form data
    uname=username.get()
    pwd=password.get()
    #applying empty validation
    if uname=="admin" and pwd=="123":
        global login_success_screen
        login_success_screen = Toplevel(login_screen)
        login_success_screen.geometry("150x100")
        Label(login_success_screen, text="Login Success").pack()
        Button(login_success_screen, text="OK", command=delete_login_success).pack()
    elif (uname=="" and pwd==""):
        root = Tk()
        
        def message():
            L['text'] = ''

        def delay():
            L['text'] = ''
        root.after(1000, message)
        root.after(1000, root.destroy)
        L = Label(root, text="No details entered")
        L.pack()
    elif (uname=="" or pwd==""):
        root = Tk()
        
        def message():
            L['text'] = ''

        def delay():
            L['text'] = ''
        root.after(1000, message)
        root.after(1000, root.destroy)
        L = Label(root, text="Insuffucient details")
        L.pack()
    elif (uname=="admin"):
        root = Tk()
        
        def message():
            L['text'] = ''

        def delay():
            L['text'] = ''
        root.after(1000, message)
        root.after(1000, root.destroy)
        L = Label(root, text="Wrong password")
        L.pack()    
    else:
        root = Tk()
        
        def message():
            L['text'] = ''

        def delay():
            L['text'] = ''
        root.after(1000, message)
        root.after(1000, root.destroy)
        L = Label(root, text="Wrong username and password")
        L.pack()
       
def delete_login_success():
    login_success_screen.destroy()
    login_screen.destroy()
    main_account_screen()
#Admin login screen interface
def Loginform():
    global login_screen
    login_screen = Tk()
    #Setting title of screen
    login_screen.title("Admin Login")
    #setting height and width of screen
    login_screen.geometry("300x250")
    #declaring variable
    global  message
    global username
    global password
    username = StringVar()
    password = StringVar()
    message=StringVar()
    #Creating layout of login form
    Label(login_screen,width="300", text="Please enter details below", bg="cyan",fg="black").pack()
    #Username Label
    Label(login_screen, text="Username * ").place(x=20,y=40)
    #Username textbox
    Entry(login_screen, textvariable=username).place(x=90,y=42)
    #Password Label
    Label(login_screen, text="Password * ").place(x=20,y=80)
    #Password textbox
    Entry(login_screen, textvariable=password ,show="*").place(x=90,y=82)
    #Label for displaying login status[success/failed]
    Label(login_screen, text="",textvariable=message).place(x=95,y=100)
    #Login button
    Button(login_screen, text="Login", width=10, height=1, bg="magenta",fg="white",command=login).place(x=105,y=130)
    login_screen.mainloop()
#calling function Loginform
if __name__ == "__main__":
    Loginform()
