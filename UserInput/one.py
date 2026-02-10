name = input("What is your name? : ")
# age = input("How old are you? : ")
# age += 1 shows error because we take input as string so cant concatenate int to it

# age = int(age)
# age += 1

#one more way is
age = int(input("How old are you? : "))
age = int(age)
age += 1

print(f"Hello {name}")
print("Happy Birthday")
print(f"You are {age} years old")