# create gui
# 9/1/2020

from tkinter import *
from Account_Management import *


class Application(Frame):

    """ A GUI application"""
    def __init__(self, master):
        """ Initialize the Frame """
        super(Application, self).__init__(master)
        self.grid()
        self.create_login()

    def submit(self):
        username = self.username_ent.get()
        password = self.password_ent.get()
        Login(username, password)

    def signup(self):
        print("signup")
        return "signup"

    def create_login(self):
        """ Create login page """
        # login title
        self.login_lbl = Label(self, text="Login")
        self.login_lbl.grid(row=0, column=1, columnspan=1, sticky=W)

        # username title
        self.username_lbl = Label(self, text="Username: ")
        self.username_lbl.grid(row=1, column=0, columnspan=1, sticky=W)

        # username entry box
        self.username_ent = Entry(self)
        self.username_ent.grid(row=1, column=1, columnspan=2, sticky=W)

        # password title
        self.password_lbl = Label(self, text="Password: ")
        self.password_lbl.grid(row=2, column=0, columnspan=1, sticky=W)

        # password entry box
        self.password_ent = Entry(self)
        self.password_ent.grid(row=2, column=1, columnspan=2, sticky=W)

        # submit button
        self.submit_bttn = Button(self, text="Submit", command=self.submit)
        self.submit_bttn.grid(row=3, column=1, columnspan=1, sticky=W)

        # sign-up button
        self.signup_bttn = Button(self, text="Sign-Up", command=self.signup)
        self.signup_bttn.grid(row=3, column=2, columnspan=2, sticky=W)

    # def create_signup(self):

