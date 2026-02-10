import random

low = 1
high = 100
answer = random.randint(low, high)
guesses = 0
is_running = True

print("Python Number guessing Game")
print(f"Select a number between {low} and {high}")

while is_running:
    guess = input("Enter Your Guess: ")
    
    
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        
        if guess < low or guess > high:
            print("That number is out of range")
            print("Please select a number between {low} and {high}")
            
        elif guess < answer:
            print("Too low! Try again!")
            
        elif guess > answer:
            print("Too high! Try again!")
            
        else:
            print(f"CORRECT! The answer was {answer}")
            print(f"Number of guesses: {guesses}")
            is_running = False
            
    else:
        print("Invalid Guess")
        print("Please select a number between {low} and {high}")

