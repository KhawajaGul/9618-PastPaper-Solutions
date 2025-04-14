'''
We need to figure out how to sort arrays
        DEFAULT: ASCENDING ORDER

unsorted = [9,2,5,7,3,1]


Bubble sort will compare element i with element i+1
    Sort if the element is out of place

    
ONE ITERATION OVER THE ARRAY fixes the position of ONE element
    [10, 8, 2]
        Intermediary step: [8, 10, 2]
    [8, 2, 10]

In the first iteration, max total comparisons are going to be (length-1)
Then we continue decreasing them by one as elements continue getting fixed


1. Iterate over the array   -> LOOPS (FOR LOOPS)
2. Iterate over the array again and again   -> LOOPS 
    NESTED LOOPS

OUTER: Iterate over the array again and again. FIx all elements
{
    INNER: Iterate over the array, fixing one element at a time
}

'''

def swap(a, b):
    print(a)    #5
    print(b)    #9
    temp = a
    a = b
    b = temp
    print(a)    # 9
    print(b)    # 5
    return a, b

def BubbleSort(kashif):
    maxComp = len(kashif) - 1
    flag = False

    while not flag:     #while flag == False
        flag = True
        for i in range(maxComp):
            if kashif[i] > kashif[i+1]:
                kashif[i], kashif[i+1] = swap(kashif[i], kashif[i+1])
                flag = False
        maxComp -= 1


