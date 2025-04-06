# Define a class to represent a character in a 2D game world
class Character:
    # Private variables for position (X, Y)
    # Public variable for Name

    def __init__(self, XPosition, YPosition, Name):
        # Initialize with starting position and name
        self.__XPosition = XPosition
        self.__YPosition = YPosition
        self.Name = Name

    # Getter for X position
    def GetXPosition(self):
        return self.__XPosition
    
    # Getter for Y position
    def GetYPosition(self):
        return self.__YPosition
    
    # Setter for X position — moves by given value
    def SetXPosition(self, value):
        self.__XPosition += value  # Update private variable
        # Clamp the value between 0 and 10000
        if self.__XPosition > 10000:
            self.__XPosition = 10000
        elif self.__XPosition < 0:
            self.__XPosition = 0

    # Setter for Y position — moves by given value
    def SetYPosition(self, value):
        self.__YPosition += value  # Update private variable
        # Clamp the value between 0 and 10000
        if self.__YPosition > 10000:
            self.__YPosition = 10000
        elif self.__YPosition < 0:
            self.__YPosition = 0

    # Method to move the character in a given direction
    def Move(self, direction):
        if direction == "up":
            self.SetYPosition(10)      # Move up = increase Y
        elif direction == "down":
            self.SetYPosition(-10)     # Move down = decrease Y
        elif direction == "left":
            self.SetXPosition(-10)     # Move left = decrease X
        else:  # Assume right
            self.SetXPosition(10)      # Move right = increase X

# Create an object of Character named Jack
Jack = Character(50, 50, "Jack")

# Subclass that represents a faster character on a bike
class BikeCharacter(Character):
    def __init__(self, XPosition, YPosition, Name):
        super().__init__(XPosition, YPosition, Name)  # Inherit from Character

    # Override the Move method to move twice as fast
    def Move(self, direction):
        if direction == "up":
            super().SetYPosition(20)      # Move up by 20 units
        elif direction == "down":
            super().SetYPosition(-20)     # Move down by 20 units
        elif direction == "left":
            super().SetXPosition(-20)     # Move left by 20 units
        else:
            super().SetXPosition(20)      # Move right by 20 units

# Create an object of BikeCharacter named Karla
Karla = BikeCharacter(100, 50, "Karla")

# ========================
# USER INPUT SECTION
# ========================

# Ask user to choose which character to move
charName = input("Do you want to move Jack or Karla? Please write exact name: ").lower()

# Repeat until a valid name is given
while charName != "jack" and charName != "karla":
    charName = input("Invalid Input! Please choose from Jack or Karla: ")

# Ask user for direction to move
direction = input("Please enter the direction (up, down, left, right): ").lower()

# Repeat until a valid direction is entered
while direction not in ["up", "down", "left", "right"]:
    direction = input("Invalid Input! Please choose from given options: ")

# ========================
# CHARACTER MOVEMENT
# ========================

# Move the selected character and display new position
if charName == "jack":
    Jack.Move(direction)
    print(f"Jack's new position is X={Jack.GetXPosition()} Y={Jack.GetYPosition()}")
else:
    Karla.Move(direction)
    print(f"Karla's new position is X={Karla.GetXPosition()} Y={Karla.GetYPosition()}")
