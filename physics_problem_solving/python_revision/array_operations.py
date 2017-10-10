import numpy as np

x = np.array([1.,2.,3.])
y = np.array([2.,2.,1.])
z = np.array([[1.,2.,1.], [0.,3.,4.], [8.,7.,9.]])

dot = np.dot(x,y)
cross = np.cross(x,y)

dot_2 = np.dot(z,x)

a = x * y # each element is multiplied together, it's not dotted or crossed as in matrix maths

