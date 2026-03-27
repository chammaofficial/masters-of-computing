#
# numbersbar.py: Read ten numbers give sum, min, max & mean and plot a bar chart
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

plt.title('Numbers Bar Chart')
plt.xlabel('Index')
plt.ylabel('Number')
plt.bar([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], numarray, 0.9, color='purple')
plt.savefig('plot_numbersbar.png')
