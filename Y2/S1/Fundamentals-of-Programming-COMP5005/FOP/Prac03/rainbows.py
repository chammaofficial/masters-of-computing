#
# rainbows.py - Simulation of rainbow with arrays and matplotlib
#

import math
import numpy as np
import matplotlib.pyplot as plt
res = 4
for r in range(10,3,-1):
    size = r * res * 2 + 1
    xarray = np.zeros(size)
    arcarray = np.zeros(size)
    if r == 10:
        colour = "red" 
    elif r == 9:
        colour = "orange" 
    elif r == 8:
        colour = "yellow" 
    elif r == 7:
        colour = "green" 
    elif r == 6:
        colour = "blue" 
    elif r == 5:
        colour = "indigo" 
    else:
        colour = "violet" 
    for i in range(-res * r, res * r + 1):
        xarray[i] = i
        print(r, i)
        arcarray[i] = math.sqrt((res * r)**2 - i**2)
    plt.plot(xarray, arcarray, color=colour, marker="o")
plt.title("Many Curves - arrays")
plt.savefig('rainbow.png')
