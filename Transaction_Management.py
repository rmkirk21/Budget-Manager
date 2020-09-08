# manage transactions
# 9/6/2020

import os

class Transaction():

    def __init__(self, username):
        self.username = username

    def AddTransaction(self, date, reason, amount):
        transactions = open(os.path.join(os.getcwd(), 'Users\\' + self.username + '\\Transactions.txt'), 'a')
        transactions.write('\n' + date + '|' + reason + '|' + amount + '|')
        transactions.close()

    def TransactionHistory(self):
        history = []
        transactions = open(os.path.join(os.getcwd(), 'Users\\' + self.username + '\\Transactions.txt'))
        for line in transactions:
            history.append(line)
        print(history)
        return(history)