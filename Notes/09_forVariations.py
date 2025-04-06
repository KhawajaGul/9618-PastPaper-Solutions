# for i in range(5):
#     print("i")

# for i in range(3):
#     print(i)
'''
0
1
2
'''

# for i in range(11, 15):
#     print(i)

'''
We know that when there is only one number in the brackets, it is the ending point of a loop(exclusive)
When 2 numbers are present, they are the start and end points
START IS INCLUSIVE
END IS EXCLUSIVE



I want to print all numbers form 9 top 1
By default, a for loop starts from 0 and adds one in each iterations
When working in reverse, not only do we need to add startr and end points
WE ALSO NEED TO SPECIFY STEP SIZE
    STEP SIZE IS THE THIRD NUMBER WE ADD
'''

# for i in range(9, 0, -1):
#     print(i)

'I want to print all odd numbers from 1 to 10'
for i in range(1, 11, 2):
    print(i)