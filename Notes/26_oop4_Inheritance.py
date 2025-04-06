'''
You are programming for a car manufacturer. Obv all cars will have the same brand. HOWEVER,
models will vary
What I need to do to begin wit is store their data

Porche
    911
    GT3 RS
    Taycan

Brand = Porche
Model = 911
T&Cs = 9CG475EUJ

Brand = Porche
Model = GT3 RS
T&Cs = 9CG475EUJ

Brand = Porche
Model = Taycan
T&Cs = 9CG475EUJ

There isn't any direct repitition, however there is a lot of redundancy. As a programmer I
feel a bit uncomfortable

Notice that there is a relationship here
    All classes contain certain identical attributes
            ALL THESE ATTRIBUTES COME FROM PORCHE
            This is like childeren sharing some of their parents' traits
            (This is like all submings having same parental info in documents)

There is a similar Parent-Child Relation between company and models
    We inherit from the company
'''

# We begin by creating the parent class
class carBrand:
    def __init__(self, brand, TnCs):
        self.brand = brand
        self.TnC = TnCs

    def displayBrand(self):
        print(f"Brand name: {self.brand}")


# CHILD CLASS
# Just like your ID Card conatins the name of your parents, a child class will also contain it's parents' name
class carModel(carBrand):
    def __init__(self, model, color, brand, TnCs):
        super().__init__(brand, TnCs)
        '''The above line initializes teh constructor of the parent class from within the 
        child class.
        What is the one thing absolutely necessary for anyone in this world's existance?
                YOUR PARENTS NEED TO HAVE LIVED
            Initialising the parent class from within a child class ENSURES that everytime
            you create an instance of a child, a parent does exist
        '''
        self.model = model
        self.color = color

    def details(self):
        print(f"My model is {self.model} which is of {self.color} color")


myCar = carModel('Alto', 'Silver', 'Suzuki', 'Can flip anytime')

print(myCar.model)
print(myCar.brand)
myCar.details()
myCar.displayBrand()