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

    print("*****************************************\n")
    print("Answer the Python Question Below to get Access to the Game\n")
    
    while True:   
        question = "What is the string method in python to add something to a list: "
        user = input(question)
        if user == ".append()":
            print("\nYou are absolutely correct. *Answer = .append() ")
            break
        else:
            print("\n******Keep Trying******\n*****Yes You Can*****\n*****You've Got This****")

    while True:
        user_name = input("\n\nEnter Your Name to get started: ")

        if user_name.replace(" ", "").isalpha() != True:
            print("\nInvalid ***  Expecting Alphabets only")
        else:
            print("\n****Login Successful💻****")
            print("**** Have fun playing and see if you can guess the hidden words!🎮🎮🎮****")
            break

    while True:
        print("\nAnswer this question to Now Start the game\n")
        question1 = "\nHow do you append multiple values to a list python: "

        user1 = input(question1)
        if user1 == ".extend()":
            print("***You answered correctly*** Answer = .extend() ")
            break
        else:
            print("Keep Trying")
    
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
        total_lives = 5
        guessed_letters = []

        while total_lives > 0:
            words_to_display = display_word(guess_a_word, guessed_letters)
            print("\nGuess the hidden word: " + words_to_display)
            print("\n*****HINTS: NAMES OF STUDENT IN SAIS:🧩🧩*****\n")
            print(f"*****You have {total_lives} lives left to guess****")
            print("*******************************")
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
        question2 = "What special method allows you to initalize attributes in python: "

        if total_lives == 0:
            print("\nSorry, you're out of attempts. The word was: " + guess_a_word)
            print("Answer the question to play again or exit.")
            x = input(question2).strip()

            if x.lower() == "def __init__":
                print("\nCorrect answer! You may procede to play the game again")
                start_game()
            else:
                print("\nGame has Ended")
                print("\n\n*********EXIT💔💔💔**************")
            

welcome()
start_game()
