# create gui
# 9/1/2020

from tkinter import *
from Account_Management import *


class LoginGUI(Frame):

    """ Login GUI """
    def __init__(self, master):
        """ Initialize the Frame """
        super(LoginGUI, self).__init__(master)
        self.grid()
        self.create()

    def submit(self):
        username = self.username_ent.get()
        password = self.password_ent.get()
        Login(username, password)
        self.quit()

    def signup(self):
        root = Tk()
        root.title("Budget Manager")
        root.geometry("200x150")
        app = SignupGUI(root)
        root.mainloop()

    def create(self):
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
        self.signup_btn = Button(self, text="Sign-Up", command=self.signup)
        self.signup_btn.grid(row=3, column=2, columnspan=2, sticky=W)


class SignupGUI(Frame):

    """ Signup GUI """
    def __init__(self, master):
        """ Initialize the Frame """
        super(SignupGUI, self).__init__(master)
        self.grid()
        self.create()

    def Signup(self):
        fname = self.fname_ent.get()
        lname = self.lname_ent.get()
        username = self.user_ent.get()
        password = self.password_ent.get()
        SignUp(fname, lname, username, password)

    def create(self):
        """ Create signup page """
        # sign-up title
        self.login_lbl = Label(self, text="Sign Up")
        self.login_lbl.grid(row=0, column=1, columnspan=1, sticky=W)

        # First name label
        self.fname_lbl = Label(self, text="First Name: ")
        self.fname_lbl.grid(row=1, column=0, columnspan=1, sticky=W)

        # First name entry
        self.fname_ent = Entry(self)
        self.fname_ent.grid(row=1, column=1, columnspan=2, sticky=W)

        # Last name label
        self.lname_lbl = Label(self, text="Last Name: ")
        self.lname_lbl.grid(row=2, column=0, columnspan=1, sticky=W)

        # Last name entry
        self.lname_ent = Entry(self)
        self.lname_ent.grid(row=2, column=1, columnspan=2, sticky=W)

        # username label
        self.user_lbl = Label(self, text="Username: ")
        self.user_lbl.grid(row=3, column=0, columnspan=1, sticky=W)

        # username entry
        self.user_ent = Entry(self)
        self.user_ent.grid(row=3, column=1, columnspan=2, sticky=W)

        # password label
        self.password_lbl = Label(self, text="Password: ")
        self.password_lbl.grid(row=4, column=0, columnspan=1, sticky=W)

        # password entry
        self.password_ent = Entry(self)
        self.password_ent.grid(row=4, column=1, columnspan=2, sticky=W)

        # sign-up button
        self.signup_btn = Button(self, text="Sign Up", command=self.Signup)
        self.signup_btn.grid(row=5, column=1, columnspan=1, sticky=W)
