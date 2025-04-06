'''
                                    WRITING TO A FILE
Just like in pseudocode, if we try to wroite to a non-existant file, that file will be 
created and then you can ofc write onto it
Also, if you write to a pre existing file, any data present will be overwritten
    DATA IS OVERWRITTEN ONLY WHEN YOU OPEN THE FILE AGAIN
'w' signifies WRITE MODE
'''

# file = open('file2', 'w')
# file.write('WWE')
# file.close()

'''
I want to creatre a file of names of everyone in the class, by taking user input
    - 5 students
    - need to take input of all names 
    - ITERATIVE - > LOOPS -> COunt is  known -> FOR LOOPS
'''
# file = open('file2', 'w')
# for i in range(5):
#     name = input("Please enter your name: ")
#     file.write(name)
# file.close()

# The above code wrote all names in SAME LINE - with no spaces

file = open('file2', 'w')
for i in range(5):
    name = input("Please enter your name: ")
    file.write(name + '\n')
    '''
    + is the string concatenation operator in python (joins two strings)
    '\n' is teh NEWLINE OPERATOR
    '''
file.close()
