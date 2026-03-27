#
# bucket2.py - bucket list builder
#

print('\nBUCKET LIST BUILDER\n')
bucket = []
choice = input('Enter selection: e(X)it, (A)dd, (D)elete, (L)ist...').upper()
choice = choice.upper()
while choice[0] != 'X':
    if choice[0] == 'A':
        print('Enter list item... ')
        newitem = input()
        bucket.append(newitem)
    elif choice[0] == 'L':
        for item in bucket:
            print(item)
    elif choice[0] == 'D':
        index = 1
        for item in bucket:
            print(f'{index}. {item}')
            index = index + 1
        delitem = int(input('Enter a item number to delete: '))
        del bucket[delitem - 1]
    else:
        print('Invalid selection.')
    choice = input('Enter selection: e(X)it, (A)dd, (D)elete, (L)ist..').upper()
print('\nGOODBYE!\n')
