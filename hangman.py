import random

word_list=["dead","carpet","chick","pencil","shoe"]
max_incorrect_letters = 6

def choose_word(word_list):
    return random.choice(word_list)

def display_word(word, guess_letters):
    display=""
    for letter in word:
        if letter in guess_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()
        
def display_hangingman(incorrect_letters):
    stages = [
        """
        ---------
        |     |
        |     
        |    
        |    
        |
        ---------
        """,
        """
         ---------
        |     |
        |     o
        |    
        |    
        |
        ---------
        """,
         """
         ---------
        |     |
        |     o
        |     |
        |    
        |
        ---------
        """,
         """
         ---------
        |     |
        |     o
        |    /|
        |    
        |
        ---------
        """,
         """
         ---------
        |     |
        |     o
        |    /|\\
        |    
        |
        ---------
        """,
         """
         ---------
        |     |
        |     o
        |    /|\\
        |    /
        |
        ---------
        """,
         """
         ---------
        |     |
        |     o
        |    /|\\
        |    / \\
        |
        ---------
        """,
        ]
    return stages[incorrect_letters]
    
def play_game():
    word=choose_word(word_list)
    guess_letters=[]
    incorrect_letters = 0
    print("Welcome to hangingman game!")
    print(f"The word has {len(word)} letters")
    print(f"You have {max_incorrect_letters} incorrect guesses allowed")
        
    while incorrect_letters < max_incorrect_letters:
        print(display_hangingman(incorrect_letters))
        print("word: " + display_word(word, guess_letters))
        print("guessed letters:")
        print("incorrect guessses remaining: ", max_incorrect_letters - incorrect_letters)
        
        if all(letters in guess_letters for letters in word):
            print(f"Congratulations! You have WON the game, the word:  {word}")
            break
        
        guess = input("guess a letter: ").lower().strip()
        if len(guess) !=1 or not guess.isalpha():
            print("Please, Enter a single alphabet!")
            continue
        if guess in guess_letters:
            print("You have already guessed this alphabet, please try another alphabet")
            continue
        
        guess_letters.append(guess)
        if guess in word:
            print(f"_ _ Good Guess _ _ '{guess} is in the word")
        else:
            incorrect_letters += 1
            print(f"_ _ BAD _ _ '{guess} is not in the word")
            
    else:
        print(display_hangingman(incorrect_letters))
        print("Game is OVER, You are out of guesses")
        print(f"The word was: {word}")
       
if __name__ == "__main__":
    play_game()        

    
