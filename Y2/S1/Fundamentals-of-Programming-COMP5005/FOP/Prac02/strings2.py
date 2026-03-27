#
# strings2.py: Extended Version of Strings1
#

instring = input('Enter a string... ')
instring = instring.upper()
instring = instring * 2


# *** add (2) upper and (3) duplicating code here

#forwarded with a while loop
print('Forwared string is : ', end='')
index = 0
while index < len(instring):
    print(instring[index], end='')
    index = index + 2
print()

# forwarded with a for-range loop
print('Forwarded string is : ', end='')
for index in range(0, len(instring), 2):
    print(instring[index], end='')
print()

# forwarded with slicing
print('Forwarded string is :', instring[::2])

#forwarded with a while loop
print('Forwared string is : ', end='')
index = 1
while index < len(instring):
    print(instring[index], end='')
    index = index + 2
print()

# forwarded with a for-range loop
print('Forwarded string is : ', end='')
for index in range(1, len(instring), 2):
    print(instring[index], end='')
print()

# forwarded with slicing
print('Forwarded string is :', instring[1::2])

