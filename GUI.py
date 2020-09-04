# create gui
# 9/1/2020

from tkinter import *
from Account_Management import *
import tkinter.messagebox


class GUI(Frame):

    def __init__(self, master):
        """ Initialize the frame. """
        super(GUI, self).__init__(master)
        self.grid()
        self.create_main()

    def submit_login(self):
        username = self.username_ent.get()
        password = self.password_ent.get()

        if Login(username, password).CheckLogin():
            self.quit()
        else:
            self.username_ent.delete(0, END)
            self.password_ent.delete(0, END)
            tkinter.messagebox.showinfo('ERROR :P', 'WRONG')

    def create_main(self):

        # test for main page. will go more indepth later
        self.welcome_lbl = Label(self, text="Welcome")
        # use grid after first test
        self.welcome_lbl.pack()

        # button to open login page
        self.login_bttn = Button(self, text="Login", command=self.launch_login_window)
        self.login_bttn.pack()

    def launch_login_window(self):
        login = Toplevel()
        login.title("Login")
        login.geometry("200x300")

        # login title
        self.login_lbl = Label(login, text="Login")
        self.login_lbl.grid(row=0, column=1, columnspan=1, sticky=W)

        # username title
        self.username_lbl = Label(login, text="Username: ")
        self.username_lbl.grid(row=1, column=0, columnspan=1, sticky=W)

        # username entry box
        self.username_ent = Entry(login)
        self.username_ent.grid(row=1, column=1, columnspan=2, sticky=W)

        # password title
        self.password_lbl = Label(login, text="Password: ")
        self.password_lbl.grid(row=2, column=0, columnspan=1, sticky=W)

        # password entry box
        self.password_ent = Entry(login)
        self.password_ent.grid(row=2, column=1, columnspan=2, sticky=W)

        # submit button
        self.submit_bttn = Button(login, text="Submit", command=self.submit_login)
        self.submit_bttn.grid(row=3, column=1, columnspan=1, sticky=W)

        # sign-up button
        self.signup_btn = Button(login, text="Sign-Up", command=self.launch_signup_window)
        self.signup_btn.grid(row=3, column=2, columnspan=2, sticky=W)

    def launch_signup_window(self):
        signup = Toplevel()
        signup.title("Signup")

        # sign-up title
        signup.login_lbl = Label(signup, text="Sign Up")
        signup.login_lbl.grid(row=0, column=1, columnspan=1, sticky=W)

        # First name label
        signup.fname_lbl = Label(signup, text="First Name: ")
        signup.fname_lbl.grid(row=1, column=0, columnspan=1, sticky=W)

        # First name entry
        signup.fname_ent = Entry(signup)
        signup.fname_ent.grid(row=1, column=1, columnspan=2, sticky=W)

        # Last name label
        signup.lname_lbl = Label(signup, text="Last Name: ")
        signup.lname_lbl.grid(row=2, column=0, columnspan=1, sticky=W)

        # Last name entry
        signup.lname_ent = Entry(signup)
        signup.lname_ent.grid(row=2, column=1, columnspan=2, sticky=W)

        # username label
        signup.user_lbl = Label(signup, text="Username: ")
        signup.user_lbl.grid(row=3, column=0, columnspan=1, sticky=W)

        # username entry
        signup.user_ent = Entry(signup)
        signup.user_ent.grid(row=3, column=1, columnspan=2, sticky=W)

        # password label
        signup.password_lbl = Label(signup, text="Password: ")
        signup.password_lbl.grid(row=4, column=0, columnspan=1, sticky=W)

        # password entry
        signup.password_ent = Entry(signup)
        signup.password_ent.grid(row=4, column=1, columnspan=2, sticky=W)

        # sign-up button
        signup.signup_btn = Button(signup, text="Sign Up")  # add command to button
        signup.signup_btn.grid(row=5, column=1, columnspan=1, sticky=W)