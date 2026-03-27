#
# numbersarray.py: Read ten numbers give sum, min, max & mean 
#


import numpy as np
import matplotlib.pyplot as plt

numarray = np.zeros(10)   # create an empty 10 element array 

print('Enter ten numbers...')

for i in range(len(numarray)):
    print('Enter a number (', i, ')...')
    numarray[i] = int(input())
    
print('Total is ', numarray.sum())
print('Min is ', numarray.min())
print('Max is ', numarray.max())
print('Avg is ', numarray.mean())

plt.plot(numarray)
plt.ylabel('Some Numbers')
plt.savefig('plot_numbersarray.png')
