import csv
from tabulate import tabulate
import sys
import random
import re

# Main function asks the user to select an option
def main():
    selected_option = menu()
    if selected_option == 1:
        play_game()
    if selected_option == 2:
        show_words()
    if selected_option == 3:
        print("")
        print("===============================")
        sys.exit("Thank you for playing!")
    main()

# Lets user select the option of what they want to do
def menu():
    print("")
    print("====== WELCOME TO WORDLE ======")
    print("1 - Play the game")
    print("2 - Show the available words")
    print("3 - Exit the game")
    print("===============================")
    while True:
        try:
            option = int(input("Select an option: "))
            if 4 > option > 0:
                return option
            else:
                print("Select a valid level")
        except ValueError:
            print("Select a valid level")
            pass

# Prompts user to select a level
def select_level():
    while True:
        try:
            headers = ["Levels", "Length of words"]
            table = [["Level 1", "3 letters"],["Level 2", "4 letters"],["Level 3", "5 letters"]]
            print("")
            print(tabulate(table, headers, tablefmt="fancy_grid"))
            level = int(input("Select a level (1-3): "))
            if 4 > level > 0:
                return level
            else:
                pass
        except ValueError:
            pass

# Plays the game
def play_game():
    tries = 0
    check = False
    level = select_level()
    answer = get_word(level)
    print("")
    print(f"You have {10-tries} attempts left!")
    while check == False and 10 > tries :
        while True:
            try:
                attempt = input("Guess the word: ")
                check = check_word(answer, attempt.lower().strip())
                break
            except ValueError:
                print("Wrong length of word")
            except NameError:
                print("Words can only contain (a-z)")
        if check == False:
            table = []
            headers = []
            for i in range(len(answer)):
                if answer[i] == attempt.strip().lower()[i]:
                    table.append("✔")
                elif attempt.strip().lower()[i] in answer:
                    table.append("↻")
                else:
                    table.append("✘")
            print(tabulate([table], attempt.strip().lower(), tablefmt="fancy_grid"))
            print("✔ - Correct letter / ↻ - Wrong position / ✘ - Wrong letter")
            tries += 1
            print("")
            print(f"You have {10-tries} attempts left!")
        if check == True:
            table = []
            headers = []
            for i in range(len(answer)):
                if answer[i] == attempt.strip().lower()[i]:
                    table.append("✔")
                elif attempt.strip().lower()[i] in answer:
                    table.append("↻")
                else:
                    table.append("✘")
            print(tabulate([table], attempt.strip().lower(), tablefmt="fancy_grid"))
            print("✔ - Correct letter / ↻ - Wrong position / ✘ - Wrong letter")
            tries += 1
            print("")
            print(f"Congratulations, you won after {tries} attempts!")

# Returns a random word
def get_word(level):
    possibilities = []
    with open("wordle.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            possibilities.append(row)
    return random.choice(possibilities[level]).strip()

# Checks if the user's word is correct
def check_word(answer, attempt):
    if len(answer) != len(attempt):
        raise ValueError
    elif re.search("[a-zA-Z]", attempt) == None:
        raise NameError
    elif answer != attempt:
        return False
    else:
        return True

# Shows the user the words available in-game
def show_words():
    with open("wordle.csv", "r") as file:
        reader = csv.reader(file)
        table = []
        rows = []
        for row in reader:
            rows.append(row)
        while True:
            try:
                print("")
                length = int(input("Select length of the words you want to see (3-5): "))
                if 6 > length > 2:
                    break
            except ValueError:
                pass
        for i in range(len(rows[length-2])):
            table.append(rows[length-2][i].strip())
        print("")
        print("===============================")
        print("The available words are: ")
        print("")
        print(tabulate([table], tablefmt="fancy_grid"))

if __name__ == "__main__":
    main()
