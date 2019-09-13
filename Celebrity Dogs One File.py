import random

class Dog: #Class Dog, It Is For Generating Random Dogs, Handling Them And Printing Them
    name = "" #All the dog's statistics
    intelligence = 0 
    friendliness = 0
    exercise = 0
    drool = 0

    def __init__(self): #Constructor For Class Dog
        dogNames = []
        with open("dogs.txt", "r") as f: #Opens File To Read Dog Names
            for line in f:
                dogNames.append(line)
            for i in range(len(dogNames)):
                dogNames[i] = dogNames[i].replace("\n", "")
                
        self.name = dogNames[random.randint(0, 29)]
        self.intelligence = random.randint(1, 100)
        self.friendliness = random.randint(1, 100)
        self.exercise = random.randint(1, 10)
        self.drool = random.randint(1, 10)

    def printDog(self): #This Prints All The Dog Info When you need it
        print("============================================")
        print("{0}: ".format(self.name))
        print("Intelligence: {0}".format(self.intelligence))
        print("Friendliness: {0}".format(self.friendliness))
        print("Exercise: {0}".format(self.exercise))
        print("Drool: {0} \n".format(self.drool))

class Player: #This Class Handles All The Card Generating And Player-Computer Stuff
    numOfCards = 0
    lostPreviousRound = False
    cards = []

    def __init__(self, NumOfCardsToGenerateDivided): #Constructor For This Class
        self.numOfCards = NumOfCardsToGenerateDivided

    def generateCards(self): #Generates All The Classes
        for i in range(self.numOfCards):
            dog = Dog()
            self.cards.append(dog)

class Computer: #This Class Handles Computer Stuff
    numOfCards = 0
    lostPreviousRound = False
    cards = []

    def __init__(self, NumOfCardsToGenerateDivided): #Constructor For This Class
        self.numOfCards = NumOfCardsToGenerateDivided

    def generateCards(self): #Generates All The Classes
        for i in range(self.numOfCards):
            dog = Dog()
            self.cards.append(dog)

'''
You Are Probably Wondering Why There are 2 classes, Computer And Player, it is
Because Python Classes Work A Little Bit Different Than C++ or C#, and it did
not work with one class, so i just did 2 classes
'''

def clearScreen(): #For Clearing Screen (duh.)
    for i in range(1, 100):
        print("\n")

#This Checks When Player Lost When Won, And What Card He Lost
def exchangeCard(playerClass, computerClass, Class, chosedCard):
    try:
        #[INTELLIGENCE]
        if (Class == 1):
            if (playerClass.cards[chosedCard].intelligence >= computerClass.cards[0].intelligence):
                print("You Won This Round !!!")
                playerClass.cards.append(computerClass.cards[0])
                computerClass.cards.pop(0)
                playerClass.lostPreviousRound = False
            else:
                print("You Lost This Round.")
                computerClass.cards.append(playerClass.cards[chosedCard])
                playerClass.cards.pop(chosedCard)
                playerClass.lostPreviousRound = True

        #[FRIENDLINESS]
        elif (Class == 2):
            if (playerClass.cards[chosedCard].friendliness >= computerClass.cards[0].friendliness):
                print("You Won This Round !!!")
                playerClass.cards.append(computerClass.cards[0])
                computerClass.cards.pop(0)
                playerClass.lostPreviousRound = False
            else:
                print("You Lost This Round.")
                computerClass.cards.append(playerClass.cards[chosedCard])
                playerClass.cards.pop(chosedCard)
                playerClass.lostPreviousRound = True

        #[EXERCISE]
        elif (Class == 3):
            if (playerClass.cards[chosedCard].exercise >= computerClass.cards[0].exercise):
                print("You Won This Round !!!")
                playerClass.cards.append(computerClass.cards[0])
                computerClass.cards.pop(0)
                playerClass.lostPreviousRound = False
            else:
                print("You Lost This Round.")
                computerClass.cards.append(playerClass.cards[chosedCard])
                playerClass.cards.pop(chosedCard)
                playerClass.lostPreviousRound = True

        #[DROOL]
        elif (Class == 4):
            if (playerClass.cards[chosedCard].drool <= computerClass.cards[0].drool):
                print("You Won This Round !!!")
                playerClass.cards.append(computerClass.cards[0])
                computerClass.cards.pop(0)
                playerClass.lostPreviousRound = False
            else:
                print("You Lost This Round.")
                computerClass.cards.append(playerClass.cards[chosedCard])
                playerClass.cards.pop(chosedCard)
                playerClass.lostPreviousRound = True
                
    except Exception as e:
        print(e + "...Error, Returning To Main Menu")
        handleMenu()

#This Is Actual Game That Has Main Loop In It
def inGame(playerClass, computerClass):
    try:
        clearScreen()
        while (len(playerClass.cards) > 0 or len(computerClass.cards) > 0):
            if (len(playerClass.cards) <= 0 or len(computerClass.cards) <= 0):
                break
            
            for i in range(len(playerClass.cards)):
                playerClass.cards[i].printDog()

            if (playerClass.lostPreviousRound == False):
                print("1.Intelligence")
                print("2.Friendliness")
                print("3.Exercise")
                print("4.Drool")
                choice = int(input("Enter A Choice: "))

                print("COMPUTER'S CARD:")
                computerClass.cards[0].printDog()

                chosedCard = int(input("Enter A Card To Use: "))
                
                if (choice == 1):
                    exchangeCard(playerClass, computerClass, choice, chosedCard)
                elif (choice == 2):
                    exchangeCard(playerClass, computerClass, choice, chosedCard)
                elif (choice == 3):
                    exchangeCard(playerClass, computerClass, choice, chosedCard)
                else:
                    exchangeCard(playerClass, computerClass, 4, chosedCard)
            else:
                choices = {1 : "Intelligence",
                           2 : "Friendliness",
                           3 : "Exercise",
                           4 : "Drool"} #This Is For Computer Choices
                
                choice = random.randint(1,4)
                print("Computer Chose: " + choices[choice])
                chosedCard = int(input("Choose A Card: "))
                
                print("COMPUTER'S CARD:")
                computerClass.cards[0].printDog()
                
                exchangeCard(playerClass, computerClass, choice, chosedCard)

        if (len(playerClass.cards) == 0):
            print("YOU LOST !")
        else:
            print("YOU WIN !!!")

                
    except Exception as e:
        print(e + "...Error, Returning To Main Menu")
        handleMenu()

#This Is Starting Game After Setting It Up To Be Ready
def startGame(NumOfCardsToGenerate):
    try:
        player = Player(NumOfCardsToGenerate)
        computer = Computer(NumOfCardsToGenerate)
        
        player.generateCards()
        computer.generateCards()
        inGame(player, computer)
    except Exception as e:
        print(e + "Error, Returning To Main menu")
        handleMenu()

#This Is Setting Up Game For Stating It
def setUpGame():
    try:
        numOfCards = int(input("Enter Even Num Of Cards To Generate Between 4 And 30:"))
        if (numOfCards < 4 or numOfCards > 30):
            print("Incorrect Number Entered, Returning To Main Menu")
            handleMenu()
        else:
            print("Good Luck !")
            print("Generating Cards")
            numOfCards = numOfCards // 2
            startGame(numOfCards)
    except Exception as e:
        print(e + "...Error, Returning To Main Menu")
        handleMenu()

#This Is Main Menu, Simple
def handleMenu():
    try:
        print("Welcome To The Awesome Celebrity Dogs Game")
        print("------------------------------------------\n")
        print("1) Play Game")
        print("2) Quit")
        choice = int(input("Enter A Choice: "))
    except:
        printMenu()
    finally: #Finally Segment Happens After Try Statement If There Weren't Any Errors
        if (choice == 1):
            setUpGame()
        else:
            print("Goodbye")

handleMenu() #Calls Menu At The Starat of Program
