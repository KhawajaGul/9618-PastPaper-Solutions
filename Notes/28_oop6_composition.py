'''
                            Composition
What is a car composed of?
    Engine
    Lights
    Every car will have an engine and lights
    HOWEVER, diff cc of engine
            diff luminosity of lights

Since the general template is the same, but details change -> we know this is a task 
for classes


NOTE These different objects are going to come togather to form one object -> CARRR
This is the idea of composition
'''

class Engine:
    def __init__(self, cc):
        self.cc = cc
    
    def start(self):
        print(f"Starting the {self.cc}cc engine")
    
    def sportsMode(self):
        print("Going into sports mode!!!")

class Lights:
    def __init__(self, wattage):
        self.wattage = wattage
    
    def on(self):
        print(f"Turning on the {self.wattage} Watts lights")

    def highBeam(self):
        print(f"High beam on")



class Car:
    def __init__(self, model, lightWattage, engineCC):
        self.model = model
        self.engine = Engine(engineCC)
        self.lights = Lights(lightWattage)

    def startCar(self):
        self.engine.start()
        self.lights.on()

    def sports(self):
        self.engine.sportsMode()
        self.lights.highBeam()

car1 = Car("c63", 30, 6300)
car1.startCar()
print("Race time")
car1.sports()