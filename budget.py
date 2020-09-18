import math


class Category:
    get_withdrawl = 0

    def __str__(self):
        title = f"{self.categories:*^30}\n"
        item = ''
        total = 0
        for value in self.ledger:
            item += f"{value['description'][0:23]:23}" + \
                    f"{value['amount']:>7.2f}" + '\n'
            total += value['amount']

        output = title + item + 'Total: ' + str(total)
        return output

    def __init__(self, categories):
        self.ledger = list()
        self.categories = categories

    def deposit(self, amount, description=''):
        self.amount = amount
        self.description = description
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=''):
        self.amount = amount
        self.description = description
        if self.check_funds(self.amount) is True:
            self.ledger.append({'amount': -amount, 'description': description})
            self.get_withdrawl += amount
            return True
        else:
            return False

    def get_balance(self):
        self.a = 0
        for value in self.ledger:
            self.a += value['amount']
        return self.a

    def transfer(self, amount, Category):
        self.description = ''
        self.amount = amount
        self.description = 'Transfer to' + ' ' + Category.categories
        if self.check_funds(self.amount) is True:
            self.ledger.append({'amount': -self.amount, 'description': self.description})
            Category.description = ''
            Category.amount = amount
            Category.description = 'Transfer from' + ' ' + self.categories
            Category.ledger.append({'amount': Category.amount, 'description': Category.description})
            return True
        else:
            return False

    def check_funds(self, amount):
        self.a = 0
        for value in self.ledger:
            self.a += value['amount']
        if self.a - amount >= 0:
            return True
        else:
            return False


def create_spend_chart(categories):
    columns = []
    total = 0
    for category in categories:
        categorySpend = 0
        for row in category.ledger:
            if row['amount'] < 0:
                categorySpend += (row['amount'] * -1)
                total += (row['amount'] * -1)
        columns.append({'name': category.categories, 'spent': categorySpend})

    i = 0
    while i < len(columns):
        columns[i]['percentage'] = math.floor((columns[i]['spent'] / total) * 10) * 10
        # print(columns[i]['percentage'])
        i += 1

    res = "Percentage spent by category\n"
    y = 100
    while y >= 0:
        part = str(y) + "| "
        part = part.rjust(5, ' ')
        res += part
        z = 0
        yData = ''
        while z < len(columns):
            if columns[z]['percentage'] >= y:
                yData = 'o  '
            else:
                yData = '   '
            res += yData
            z += 1
        res += '\n'
        if y == 0:
            res += '    -'
            for x in columns:
                res += '---'
            res += '\n'
        y -= 10

    longestName = 0
    for x in columns:
        if len(x['name']) > longestName:
            longestName = len(x['name'])

    ln = 0
    while ln < longestName:
        xLabel = '     '
        for x in columns:
            if ln < len(x['name']):
                part = x['name'][ln] + '  '
            else:
                part = '   '
            xLabel += part
        res += xLabel
        # test fails if an extra line break at the end...
        if ln < longestName - 1:
            res += '\n'
        ln += 1

    # print (res)
    return res