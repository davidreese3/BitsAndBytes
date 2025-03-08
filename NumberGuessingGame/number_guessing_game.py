import random as rd
import os

folder_path = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(folder_path, "highscore.txt")

def main():
    setup()

    print("Welcome to the number guessing game!")
    print("The number is within 1 and 100. ")

    guesses = []
    guesses = run_game()

    print(f"You guessed the number! It took {len(guesses)} guesses.")
    print(f"Your guesses: {guesses}")

    check_high_score(len(guesses))

def setup():
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    if not os.path.exists(filename):
        with open(filename, "w") as file:
            file.write("")

def run_game():
    randomNum = rd.randint(1, 100)
    guess = 0
    guesses = []
    while (guess != randomNum):
        print("Please enter a guess.")
        guess = int(input())
        if(guess > randomNum):
            print("Too high!")
        elif(guess < randomNum):
            print("Too low!")
        guesses.append(guess)
    return guesses

def check_high_score(score):  
    with open(filename, "r") as file:
        file_content = file.read()

    if(file_content == ""):
        print("No high score recorded. You got the first high score!")
        save_high_score(score)
        return

    file_content_split = file_content.split(", ")
    curr_score = int(file_content_split[0])
    curr_name = file_content_split[1]
    
    if(score < curr_score):
        print(f"You beat the high score! (({curr_score} {curr_name})")
        save_high_score(score)
    else:
        print(f"You did not beat the high score. ({curr_score} {curr_name}) Better luck next time.")

def save_high_score(score):
    print("Please enter a name.")
    new_name = input()
    with open(filename, "w") as file:
        file.write(f"{score}, {new_name}")

if __name__ == "__main__":
    main()
