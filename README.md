# Wordle - CS50P Final Project
#### Video Demo: <https://youtu.be/L34DQ_DT4to>
## Description
In this project, I recreated the game 'Wordle', where players try to guess a random word in 10 attempts. I have played 'Wordle' many times and with CS50P, I was equipped with all the necessary tools to re-create the game. A random word is generated, and you try to guess it. After each guess, the user receives feedback on the answer they gave, saying if each letter of their answer is correct, wrong or in the wrong position. I created three difficulty levels to the game ranging from 3-letter words to 5-letter words.

## Files needed
Please download all the files in the folder.
- project.py - Contains the code to play the game with all the functions inside
- test_project.py - Runs the tests to check if everything works properly
- wordle.csv - Contains the list of words used inside the game

## Libraries
Please install the tabulate library in order for the project to work properly:
- pip install tabulate

## How to play
- There are three levels inside the game. (Level 1: 3 letters, Level 2: 4 letters, Level 3: 5 letters)
- Select a level in order to play the game.
- You are given ten attempts to guess the correct random word.
- After each guess, the game tells you which letters are correct, wrong or in the wrong position and the attempts you have left.
- If you run out of attempts you lose the game!
- If you guess the word, you win the game!

## Menu
Once you start the game, you see the main menu and it asks you to select an option:
- Type 1 to play the game
> Runs the game and asks you to select a level from 1-3.
- Type 2 to show the available words inside the game
> Asks you to input the length of the words you want to see. (e.g. "3" shows the words with 3 letters)
- Type 3 to exit the game
> Exits the game

## Levels
Inside the game, there are three difficulty levels:
- Level 1
> In this level you'll only have 3 letter words to guess.
- Level 2
> In this level you'll only have 4 letter words to guess.
- Level 3
> In this level you'll only have 5 letter words to guess.

## Guessing Legend
When you guess a word, you are shown a box with icons under each letter, the icons mean:

- ✔ - Correct letter in the correct position
- ↻ - Correct letter in the wrong position
- ✘ - Wrong letter (that letter is not in the word)

## Thank you
Thank you for trying my project and I hope you have fun playing it :)
