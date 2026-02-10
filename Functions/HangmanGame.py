import random
from Wordslist import words
hangman_art = {0: ("     ",
                   "     ",
                   "     "),
               1: ("  o  ",
                   "     ",
                   "     "),
               2: ("  o  ",
                   "  |  ",
                   "     "),
               3: ("  o  ",
                   " /|  ",
                   "     "),
               4: ("  o  ",
                   " /|\\",
                   "     "),
               5: ("  o  ",
                   " /|\\",
                   " /   "),
               6: ("  o  ",
                   " /|\\",
                   " / \\")}

def display_man(wrong_guesses):
    
    print("***********************************")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("***********************************")
    
def display_hint(hint):
    print(" ".join(hint))

def display_answer(ans):
    print(" ".join(ans))

def main():
    ans = random.choice(list(words)).lower()   # ensure lowercase
    hint = ["_"] * len(ans)
    wrong_guesses = 0
    guessed_letters = set()

    while True:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input")
            continue
        
        if guess in guessed_letters:
            print(f"{guess} is already guessed")
            continue
        
        guessed_letters.add(guess)
        
        if guess in ans:
            for i, ch in enumerate(ans):
                if ch == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1
            
        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(ans)
            print("🎉 YOU WIN!")
            break
        
        if wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(ans)
            print("💀 YOU LOSE!")
            break

            
if __name__ == '__main__':
    main()