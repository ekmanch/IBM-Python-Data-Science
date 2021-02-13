#################################################
# Numpy 1D Array Quick Practice Lab
#################################################

print("QUICK PRACTICE LAB")

# Question 1
# Cast the following list to a numpy array:

import numpy as np
a=[1,2,3,4,5]

# Answer:

np_a = np.array(a)
print(np_a)

# Question 2
# 1) Type using the function type

print(type(np_a))

# Question 3
# 2) The shape of the array

print(np_a.shape)

# Question 4
# 3) The type of data in the array

print(np_a.dtype)

# Question 5
# 4) Find the mean of the array

print(np_a.mean())

print("QUIZ")

# Question 1
# What is the result of the following operation
# np.array([1,-1])*np.array([1,1])
# Prediction: [1,-1]

print(np.array([1,-1])*np.array([1,1]))

# Question 2
# What is the result of the following operation
# np.dot(np.array([1,-1]),np.array([1,1]))
# Prediction: 0

print(np.dot(np.array([1,-1]),np.array([1,1])))