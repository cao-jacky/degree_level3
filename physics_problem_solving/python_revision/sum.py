import numpy as np

x = np.arange(10,21,1) # Creating list of numbers from 10 to 20 in integer steps of 1
s = 0

for i in range(np.size(x)):
    s = s + np.log10(x[i])

print s

# "Rewriting"
y = np.log10(x)
s2 = np.sum(y)

print s2
