# class to modify and create accounts
# 9/1/2020

import os


class Login():  # Logs in users who already have an account

    def __init__(self, username, password):
        self.user = username
        self.password = password

    def CheckLogin(self):  # Checks if login information is correct
        users = open(os.path.join(os.getcwd(), 'Users\\User_Data.txt'))
        for line in users:
            if self.user == (line.split('|'))[0]:  # Checks if username is correct
                if self.password == (line.split('|'))[1]:  # Checks if password is also correct
                    users.close()
                    return True  # Returns true if username and password are correct
        users.close()
        return False  # Returns false if username or password are incorrect


class SignUp():  # Signs up new users

    def __init__(self, fname, lname, username, password):
        self.username = username
        self.password = password
        self.fname = fname
        self.lname = lname

    def CreateLogin(self):  # Creates data entries for new users
        users = open(os.path.join(os.getcwd(), 'Users\\User_Data.txt'), 'a')
        users.write(self.username + '|' + self.password + '|' + self.fname + '|' + self.lname + '|\n')  # Adds username and password to User_Data.txt
        users.close()
        os.mkdir(os.getcwd() + '\\Users\\' + self.username)
        transactionfile = open(os.path.join(os.getcwd(), 'Users\\' + self.username + '\\Transactions.txt'), 'w+')
        itemfile = open(os.path.join(os.getcwd(), 'Users\\' + self.username + '\\BudgetItems.txt'), 'w+')
        categoryfile = open(os.path.join(os.getcwd(), 'Users\\' + self.username + '\\Categories.txt'), 'w+')
        transactionfile.close()
        itemfile.close()

    def CheckSignUp(self):  # Checks if new users username is already used
        if '|' in self.username or '|' in self.password:    # Username and password cannot contain a '|'
            return False
        userdata = open(os.path.join(os.getcwd(), 'Users\\User_Data.txt'))
        for line in userdata:
            if self.username.lower() == (line.split('|'))[0].lower():
                userdata.close()
                return False  # Returns false if username is taken
        userdata.close()
        self.CreateLogin()  # Creates login if username is available
        return True