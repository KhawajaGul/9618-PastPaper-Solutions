'''

Make a class called treasure chest
Attributes:
    Question : STRING
    Answer : INTEGER
    Points : INTEGER
    PlayerName : STRING
The first three atrributes need to be kept private

- Getter for Question
- A func that checks if the user answer is correct or not by taking as input a user answer
- Implement a method for points where
    Correct ans in 1 attempts = full points
    Correct ans in 2 attempts = half points
    Correct ans in 3/4 attempts = 1/4 points
    Zero for any more attempts

'''
class TreasureChest:
    # PRIVATE question : STRING
    def __init__(self, question, answer, points, name):
        self.__question = question
        self.__answer = answer
        self.__points = points
        self.playerName = name

    def getQuestion(self):
        return self.__question
    
    def checkAns(self, userInput):
        if userInput == self.__answer:
            return True
        else:
            return False
        
    def pointCalc(self, attempts):
        if attempts == 1:
            return self.__points
        if attempts == 2:
            return (self.__points/2)
        if attempts == 3 or attempts == 4:
            return (self.__points/4)
        else:
            return 0
        
chest1 = TreasureChest("Hru", 95, 100, "Sami")

print(chest1.getQuestion())
print(chest1.checkAns(95))

print(chest1.pointCalc(3))
