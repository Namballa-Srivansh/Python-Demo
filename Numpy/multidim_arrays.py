import numpy as np

# array = np.array('A')

# array = np.array(['A', 'B', 'C'])

# array = np.array([['A', 'B', 'C'],
#                  ['D', 'E', 'F'], 
#                  ['G', 'H', 'I']])

array = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
                  [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']],
                  [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', ' ']],])

# print(array.ndim)
# print(array.shape)

# print(array[0][0][0]) # chain indexing
# print(array[1, 1, 1])

word = array[0, 0, 0] + array[2, 0, 0] + array[2, 0, 0]

print(word)