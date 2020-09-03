# create gui
# 9/1/2020

from tkinter import *
from Account_Management import *
import tkinter.messagebox


class GUI(Frame):

    """ Login GUI """
    def __init__(self, master):
        """ Initialize the Frame """
        super(GUI, self).__init__(master)
        self.grid()
        # call fuction to add widgets