# manage users budget
# 9-8-2020

# create list of budget items
# compare budget to true spending

import os


class Budget():

    def __init__(self, username):
        self.username = username

    def add_budget_item(self, item, amount):
        itemfile = open(os.path.join(os.getcwd(), 'Users\\' + self.username + '\\BudgetItems.txt'), 'r')
        itemdata = itemfile.readlines()
        itemfile.close()
        dup = ''
        for linenum in range(len(itemdata)):
            if itemdata[linenum].split('|')[0].lower() == item.lower():
                dup = linenum
        if dup != '':
            del itemdata[dup]
        itemfile = open(os.path.join(os.getcwd(), 'Users\\' + self.username + '\\BudgetItems.txt'), 'w+')
        for line in itemdata:
            itemfile.write(line)
        itemfile.close()
        itemfile = open(os.path.join(os.getcwd(), 'Users\\' + self.username + '\\BudgetItems.txt'), 'a')
        itemfile.write(item + '|' + amount + '|\n')
        itemfile.close()

    def get_budget_items(self):
        itemfile = open(os.path.join(os.getcwd(), 'Users\\' + self.username + '\\BudgetItems.txt'))
        items, cost = [], []
        for line in itemfile:
            items.append(line.split('|')[:2])
            cost.append(line.split('|')[1])
        itemfile.close()
        items = [items for _, items in sorted((zip(cost, items)))]
        return items
