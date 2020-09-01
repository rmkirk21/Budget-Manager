# class to modify and create accounts
# 9/1/2020

import os


class Login():
    """ Log in """

    def __init__(self, username, password):

        self.user = username
        self.password = password

    def CheckLogin(self):
        userdata = open(os.path.join(os.getcwd(), 'User_Data.txt'))
        for line in open(os.path.join(os.getcwd(), 'User_Data.txt')):
            if self.user == (line.split(':'))[0]:
                if self.password == (line.split(':'))[1]:
                    userdata.close()
                    return True
                else:
                    userdata.close()
                    return False
            else:
                userdata.close()
                return False


class SignUp():

    def __init__(self, fname, lname, username, password):
        self.username = username
        self.password = password
        self.fname = fname
        self.lname = lname

    def CreateLogin(self):
        userdata = open(os.path.join(os.getcwd(), 'User_Data.txt', 'a'))
        userdata.write(self.username + ':' + self.password)
        userdata.close()

    def CheckSignUp(self):
        for line in open(os.path.join(os.getcwd(), 'User_Data.txt')):
            if self.username == (line.split(':'))[0]:
                return False
            else:
                self.CreateLogin()
                return True
