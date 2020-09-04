# class to modify and create accounts
# 9/1/2020

import os

class Login(): #Logs in users who already have an account

    def __init__(self, username, password):
        self.user = username
        self.password = password

    def CheckLogin(self): #Checks if login information is correct
        userdata = open(os.path.join(os.getcwd(), 'User_Data.txt'))
        for line in userdata:
            if self.user == (line.split(':'))[0]: #Checks if username is correct
                if self.password == (line.split(':'))[1]: #Checks if password is also correct
                    userdata.close()
                    return True #Returns true if username and password are correct
        userdata.close()
        return False #Returns false if username or password are incorrect


class SignUp(): #Signs up new users

    def __init__(self, fname, lname, username, password):
        self.username = username
        self.password = password
        self.fname = fname
        self.lname = lname

    def CreateLogin(self): #Creates data entries for new users
        userdata = open(os.path.join(os.getcwd(), 'User_Data.txt'), 'a')
        userdata.write('\n' + self.username + ':' + self.password) #Adds username and paassword to User_Data.txt
        userdata.close()
        newuser = open(os.path.join(os.getcwd(), 'Users\\' + self.username + '.txt'), 'w+') #Creates new txt file for users budget information
        # input starting data for each new user
        newuser.close()

    def CheckSignUp(self): #Checks if new users username is already used
        userdata = open(os.path.join(os.getcwd(), 'User_Data.txt'), 'a')
        for line in userdata:
            if self.username == (line.split(':'))[0]:
                userdata.close()
                return False #Returns false if username is taken
        userdata.close()
        self.CreateLogin()
        return True #Returns true if username is available