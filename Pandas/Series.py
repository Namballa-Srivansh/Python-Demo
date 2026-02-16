import pandas as pd

# Series are Homogeneous like numpy array
# can perform vectorized operations
# Handle Missing Values with NaN
# Mutable values, immutable size 

# s= pd.Series([1, 2, 3, 4, 5])
# print(s)

# # index
# print(s[0])
# print(s[2])

# ------------------------LABEL--------------------------------- 

# s= pd.Series([23, 24, 25, 26], index=["Adam", "Eve", "Bob", "Charlie"])

# print(s)
# print(s["Adam"])
# print(s["Bob"])
# print(s.index)

# --------------------------VECTORIZATION----------------------------------
 
# s1= pd.Series([1, 2, 3, 4, 5])
# s2= pd.Series([10, 20, 30, 40, 50])

# s1[0] = 100
# print(s1 + s2)

# changed_s1 = s1.drop(0)
# print(s1)
# print(changed_s1)