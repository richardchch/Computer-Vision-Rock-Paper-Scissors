#%%
import random

def get_computer_choice():
    """
    Randomly picks an option between "Rock", "Paper", and "Scissors".
    Returns the choice.
    """
    options = ["Rock", "Paper", "Scissors"]
    return random.choice(options)

def get_user_choice():
    """
    Asks the user for an input (Rock, Paper, or Scissors).
    Returns the user's choice.
    """
    user_choice = input("Enter your choice (Rock, Paper, or Scissors): ").strip().capitalize()
    while user_choice not in ["Rock", "Paper", "Scissors"]:
        print("Invalid choice. Please enter Rock, Paper, or Scissors.")
        user_choice = input("Enter your choice (Rock, Paper, or Scissors): ").strip().capitalize()
    return user_choice

def get_winner(computer_choice, user_choice):
    """
    Determines the winner based on the choices of the computer and the user.
    Prints the result and returns the winner.
    """
    if computer_choice == user_choice:
        print("It is a tie!")
        return "tie"
    elif (computer_choice == "Rock" and user_choice == "Scissors") or \
         (computer_choice == "Paper" and user_choice == "Rock") or \
         (computer_choice == "Scissors" and user_choice == "Paper"):
        print("You lost")
        return "computer"
    else:
        print("You won!")
        return "user"

def play():
    """
    Plays a game of Rock-Paper-Scissors.
    """
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    winner = get_winner(computer_choice, user_choice)
    print(f"The computer chose {computer_choice}.")

# Call the play function to start the game
play()

# %%
