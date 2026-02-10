
# collection = single "Variable" used to store multiple values
# List = [] ordered and changeable. Duplicates OK
# Set = {} unordered and immutable. but Add/Remove OK. No Duplicates
# Tuple = () ordered and unchangeable. Duplicates OK. Faster

# +++++++++++++++++++++++++++++LIST++++++++++++++++++++++++++

# fruits = ["apple", "orange", "banana", "coconut"]

# print(dir(fruits)) Prints all the functions of List
# print(help(fruits))

# print("apple" in fruits) checks present or not and prints true or false
# print("pineapple" in fruits)

# print(fruits)
# print(fruits[0])
# print(fruits[1])
# print(fruits[2])
# print(fruits[3])
# print(fruits[0:3])
# print(fruits[::2])
# print(fruits[::-1])

# for fruit in fruits:
#     print(fruit)

# fruits[0] = "pineapple"
# print(fruits)

# print(len(fruits))
# fruits.clear()
# fruits.sort()
# fruits.append("Pineapple")
# fruits.remove("apple")
# fruits.insert(0, "pineapple")
# print(fruits.index("apple"))
# fruits.count()

# ++++++++++++++++++++++++SET+++++++++++++++++++++++++++++++++++

fruits = {"apple", "orange", "banana", "coconut", "coconut"}

# print(dir(fruits)) Prints all the functions of Set
# print(help(fruits))

# print("apple" in fruits) checks present or not and prints true or false
# print("pineapple" in fruits)

# print(fruits)

# for fruit in fruits:
#     print(fruit)

# print(len(fruits))
# fruits.add()
# fruits.remove("apple")

#+++++++++++++++++++++++++++++TUPLES++++++++++++++++++++++++++++++++

# fruits = ["apple", "orange", "banana", "coconut"]

# print(dir(fruits)) Prints all the functions of List
# print(help(fruits))

# print("apple" in fruits) checks present or not and prints true or false
# print("pineapple" in fruits)


# for fruit in fruits:
#     print(fruit)

# print(fruits)

# fruits.index("apple")
# fruits.count("coconut")