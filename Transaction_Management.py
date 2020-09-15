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
            transactions.write(date + '|' + reason + '|' + amount + '|\n')
            transactions.close()
            return True

    def TransactionHistory(self):
        history, dates, year, month, day = [], [], [], [], []
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

    def MonthlyTransactionHistory(self, month, year):
        history, dates = [], []
        transactions = open(os.path.join(os.getcwd(), 'Users\\' + self.username + '\\Transactions.txt'))
        for line in transactions:
            if month == line.split('|')[0].split('-')[0] and year == line.split('|')[0].split('-')[2]:
                history.append(line.split('|')[:3])
                dates.append(int(year + month))
        transactions.close()
        history = [history for _, history in sorted((zip(dates, history)))]
        return history

    def TransactionsMonths(self):
        transactions = open(os.path.join(os.getcwd(), 'Users\\' + self.username + '\\Transactions.txt'))
        dates = []
        sort = []
        for line in transactions:
            dates.append([line.split('|')[0].split('-')[0], line.split('|')[0].split('-')[2]])
            sort.append(int(line.split('|')[0].split('-')[2] + line.split('|')[0].split('-')[0]))
        dates = [dates for _, dates in sorted((zip(sort, dates)))]
        return [ele for ele in reversed(set(map(tuple, dates)))]
