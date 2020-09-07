# create gui
# 9/1/2020

from tkinter import *
from Account_Management import *
import tkinter.messagebox


class GUI(Frame):

    def __init__(self, master):
        """ Initialize the frame. """
        super(GUI, self).__init__(master)
        self.grid()
        self.create_main()

    def submit_login(self):
        username = self.username_ent.get()
        password = self.password_ent.get()

        if Login(username, password).CheckLogin():
            self.quit()
        else:
            self.username_ent.delete(0, END)
            self.password_ent.delete(0, END)
            tkinter.messagebox.showinfo('ERROR :P', 'WRONG')

    def submit_transaction(self):
        date = self.transactionDate_ent.get()
        reason = self.transactionReason_ent.get()
        amount = self.transactionAmount_ent.get()

        # check if entry boxes are empty and act accordingly
        if date == "" or reason == "" or amount == "":
            tkinter.messagebox.showinfo('ERROR :P', 'You have failed to provide enough information. \nPlease try again :)')

    def signup(self):
        fname = self.fname_ent.get()
        lname = self.lname_ent.get()
        username = self.user_ent.get()
        password = self.password_ent.get()

        if SignUp(fname, lname, username, password).CheckSignUp():
            self.quit()
            tkinter.messagebox.showinfo('YAY', 'New User Created')
        else:
            tkinter.messagebox.showinfo('ERROR :P', 'Already Exists')

    def create_main(self):

        # test for main page. will go more indepth later
        self.welcome_lbl = Label(self, text="Welcome")
        # use grid after first test
        self.welcome_lbl.pack()

        # button to open login page
        self.login_bttn = Button(self, text="Login", command=self.launch_login_window)
        self.login_bttn.pack()

        # display last 10 transactions
        """ Make sure to change text to the transactions """
        self. transaction_text = Message(self, width=35, bg="#E0E0E0", text="Hello \n hi")
        self.transaction_text.pack()

        # button to display all transactions
        self.viewTransactions_bttn = Button(self, text="View All Transactions", command=self.launch_transactions_window)
        self.viewTransactions_bttn.pack()

        # button to add a transaction
        self.addTransaction_bttn = Button(self, text="Add a Transaction", command=self.launch_addTransaction_window)
        self.addTransaction_bttn.pack()

    def launch_login_window(self):
        login = Toplevel()
        login.title("Login")
        login.geometry("200x300")

        # login title
        login_lbl = Label(login, text="Login")
        login_lbl.grid(row=0, column=1, columnspan=1, sticky=W)

        # username title
        username_lbl = Label(login, text="Username: ")
        username_lbl.grid(row=1, column=0, columnspan=1, sticky=W)

        # username entry box
        self.username_ent = Entry(login)
        self.username_ent.grid(row=1, column=1, columnspan=2, sticky=W)

        # password title
        password_lbl = Label(login, text="Password: ")
        password_lbl.grid(row=2, column=0, columnspan=1, sticky=W)

        # password entry box
        self.password_ent = Entry(login)
        self.password_ent.grid(row=2, column=1, columnspan=2, sticky=W)

        # submit button
        self.submit_bttn = Button(login, text="Submit", command=self.submit_login)
        self.submit_bttn.grid(row=3, column=1, columnspan=1, sticky=W)

        # sign-up button
        self.signup_btn = Button(login, text="Sign-Up", command=self.launch_signup_window)
        self.signup_btn.grid(row=3, column=2, columnspan=2, sticky=W)

    def launch_signup_window(self):
        signup = Toplevel()
        signup.title("Signup")

        # sign-up title
        login_lbl = Label(signup, text="Sign Up")
        login_lbl.grid(row=0, column=1, columnspan=1, sticky=W)

        # First name label
        fname_lbl = Label(signup, text="First Name: ")
        fname_lbl.grid(row=1, column=0, columnspan=1, sticky=W)

        # First name entry
        self.fname_ent = Entry(signup)
        self.fname_ent.grid(row=1, column=1, columnspan=2, sticky=W)

        # Last name label
        lname_lbl = Label(signup, text="Last Name: ")
        lname_lbl.grid(row=2, column=0, columnspan=1, sticky=W)

        # Last name entry
        self.lname_ent = Entry(signup)
        self.lname_ent.grid(row=2, column=1, columnspan=2, sticky=W)

        # username label
        user_lbl = Label(signup, text="Username: ")
        user_lbl.grid(row=3, column=0, columnspan=1, sticky=W)

        # username entry
        self.user_ent = Entry(signup)
        self.user_ent.grid(row=3, column=1, columnspan=2, sticky=W)

        # password label
        password_lbl = Label(signup, text="Password: ")
        password_lbl.grid(row=4, column=0, columnspan=1, sticky=W)

        # password entry
        self.password_ent = Entry(signup)
        self.password_ent.grid(row=4, column=1, columnspan=2, sticky=W)

        # sign-up button
        signup_btn = Button(signup, text="Sign Up", command=self.signup)
        signup_btn.grid(row=5, column=1, columnspan=1, sticky=W)

    def launch_transactions_window(self):
        history = Toplevel()
        history.title("Transaction History")
        history.geometry("300x500")

        # create list box for transactions
        transaction_list = Listbox(history)
        transaction_list.pack(side=LEFT, fill=BOTH, expand=YES)

        # create scrollbar for list box
        transaction_scroll = Scrollbar(history)
        transaction_scroll.pack(side=RIGHT, fill=BOTH)

        for values in range(100):
            transaction_list.insert(END, values)

        transaction_list.config(yscrollcommand=transaction_scroll.set)
        transaction_scroll.config(command=transaction_list.yview)

    def launch_addTransaction_window(self):
        addTransaction = Toplevel()
        addTransaction.title("Add Transaction")
        addTransaction.geometry("200x300")

        # date of transaction label
        transactionDate_lbl = Label(addTransaction, text="Date of Transaction")
        transactionDate_lbl.pack()

        # date of transaction entry box
        self.transactionDate_ent = Entry(addTransaction)
        self.transactionDate_ent.pack()

        # reason for transaction label
        transactionReason_lbl = Label(addTransaction, text="Reason For Transaction")
        transactionReason_lbl.pack()

        # reason for transaction entry box
        """ May Change to a drop down menu later"""
        """ But entry box is easier than drop down for now"""

        self.transactionReason_ent = Entry(addTransaction)
        self.transactionReason_ent.pack()

        # amount of transaction label
        transactionAmount_lbl = Label(addTransaction, text="Amount of Transaction")
        transactionAmount_lbl.pack()

        # amount of transaction entry box
        self.transactionAmount_ent = Entry(addTransaction)
        self.transactionAmount_ent.pack()

        # submit transaction button
        submitTransaction_bttn = Button(addTransaction, text="Submit", command=self.submit_transaction)
        submitTransaction_bttn.pack()