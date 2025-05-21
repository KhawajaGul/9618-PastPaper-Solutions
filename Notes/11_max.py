'''
Take as input from the user 5 different positive integers and dispaly the largest

Repetitive task -> Loop
    Num of Iterations known? Yes, therefore FOR loop
'''

max = -1
for i in range(5):
    userIN = int(input("Pls enter a positive integer: "))
    if userIN > max:
        max = userIN
print(max)
