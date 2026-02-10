import numpy as np

# Save a Numpy array

# array = np.array([[1, 2, 3], [4, 5, 6]])

# np.save("data", array)

# print("Numpy array was saved!")

# -----------------------------------------------------------------------


# Load a Numpy array

# array = np.load("data.npy")
# print(array)


# -------------------------------------------------------------------------------

# Save multiple Numpy array

# array1 = np.array([[1, 2, 3], [4, 5, 6]])
# array2 = np.array([1.1, 2.2, 3.3, 4.4])

# np.savez("data", array1, array2)
# np.savez_compressed("data2", array1, array2)


# print("Numpy arrays were saved!")

# ------------------------------------------------------------------------------

# Load multiple Numpy arrays

arrays = np.load("data.npz")
array1 = arrays["arr_0"]
array2 = arrays["arr_1"]
print(array1,"\n", array2)