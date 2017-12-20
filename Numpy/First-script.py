#!/usr/bin/env python
# -*-coding:utf-8-*-

import numpy as np

# Task 1
Z = np.zeros(10)
print("Array of size 10 full of zeros : ", Z, "\n")

# Task 2
Z = np.zeros(10)
Z[4] = 1
print("Array of size 10 full of zeros with 1 at the fifth position : ", Z, "\n")

# Task 3
Z = np.arange(10, 50)
print("Before reversing : ", Z, "\n")

# Task 4
Z = Z[::-1]
print("After reversing : ", Z, "\n")

# Task 5
Z = np.arange(9).reshape(3, 3)
print("Create a 3x3 matrix with values ranging from 0 to 8 : \n", Z, "\n")

# Task 6
nz = np.nonzero([1, 2, 0, 0, 4, 0])
print("Find << INDICES >> of non-zero elements :", nz, "\n")

# Task 7
Z = np.eye(3)
print("Create a 3x3x3 identity matrix : \n", Z, "\n")

# Task 8
Z = np.random.random((3, 3, 3))
print("Create 3x3x3 array with random values : \n", Z)
