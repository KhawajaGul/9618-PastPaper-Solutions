'''
I want to take user input (int) and print all numbers from 0 - userIn
USING A WHILE LOOP

not equal to in python !=
'''

# DECLARE userIn, count : INTEGERS
# DECLARE check : BOOL
userIn = int(input("Pls enter number: "))
check = True
count = 0

# while check == True - this siatement is equivalent to the one written below
# while check:
#     print(count)
#     count += 1
#     if count == userIn+1:
#         check = False


while check:
    print(count)
    count += 1
    if count == userIn+1:
        break
'''
Break is a key word in Python - works with any loop
As soon as the line containing "break" is run, the loop is exited
'''
