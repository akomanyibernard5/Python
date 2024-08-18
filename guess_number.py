import argparse
import sys
import random

parser = argparse.ArgumentParser(
    description="Name for game"
)

parser.add_argument(
    "-n", "--name", metavar="name", dest="firstname", default="playerOne", help="Name of the player"
)

args = parser.parse_args()

def guessGame(name="playerOne"):
    gameCount = 0
    wins = 0

    def decide_winner(userInput, comResponse):
        nonlocal wins
        nonlocal gameCount
        if userInput == comResponse:
            wins += 1
            return f"{name}, you win!"
        else:
            return f"Sorry, {name}, Better luck next time."

    def play():
        nonlocal gameCount
        nonlocal wins
        try:
            userInput = int(input(f"{name}, guess which number I'm thinking of... 1, 2, or 3? "))
            if userInput not in [1, 2, 3]:
                print("Please choose a number between 1 and 3.")
                play()
                return
        except ValueError:
            print("Invalid input. Please enter a number.")
            play()
            return

        comResponse = random.choice([1, 2, 3])
        print(f"{name}, you chose {userInput}.\nI was thinking about the number {comResponse}")
        result = decide_winner(userInput, comResponse)
        gameCount += 1
        winning_percentage = (wins / gameCount) * 100
        print(f"{result}\nGame count: {gameCount}\n{name}'s wins: {wins}\nYour winning percentage: {winning_percentage:.2f}%")

    while True:
        play()
        play_again = input(f"Play again, {name}?\n\nY for Yes or \n Q to Quit: ").lower()
        if play_again == "q":
            print(f"Final game count: {gameCount}\n{name}'s total wins: {wins}\nFinal winning percentage: {winning_percentage:.2f}%")
            sys.exit()
        elif play_again != "y":
            print("Invalid input. Please enter 'Y' or 'Q'.")
            continue

guessGame(args.firstname)
