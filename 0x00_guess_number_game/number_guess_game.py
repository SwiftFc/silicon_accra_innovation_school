import random

"""
Main - A program where a computer generates
a random number and a user has to guess the number,

Keywords - random, number,
user input, guess,
while loop, conditions, range
"""

class NumberGuessingGame:
    def __init__(self):
        self.max_guess = 8
        self.computer_num = random.randint(1, 10)
        self.guess = 0

    def start_game(self):
        print("Hello Silicon Accra\n")
        print("Welcome to the Number Guessing Game!!!\n")

        while True:
            user_name = input("Enter Your Name to get started: ")

            #if user_name.isalpha() != True:
            if user_name.replace(" ", "").isalpha() != True:
                print("\nInvalid ***  Expecting Characters only")
            
            else:    
                print("\n****Login Successful💻****")
                print("****Lets Have Fun🎮🎮🎮****")
                break




    def play_game(self):
        while self.guess < self.max_guess:
            try:
                user = input("\nGuess any Number from 1 to 10: ")
                guess_num = int(user)
            
                if guess_num == self.computer_num:
                    print("   Successful Guess!!!")
                    print("""\n****You won the Game*****
                          \n****🏆🏆🏆🏆🏆🏆🏆🏆*****
                          \n*****Congratulations*****""")
                    break
                elif guess_num < 1 or guess_num > 10:
                    print("Please guess a number within the specified range")
                elif guess_num < self.computer_num:
                    print("Guess a Higher number")
                else:
                    print("Guess a lower number")

                self.guess += 1

            except ValueError:
                print("Invalid \n**Input Only Numbers**")

        if guess_num != self.computer_num:
            print("\nSorry, Max Guessses Reached")
            
        print("\n\n*********EXIT💔💔💔**************")


if __name__ == "__main__":
    game = NumberGuessingGame()
    game.start_game()
    game.play_game()
