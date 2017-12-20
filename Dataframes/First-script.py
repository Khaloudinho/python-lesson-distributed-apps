#!/usr/bin/env python
# -*-coding:utf-8-*-

import numpy as np
import pandas as pd

# Task 1 : We can make dataframe from numpy arrays
ar = np.array([[1.1, 2, 3.3, 4], [2.7, 10, 5.4, 7], [5.3, 9, 1.5, 15]])
df = pd.DataFrame(ar, index = ['L1', 'L2', 'L3'], columns = ['C1', 'C2', 'C3', 'C4'])
print("-------------- Task 1 : \n")
print(df, "\n")

# Task 2 : We can also choose the order of our dataframe if we want to
df = pd.DataFrame({'A': [1.1, 2.7, 5.3], 'B': [2, 10, 9], 'C': [3.3, 5.4, 1.5], 'D': [4, 7, 15]})
print("-------------- Task 2 : \n")
print(df, "\n")

# Task 3 : We can give several dictionnaries too
df = pd.DataFrame.from_dict({
    'A': [1.1, 2.7, 5.3], 'B': [2, 10, 9], 'C': [3.3, 5.4, 1.5], 'D': [4, 7, 15]},
    orient = 'index')
print("-------------- Task 3 : \n")
print(df, "\n")

# Task 4 : Print type of each column
print("-------------- Task 4 : \n")
print(df.dtypes, "\n")

# Task 5 : We can reindex a dataframe as we like
print("-------------- Task 5 : \n")
df.index = ['Some', 'New Things', 'As', 'Indexes']
print(df, "\n")

# Task 6 : Get two first lines without param we got the 5 first lines
print("-------------- Task 6 : \n")
print(df.head(2), "\n")

# Task 7 : Get two last lines without param we got the 5 last lines
print("-------------- Task 7 : \n")
print(df.tail(2), "\n")
