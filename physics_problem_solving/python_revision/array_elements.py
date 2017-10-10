import numpy as np

x_i = np.arange(90,100,1)
y_i = x_i.copy()

# Approach 1 - seeing if values are divisible by 2
for i in range(np.size(x_i)):
    if np.mod(x_i[i],2) == 0:
        x_i[i] = x_i[i] * (-1)

# Approach 2 - masking an array
ieven = np.arange(0,10,2)
y_i[ieven] = -1.0 * y_i[ieven]

print ieven

print x_i
print y_i
