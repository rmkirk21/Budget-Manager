# For calling error messages
# 09-08-2020

import tkinter.messagebox


class Errors:

    def wrong_login(self):
        tkinter.messagebox.showinfo('ERROR 2356', 'Username or Password incorrect')

    def not_enough_info_given(self):
        tkinter.messagebox.showinfo('ERROR 3568',
                                    'You have failed to provide enough information. \nPlease try again')

    def user_already_exists(self):
        tkinter.messagebox.showinfo('ERROR 6842', 'User Already Exists')


