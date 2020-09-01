# class to modify and create accounts
# 9/1/2020

import os


class Login():
    """ Log in """

    def __init__(self, username, password):

        self.user = username
        self.password = password

    def CheckLogin(self):
        for line in open(os.path.join(os.getcwd(), 'User_Data.txt')):
            if self.user == (line.split(':'))[0]:
                if self.password == (line.split(':'))[1]:
                    return True
                return False
            return False


class SignUp():

    def __init__(self, fname, lname, username, password):
        self.username = username
        self.password = password
        self.fname = fname
        self.lname = lname

    def CheckSignUp(self):
        for line in open(os.path.join(os.getcwd(), 'User_Data.txt')):
            if self.user == (line.split(':'))[0]:
                if self.password == (line.split(':'))[1]:
                    return False
                return False
