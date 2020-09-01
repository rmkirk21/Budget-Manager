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
        return "submit"

    def signup(self):
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
        self.submit_bttn = Button(self)
        self.submit_bttn["text"] = "Submit"
        self.submit_bttn["command"] = self.submit()
        self.submit_bttn.grid(row=3, column=1, columnspan=1, sticky=W)

        # sign-up button
        self.signup_bttn = Button(self)
        self.signup_bttn["text"] = "Sign Up"
        self.signup_bttn["command"] = self.signup()
        self.signup_bttn.grid(row=3, column=2, columnspan=2, sticky=W)