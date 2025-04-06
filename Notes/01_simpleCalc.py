'''
Write a simple calculator that asks the user for two numbers and an 
operator (+, -, *, or /), then displays the result. 

I need to take 2 operaands from the user
    Input->I need variables to store the input in
    I need to declare the variables
        Datatype: REAL

I also need an operator as an input
    Datatype: CHAR/STRING

YOU NEED TO STORE THE RESULT ASW!!!!    

I have the operator and operand
ABH KYA?!?!?!??!
    RMMBR the operator is a string/char
    This means you can't just go like: num1 operator num2

    I will make IF statements
'''



# DECLARE Num1, Num2, Result : REAL
# DECLARE Operator : STRING

Num1 = float(input("Please input the first number: "))
Num2 = float(input("Please input the second number: "))

Operator = input("Please enter the operation that you want to perform: ")

# Single equal sign is for assignment
# Double equals sign is for comparison

if Operator == "+":
    Result = Num1 + Num2
elif Operator == "-":
    Result = Num1 - Num2
elif Operator == "*":
    Result = Num1 * Num2
else:
    Result = Num1 / Num2

print(Result)

'''
In python, all inputs are taken as STRINGS BY DEFAULT
Since the plus sign is used in python to concatenate (join) two strings, that is
what happened
    Res = "Khaw"+"aja"
    print(Res)      -> Khawaja

To fix this, we EXPLICITLY state the datatype while taking inp
In Python, we have float instead of REAL
'''