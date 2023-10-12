import random

"""
*Main -  Implementation of a Word Guessing Game in python
* 
*Return: The Computer generates a random word
         from a predefined list, and a player 
         is tasked to guess the letters in the word."""

def welcome():
    print("Hello Silicon Accra\n")
    print("Welcome to the Word Guessing Game!!!\n")

    
    while True:   
        user_name = input("Enter Your Name to get started: ")

        if user_name.replace(" ", "").isalpha() != True:
            print("\nInvalid ***  Expecting Alphabets only")
        else:
            print("\n****Login Successful💻****")
            print("**** Have fun playing and see if you can guess the hidden words!🎮🎮🎮****")
            break
    
name_list = ["stanley", "praise", "abena", "kate", "nehemiah", "kristal", 
             "elijah", "ergesis", "kelvin", "stephen", "caleb", "skekwonya"]


def pick_random_word():             #defining a function to pick a random word
    return random.choice(name_list) # Choose a random word from the word_list
    
def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display
    

def start_game():
        guess_a_word = pick_random_word()
        total_lives = 10
        guessed_letters = []

        while total_lives > 0:
            words_to_display = display_word(guess_a_word, guessed_letters)
            print("\nGuess the hidden word: " + words_to_display)
            print("\n*****HINTS: NAMES OF STUDENT IN SAIS:🧩🧩*****")
            print(f"*****You have {total_lives} live left to guess****")
        
            user_guess = input("Guess a letter🤔🤔: ").lower()
        
            if len(user_guess) == 1 and user_guess.isalpha(): #Here Both Conditions have to be true
                if user_guess in guessed_letters:
                    print("**Letter Guessed Already")
                elif user_guess in guess_a_word:
                    print("Correct Guess")
                    guessed_letters.append(user_guess)
                else:
                    print("**Wrong Guess**, **Try again**")
                    guessed_letters.append(user_guess)
                    total_lives -= 1
            else:
                ("Please enter a single letter.")

            if guess_a_word == display_word(guess_a_word, guessed_letters):
                print("\nCongratulations! You've guessed the word: " + guess_a_word)
                print("   Successful Guess!!!")
                print("""\n****You won the Game*****
                          \n****🏆🏆🏆🏆🏆🏆🏆🏆*****
                          \n*****Congratulations*****""")
                break
        if total_lives == 0:
            print("\nSorry, you're out of attempts. The word was: " + guess_a_word)
            print("\n\n*********EXIT💔💔💔**************")
            

welcome()
start_game()