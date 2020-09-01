# create gui
# 9/1/2020

from tkinter import *


class Application(Frame):

    """ A GUI application"""
    def __init__(self, master):
        """ Initialize the Frame """
        super(Application, self).__init__(master)
        self.grid()
        self.create_login()

    def create_login(self):
        """ Create login page """
        # login title
        self.login_lbl = Label(self, text="Login")
        self.login_lbl.grid(row=0, column=0, columnspan=1, sticky=W)