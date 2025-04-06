'''
Write a program that determines if a person is eligible for a special library
membership. To qualify:
    They must be at least 18 years old
    If they are a student, their ID must be valid (expiry year)
    If they are not a studnet, they need to be a resident of Lahore

At the end, print if the user is eligible for a special library membership.
If not, tell why 

We need the user's age
        If < 18
            can't be a member
        Else:
            Student?
                IF YES -> is id valid? -> if also yes -> give membership
                IF NO -> From Lahore? -> IF YES -> membership
'''

# DECLARE Age, idExp : INTEGER
# DELARE stdStatus, resStatus : STRING

Age = int(input("Please enter your age: "))
if Age < 18 :
    print("Sorry you're too young :(")
else:
    stdStatus = input("Are you a student? (yes/no)")
    stdStatus.lower()
    if stdStatus == "yes":
        # What if the user inputs Yes instead of yes
        # In this case, if will not evaluate
        # To fix this, we have a built in function
        # .lower() and .upper()
        idExp = int(input("What is your ID expiry (year): "))
        if idExp < 2025:
            print("Sorry your student ID has expired")
        else:
            print("Welcome to the club!")
    else:
        resStatus = input("What city are you from? ")
        if resStatus == "Lahore":
            print("WELCOMMMEEE")
        else:
            print("Sorry you need to be a student or from Lahore")