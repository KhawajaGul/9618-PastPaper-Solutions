'''
f(x) = 2x + 1
function "f" of x
    This function will take a numeric input and mutliply it with 2 and then add 1
f(5) will equal to 11

1) When we define a function, we are essentially creating a template
2) Pass a value to the aforementioned function
        very important to know the datatype that a function accepts

IN CS< NOT ALL FUNCTIONS REQUIRE INPUTS

Procedures are known as void functions in programming
'''

# A void function, which takes no inputs
def Greeting():
    print("Hello and welcome to klasses with kurly")

# WE NEED TO CALL FUNCTIONS IN ORDER TO RUN THEM
# Greeting()

"f(x) = 2x + 1"


def f(x):
    Fizza = (2*x) + 1
    print (Fizza)
# f(5)

def personalisedGreeting(name):
    print(f"Welcome {name}")

userName = input("Please enter your name: ")
# personalisedGreeting(userName)

def f(x):
    Fizza = (2*x) + 1
    print (Fizza)
# f(5)

'f(x, y) = 3x+xy+9y'

def Ahmed(x, y):
    ans = (3*x)+(x*y)+(9*y)
    print(ans)

Ahmed(9, 5)


# FUNCTIONS THAT RETURN VALUES

'f(x, y) = 3x+xy+9y'

def Ahmed(x, y):
    ans = (3*x)+(x*y)+(9*y)
    return ans

# DECLARE alpha : INTEGER
alpha = Ahmed(9, 5)
# print(alpha)
bonus = alpha * 2