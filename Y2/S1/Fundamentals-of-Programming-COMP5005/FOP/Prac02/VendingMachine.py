#
# VendingMachine.py - Simulate Vending Machine Transactions.
#

from tabulate import tabulate

# Defining Colors and LINE_UP and LINE_CLEAR

LINE_UP = '\033[1A'
LINE_CLEAR = '\x1b[2K'

BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
UNDERLINE = '\033[4m'
BOLD = '\033[1m'
RESET = '\033[0m'

# Defining Item List

treats = [[1, 'Choco Pie', 1.00, 5],
          [2, 'Hello Panda', 0.50, 10],
          [3, 'Fortune Cookie', 0.30, 10],
          [4, 'Fig Roll', 0.30, 10],
          [5, 'Maliban Orange Cream', 0.30, 10],
          [6, 'Maliban Custard Cream', 0.30, 10],
          [7, 'Maliban Chocolate Cream' ,0.30, 10],
          [8, 'Eggless Cake', 0.80, 5],
          [9, 'Wagon Wheel', 1.50, 1]]


print(BOLD+'Welcome to the snack vending machine!\n\n'+RESET)
print('The slots are loaded with delicious treats!\n')
needtreat = input(BOLD+'Would you like a treat? (Y/N): '+RESET)
while needtreat == 'Y':
    print('Which treat would you like? ')
    print()
    print(tabulate(treats, headers=["ID", "Name", "Price", "Stock"], tablefmt='fancy_grid'))
    print()
    choice = int(input('Enter your selection: '))
    
    if choice > len(treats):
        print(RED+'\nInvalid selection. Please try again.'+RESET)
    else:
        selected_treat = treats[choice - 1]
        treat_name = selected_treat[1]
        treat_cost = selected_treat[2]
        treat_stock = selected_treat[3]
        
        if treat_stock > 0: 
            treats[choice - 1][3] = treat_stock - 1
            print(GREEN + 'Here is your ' + treat_name + ' Enjoy!' + RESET)
            print(GREEN + 'That will be: ' + str(treat_cost) + '$\n' + RESET)
            print('\nGlad to be of service!')
        else:
            print(RED + 'Oh dear! we are all out of ' + treat_name + '\n' + RESET)

    needtreat = input(BOLD+'Would you like a  treat? (Y/N)'+RESET)

