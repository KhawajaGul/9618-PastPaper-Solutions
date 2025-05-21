class Horse:
    def __init__ (self, name, maxH, percent):
        self.__Name = name
        self.__MaxFenceHeight = maxH
        self.__PercentageSuccess = percent

    def GetName(self):
        return self.__Name
    
    def GetMaxFenceHeight(self):
        return self.__MaxFenceHeight
    
    def Success(self, height, risk):
        if height > self.__MaxFenceHeight:
            return self.__PercentageSuccess * 0.2
        else:
            if risk == 1:
                return self.__PercentageSuccess * 1
            if risk == 2:
                return self.__PercentageSuccess * 0.9
    

class Fence:
    def __init__(self, height, risk):
        self.__Height = height  #integer
        self.__Risk = risk      #integer
    
    def GetHeight(self):
        return self.__Height
    def GetRisk(self):
        return self.__Risk
    


Horses = []
horse1 = Horse("Beauty", 150, 72)
Horses.append(horse1)
Horses.append(Horse("Jet", 160, 65))

print(Horses[0].GetName())
print(Horses[1].GetName())


Course = []

for i in range(4):
    valid = False

    while not valid:        #valid == False
        height = input("PLease enter height: ")
        if height >69 and height < 181:
            valid = True
        risk = int(input("Please enter risk: "))
        if risk > 5 or risk < 1:
            valid = False

    Course.append(Fence(height, risk))


for horsie in Horses:
    for obstacle in Course:
        chance = horsie.Success(obstacle.GetHeight(), obstacle.GetRisk())
        print(f"The probabbility of horse {horsie.GetName()} jumping over fence with height {obstacle.GetHeight()} successfully is {chance}%.")