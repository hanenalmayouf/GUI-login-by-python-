from tkinter import *
from functools import partial
def validateLogin(username, password):
	print("username entered :", username.get())
	print("password entered :", password.get())
	return
# call function when we click on entry box
def click1(*args):
    usernameEntry.delete(0, 'end')

def click2(*args):
    passwordEntry.delete(0, 'end')

#window
tkWindow = Tk()
tkWindow.geometry('270x220')
tkWindow.title('Login Form')
#tkWindow.configure(bg='white')

#username label and text entry box
title=Label(tkWindow,text="Sign up",font=('arial', 20, 'bold')).pack()
usernameLabel = Label(tkWindow, text="Email address").place(x=10,y=40)
username = StringVar()
usernameEntry = Entry(tkWindow,textvariable=username,width=40)
usernameEntry.place(x=10,y=60)
usernameEntry.insert(0, 'Enter email')


#password label and password entry box
passwordLabel = Label(tkWindow,text="Password").place(x=10,y=80)
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*',width=40)
passwordEntry.place(x=10,y=100)
#passwordEntry = Entry(tkWindow,textvariable=password,width=40)
#passwordEntry.insert(0, 'Enter password')

var1 = IntVar()
chk = Checkbutton(tkWindow, text="Remember me", variable=var1).place(x=10,y=120)
usernameEntry.bind("<Button-1>", click1)
passwordEntry.bind("<Button-1>", click2)
validateLogin = partial(validateLogin, username, password)

#login button
loginButton = Button(tkWindow, text="Login",width=33,bg='blue',fg='white', command=validateLogin).place(x=10,y=150)
#forget password
forgetLabel = Label(tkWindow, text="Forget").place(x=150,y=180)
passwordLabel = Label(tkWindow, text="Password?",fg='blue').place(x=190,y=180)
tkWindow.mainloop()