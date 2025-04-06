'''
% - modulus operator
it gives us the REMAINDER of a division

Y=user will input an integer, you need to check if the User wins or not. Winning
condition: The number should be even and greater than 500

we will first check if the number is greater than 500
IF IT IS GREATER then check IF the number is even
'''

# DECLARE Num : INTEGER
Num = int(input("Please input a number: "))

if Num > 500:
    if Num%2 == 0:
        print("You winnnn!")
    else:
        print("You lossseee")
else:
    print("You LOOOSSSEEEE")


'''
Single = is for assigning values:
    name = Gul
    (python equivalent of <- from pseudo)

Double equals is for comaprisons
    a==b ?
    (python equivalent of = from pseudo)


'''