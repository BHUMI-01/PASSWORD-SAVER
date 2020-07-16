from tkinter import *
from functools import partial

def validateLogin(username, password,email):
	print("username entered :", username.get())
	print("password entered :", password.get())
	print("email entered :", email.get())
	return

#window
tkWindow = Tk()  
tkWindow.geometry('400x150')  
tkWindow.title('Tkinter Login Form - pythonexamples.org')

#username label and text entry box
usernameLabel = Label(tkWindow, text="User Name").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)  

#password label and password entry box
passwordLabel = Label(tkWindow,text="Password").grid(row=1, column=0)  
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)  


#email label and email entry box
emailLabel = Label(tkWindow,text="Email").grid(row=2, column=0)  
email = StringVar()
emailEntry = Entry(tkWindow, textvariable=email, show='*').grid(row=2, column=1)  


validateLogin = partial(validateLogin, username, password,email)

#login button
loginButton = Button(tkWindow, text="Login", command=validateLogin).grid(row=5, column=0)  

tkWindow.mainloop()
