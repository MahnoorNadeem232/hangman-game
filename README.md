# hangman-game

A simple text-based Hangman game written in Python.

## Description

This project is a Python implementation of the classic Hangman word-guessing game. The player must guess a hidden word one letter at a time before running out of attempts.

The game randomly selects a word from a predefined list and displays the progress after each guess using ASCII Hangman graphics.

## Features

* Random word selection
* Input validation
* Tracks guessed letters
* Prevents duplicate guesses
* Displays remaining attempts
* ASCII Hangman graphics
* Win and lose conditions

## Word List

The game currently uses the following words:

* dead
* carpet
* chick
* pencil
* shoe

## How to Run

1. Make sure Python 3 is installed.
2. Download or clone the project.
3. Open a terminal in the project folder.
4. Run:

```bash
python hangman.py
```

## Example Gameplay

```text
Welcome to Hangman Game!

The word has 6 alphabets.
You are allowed to make 6 incorrect guesses.

Word: _ _ _ _ _ _
Guess a letter: p

Good Guess! 'p' is in the word.

Word: p _ _ _ _ _
```

## Concepts Used

This project demonstrates the use of:

* Functions
* Lists
* Strings
* Loops
* Conditional Statements
* User Input
* Random Module
* ASCII Art

## Future Improvements

Possible enhancements include:

* Larger word database
* Difficulty levels
* Hint system
* Score tracking
* Play again option
* Reading words from a file

## Author

Mahnoor Nadeem

Created as a Python learning project.
