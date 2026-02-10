# dtype = keyword argument that tells Numpy what kind of values are stored in an array
#         Otherwise Numpy guesses the best data type based on your data
#         Manually setting dtype improves performance
#         & is more memory efficient (especially when working with large data sets)

# integer (int8, int16, int32, int64)
# float (float16, float32, float64)
# boolean (bool_)
# string (str_, <U#)
# object (object_)

import numpy as np

# array = np.array([1, 2, 3, 4, 5], dtype=np.int32)
# array = np.array([1, 2, 3, 4, 5], dtype=np.float64)
# array = np.array([1, 2, 3, 4, 5], dtype=np.bool_)
# array = np.array([1, 2, 3, 4, 5], dtype=np.str_)
# array = np.array(["apple", "orange", "banana"], dtype="<U4") # appl oran bana
# array = np.array([1, 2.1, "apple", 4, True], dtype=np.object_)

array = np.array([1, 2, 3, 4, 5])

array = array.astype(np.float16)

print(array)
print(array.dtype)
print(f"{array.nbytes} bytes")