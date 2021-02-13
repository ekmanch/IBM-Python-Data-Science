#################################################
# Numpy 2D Arrays Quick Practice Lab
#################################################

# You will use the numpy array  A for the following
import numpy as np
A=np.array([[11,12],[21,22],[31,32]])

# Question 1:
# 1) Type using the function type

print(type(A))

# Question 2
# 2) The shape of the array

print(A.shape)

# Question 3
# 3) The type of data in the array

print(A.dtype)

# Question 4
# 4) Find the second row of the numpy array A:

print(A[1,:])

# You will use the following numpy arrays for the next questions:
A=np.array([[11,12],[21,22]])
B=np.array([[1, 0],[0,1]])

# Question 1
# 1) Multiply array  A  and B

print(A*B)

# Question 2
# 2) Perform matrix multiplication on array  A and  B (order will not matter in this case)

print(np.dot(A,B))