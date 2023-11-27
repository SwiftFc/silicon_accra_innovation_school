class Human:
    #attributes/properties
    number_of_legs = 0
    number_of_hands = 0
    energy = 0
    mouth = 0
    jumping_ability = False
    number_of_ears = 0
    eyes = 0
    name = " "


    #Constructor
    def __init__(self, name, eyes, number_of_legs, number_of_hands, number_of_ears, mouth):
        self.name = name
        self.eyes = eyes
        self.number_of_legs = number_of_legs
        self.number_of_hands = number_of_hands
        self.number_of_ears = number_of_ears
        self.mouth = mouth

    def clap(self):
        available_hands = self.number_of_hands
        print(f"clapping with {available_hands} hands")


#Creation of Human1 
human1 = Human("Henry",2,2,2,2,1)
print(f"My name is: {human1.name} and I have {human1.number_of_hands} hands")
print("\nThe number of eyes is:", human1.eyes)
print(human1.clap())


