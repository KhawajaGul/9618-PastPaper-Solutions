class Character:
    # self.__XPosition : INTEGER
    # self.__YPosition : INTEGER
    # self.Name : STRING
    def __init__(self, XPosition, YPosition, Name):
        self.__XPosition = XPosition
        self.__YPosition = YPosition
        self.Name = Name

    def GetXPosition(self):
        return self.__XPosition
    
    def GetYPosition(self):
        return self.__YPosition
    
    def SetXPosition(self, value):
        self.XPosition = self.XPosition + value
        if self.XPosition > 10000:
            self.XPosition = 10000
        elif self.XPosition < 0:
            self.XPosition = 0

    def SetYPosition(self, value):
        self.YPosition = self.YPosition + value
        if self.YPosition > 10000:
            self.YPosition = 10000
        elif self.YPosition < 0:
            self.YPosition = 0

    def Move(self, direction):
        if direction == "up":
            self.SetYPosition(10)
        elif direction == "down":
            self.SetYPosition(-10)
        elif direction =="left":
            self.SetXPosition(-10)
        else:
            self.SetXPosition(10)
        
Jack = Character(50, 50, "Jack")

class BikeCharacter(Character):
    def __init__(self, XPosition, YPosition, Name):
        super().__init__(XPosition, YPosition, Name)

    def Move(self, direction):
        if direction == "up":
            super().SetYPosition(20)
        elif direction == "down":
            super().SetYPosition(-20)
        elif direction =="left":
            super().SetXPosition(-20)
        else:
            super().SetXPosition(20)

Karla = BikeCharacter(100, 50, "Karla")

charName = input("Do you want to move Jack or Karla? Please write exact name: ").lower()
while charName != "jack" and charName != "karla":
    charName = input("Invalid Input! PLease choose from Jack or Karla")

direction = input("Please enter the direction (up, down, left, right): ").lower()
while direction != "up" and direction != "down" and direction != "left" and direction != "right":
    direction = input("Invalid Input! PLease choose from given options")


if charName == "jack":
    Jack.Move(direction)
    print(f"Jack's new position is X={Jack.GetXPosition()} Y={Jack.GetYPosition()}")
else:
    Karla.Move(direction)
    print(f"Karla's new position is X={Karla.GetXPosition()} Y={Karla.GetYPosition()}")
