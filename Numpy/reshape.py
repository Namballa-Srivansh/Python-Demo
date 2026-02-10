# reshape() = Changes the shape of an array
#             w/o altering its underlying data
#             .reshape(rows, columns)

import numpy as np

array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# array = array.reshape(2, 6)

# array = array.reshape(3, 2, 2)
 
# array = array.reshape(-1, 6) # numpy automatically calculates the rows sam can be applied to columns

print(array.shape)
print(array)

