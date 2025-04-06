'''
Take as input from the user an integer(n)
You need to print the sum of values from 0-n
        Eg: n = 5
            -> 1+2+3+4+5

I need to taker input from the user

I will have to perform multiple additions
    repetiitve work -> loops
        Do I know the number of iterations?
            Whenver i ask this question, if the user input BEFORE STARTING A LOOP
            tells us exactly how many iterations, we will use a for loop still
            THEREFORE, FOR LOOP

Summation Logic
'''

# DECLARE user_in, sum : INTEGER
user_in = int(input("Please enter a number: "))
sum = 0

for i in range(user_in + 1):
    # sum = sum + i
    sum += i
    print(sum)
print(f"The final answer is {sum}")

'''
sum = 0
for eg: user_in = 5
sum += i            -> 0+(0) = 0
sum += i            -> 0+(1) = 1
sum += i            -> 1+(2) = 3
sum += i            -> 3+(3) = 6
sum += i            -> 6+(4) = 10       - we have completed 5 iterations of the loop
sum += i            -> 10+(5)
'''


'''
write the same program, using a while loop
'''

