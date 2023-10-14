import random
from word import name_list

"""
*Main -  Implementation of a Word Guessing Game in python
* 
*Return: The Computer generates a random word
         from a predefined list, and a player 
         is tasked to guess the letters in the word."""

question_list = [
    {"question": "Which of data type in python does not have the changeability characteristics:", "answer": "tuple"},
    {"question": "How do you open a file in Python:", "answer": "open()"},
    {"question": "Which data type in Python is unordered:", "answer": "dictionary"},
    {"question": "Which keyword function returns the number of items in an object, such as a string or list:", "answer": "len()"},
    {"question": "What keyword method in python is used to get the absolute value of a number:", "answer": "abs()"}]

def select_random_question():
    return random.choice(question_list)

def ask_random_question():
    random_question = select_random_question()
    question_text = random_question["question"]
    correct_answer = random_question["answer"]

    while True:
        user_answer = input(f"{question_text} ").strip()
    
        if user_answer.lower() == correct_answer.lower():
            print(f"You are correct. **Answer = {correct_answer}\n")
            break        
        else:
            print("******Wrong Answer❌❌❌\n*****Keep Trying****\n")
            

        
        
def welcome():
    print("Hello Silicon Accra\n")
    print("Welcome to the Word Guessing Game🚀🚀🚀!!!\n")

    print("**********************************************\n")
    print("Answer the Simple Python Question Below to get Access to the Program\n")

    ask_random_question()

    
            

    while True:
        user_name = input("***************************************\nEnter Your Name to get started: ")
        if user_name.replace(" ", "").isalpha() != True:
            print("\nInvalid❌❌❌❌  Expecting Alphabets only")
        else:
            desn = 'Login Successful💻💻💻'.center(50, '*')
            print(f"\n{desn}")
            print("**** Have fun🎉🎉 playing and see if you can guess the hidden words!🎮🎮🎮****\n")
            break
            
    print("\nAnswer three final questions to Start the game\n")
    ask_random_question()
    ask_random_question()
    ask_random_question()
    




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
            design = 'WELCOME TO THE MAIN PAGE OF THE WORD GUESSING GAME'.center(100, '*')
            print(design)
            print("\nGUESS THE HIDDEN WORD:  " + words_to_display)
            print("\n****  HINT: NAMES OF STUDENT IN SAIS 🧩🧩  *\n")
            print(f"*****  You have {total_lives} lives left to guess  *****")
            print("**************🧩🧩🧩🧩🧩🧩******************\n")
            user_guess = input("Guess a letter🤔🤔: ").lower()
        
            if len(user_guess) == 1 and user_guess.isalpha(): #Here Both Conditions have to be true
                if user_guess in guessed_letters:
                    print("**Letter Guessed Already❌❌")
                elif user_guess in guess_a_word:
                    print("Correct Guess👏👏✔✔")
                    guessed_letters.append(user_guess)
                else:
                    print("**Wrong Guess❌, **Try again**")
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
            print("\nSorry, you're out of attempts😢😢😢. The word was: " + guess_a_word)
            print("\n\nAnswer the question below to play again or exit🎉🎉🎉.\n")
            x = input(question2).strip()

            if x.lower() == "def __init__":
                print("\nCorrect answer✔✔✔! You may proceed to play the game🎮🚀🚀🎮 again")
                ask_random_question()
                start_game()
            else:
                print("\n   Wrong Answer, Game has Ended")
                print("\n*********EXIT💔💔💔**************")
            

welcome()
start_game()
