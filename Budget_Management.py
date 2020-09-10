# manage users budget
# 9-8-2020

# create list of budget items
# compare budget to true spending

import os

class Budget():

    def __init__(self, username):
        self.username = username

    def add_budget_item(self, item):
        itemfile = open(os.path.join(os.getcwd(), 'Users\\' + self.username + '\\BudgetItems.txt'), 'a')
        itemfile.write(item + ', ')
        itemfile.close()

    def get_budget_items(self):
        itemfile = str(open(os.path.join(os.getcwd(), 'Users\\' + self.username + '\\BudgetItems.txt'), 'r'))
        print(itemfile.split(', '))
        return itemfile.split(', ')