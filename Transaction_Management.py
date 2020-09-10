# manage transactions
# 9/6/2020

import os
import datetime

class Transaction():

    def __init__(self, username):
        self.username = username

    def AddTransaction(self, date, reason, amount):
        if '' == date or '' == reason or '' == amount:
            return False
        else:
            transactions = open(os.path.join(os.getcwd(), 'Users\\' + self.username + '\\Transactions.txt'), 'a')
            transactions.write('\n' + date + '|' + reason + '|' + amount + '|')
            transactions.close()
            return True

    def TransactionHistory(self):
        history = []
        dates, year, month, day = [], [], [], []
        transactions = open(os.path.join(os.getcwd(), 'Users\\' + self.username + '\\Transactions.txt'))
        for line in transactions:
            month = line.split('|')[0].split('-')[0]
            day = line.split('|')[0].split('-')[1]
            year = line.split('|')[0].split('-')[2]
            dates.append(int(year + month + day))
            history.append(line.split('|')[:3])
        transactions.close()
        history = [history for _, history in sorted((zip(dates, history)))]
        return [ele for ele in reversed(history)]
