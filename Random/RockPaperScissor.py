import random

options = ("rock", "paper", "scissors")
running = True

while running:
    player = None
    computer = random.choice(options)
    
    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ")
        
        print(f"Player: {player}")
        print(f"Computer: {computer}")
        
        if player == computer:
            print("TIE!")
        
        elif player == "rock" and computer == "scissors":
            print("You WON!")
        
        elif player == "paper" and computer == "rock":
            print("You WON!")
            
        elif player == "scissors" and computer == "paper":
            print("You WON!")
        
        else:
            print("You LOST!")
            
        play_again = input("Play again? (y/n): ").lower()
        
        if not play_again == "y":
            running = False

print("Thanks For Playing!")
            