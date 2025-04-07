import datetime

class Character:
    # self.__CharacterName : STRING
    # self.DateOfBirth : DATE
    # self.__Intelligence
    # self.Speed
    def __init__(self, name, dob, intelligence, speed):
        self.__CharacterName = name
        self.DateOfBirth = dob
        self.__Intelligence = intelligence
        self.Speed = speed

    def GetIntelligence(self):
        return self.__Intelligence
    
    def GetName(self):
        return self.__CharacterName
    
    def SetIntelligence(self, newIntelligence):
        self.__Intelligence = newIntelligence

    def Learn(self):
        self.__Intelligence = self.__Intelligence * 1.1

    def ReturnAge(self):
        currAge = 2023 - self.DateOfBirth.year
        return currAge
    

FirstCharacter = Character("Royal", datetime.datetime(2019, 1, 1), 70, 30)

FirstCharacter.Learn()
print(f"The character's name is {FirstCharacter.GetName()}, its age is {FirstCharacter.ReturnAge()} and its intelligence is {FirstCharacter.GetIntelligence()}")


class MagicCharacter(Character):
    # self.Element : STRING
    def __init__(self, name, dob, intelligence, speed, element):
        super().__init__(name, dob, intelligence, speed)
        self.element = element

    def Learn(self):
        if self.element == "fire" or self.element == "water":
            self.SetIntelligence(self.GetIntelligence() * 1.2)
        elif self.element == "earth":
            self.SetIntelligence(self.GetIntelligence() * 1.3)
        else:
            self.SetIntelligence(self.GetIntelligence() * 1.1)


FirstMagicCharacter = MagicCharacter("Light", datetime.datetime(2018, 3,3), 75, 22, "fire")
FirstMagicCharacter.Learn()
print(f"The character's name is {FirstMagicCharacter.GetName()}, its age is {FirstMagicCharacter.ReturnAge()} and its intelligence is {FirstMagicCharacter.GetIntelligence()}")
