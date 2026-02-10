import numpy as np

# Aggregate functions = summarize data and typically
#                       return a single value

array = np.array([[1, 2, 3, 4, 5],
                  [6, 7, 8, 9, 10]])

# print(np.sum(array))
# print(np.mean(array))
# print(np.std(array))
# print(np.var(array))
# print(np.min(array))
# print(np.max(array))
# print(np.argmin(array)) # position of minimum value
# print(np.argmax(array)) # position of maximum value

print(np.sum(array, axis=0)) # if axis is 0 then applying function for column
print(np.sum(array, axis=1)) # if axis is 0 then applying function for row


