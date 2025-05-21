# DETAILED Q2 solved on stream

def RecursiveInsertion(IntegerArray, NumberElements):
    if NumberElements <= 1:
        return IntegerArray
    else:
        RecursiveInsertion(IntegerArray, NumberElements-1)
        LastItem = IntegerArray[NumberElements-1]
        CheckItem = NumberElements - 2

    LoopAgain = True
    if CheckItem < 0:
        LoopAgain = False
    elif IntegerArray[CheckItem] < LastItem:
        LoopAgain = False

    while LoopAgain: #Equivalent to saying while LoopAgain == True
        IntegerArray[CheckItem + 1] = IntegerArray[CheckItem]
        CheckItem = CheckItem - 1
        if CheckItem < 0:
            LoopAgain = False
        elif IntegerArray[CheckItem] < LastItem:
            LoopAgain = False
    
    IntegerArray[CheckItem+1] = LastItem
    return IntegerArray





def IterativeInsertion(IntegerArray, NumberElements):
    for i in range(NumberElements):
        key = IntegerArray[i]
        preKeyIndex = i - 1
        while preKeyIndex >= 0 and IntegerArray[preKeyIndex] > key:
            IntegerArray[preKeyIndex + 1] = IntegerArray[preKeyIndex]
            preKeyIndex -= 1
        IntegerArray[preKeyIndex+1] = key
    return IntegerArray





def BinarySearch(IntegerArray, First, Last, ToFind):
    if First > Last:
        return -1
    else:
        Middle = int((Last+First)/2)
        if IntegerArray[Middle] == ToFind:
            return Middle
        elif IntegerArray[Middle] > ToFind:
            return BinarySearch(IntegerArray, First, Middle-1, ToFind)
        else:
            return BinarySearch(IntegerArray, Middle+1, Last, ToFind)
        
'''
arr = [1,2,3,4]
First = 0
Last = 3
ToFind = 5

mid = 1
arr[mid] => 2

    Go to Upper half
Last = 3
First = mid+1 ==> 2
mid = 2
arr[mid] => 3

    Go to Upper Half
Last = 3
First = mid + 1 ==> 3
mid = 1
'''

NumberArray = [100,85,644,22,15,8,1]
Sorted = RecursiveInsertion(NumberArray,len(NumberArray))
print("Reursive", Sorted)

SortedIterative = IterativeInsertion(NumberArray,len(NumberArray))
print("Iterative", SortedIterative)

position = BinarySearch(Sorted, 0, len(NumberArray)-1, 644)
if position == -1:
    print("Not Found!!")
else:
    print(position)