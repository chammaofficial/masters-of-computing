#
# num_convert.py: Read in number and convert to int and float
#
print('Enter a number...')
numstr = input()
print('Number =', numstr, ' Type : ', str(type(numstr)))
numint = int(numstr)
print('Number =', numint, ' Type : ', str(type(numint)))
numfloat = float(numstr)
print('Number =', numfloat, ' Type : ', str(type(numfloat)))
