import numpy as np

x = np.array([7.,9.,2.,3.,20.])
swapped = []

for i in range(len(x)):
    for j in range(len(x)-1):
        if (x[j] > x[j+1]):
            swapped.append("Swap")
            tmp = x[j]
            x[j] = x[j+1]
            x[j+1] = tmp
        else:
            swapped.append("No swap")
           
print x
print swapped

# swap one of the for loops for a while loop?
