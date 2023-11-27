class Player:
    #attributes / Properties
    name = " "
    hands = 0

    def __init__(self, name, hands):
        self.name = name
        self.hands = hands

#Creation
player1 = Player("Henry", 2)
print(f" My name is {player1.name} and I use {player1.hands} hands to play the game")
