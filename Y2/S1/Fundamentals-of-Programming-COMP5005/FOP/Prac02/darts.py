#
# darts.py - Calculating PIE with darts
#

import random

num_trials = 10000000
ncirc = 0

r = 1.0 # radius of circle
r2 = r*r

for i in range(num_trials):
    x = random.random()
    y = random.random()
    if ((x*x + y*y) <= r2): # if x,y pos inside circle
        ncirc += 1 # increase circle count

pi = 4.0 * ncirc / num_trials
print("\nFor ", num_trials, " trials, pi = ", pi)
