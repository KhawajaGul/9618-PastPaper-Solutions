
def Initialise():
    global NumberItems
    global DataStored
    Flag = False
    while Flag == False:
        NumberItems = int(input("Please enter the number of items you would like to input: "))
        if NumberItems > 0 and NumberItems < 21:
            Flag = True
    for i in range(NumberItems):
        data = int(input("Please Input a number: "))
        DataStored.append(data)

def BubbleSort():
    global DataStored
    maxComp = len(DataStored) - 1
    flag = False

    while not flag:     #while flag == False
        flag = True
        for i in range(maxComp):
            if DataStored[i] > DataStored[i+1]:
                temp = DataStored[i]
                DataStored[i] = DataStored[i+1]
                DataStored[i+1] = temp
                flag = False
        maxComp -= 1



def BinarySearch(Target):
    global DataStored
    upperBound = len(DataStored) - 1
    lowerBound = 0

    while lowerBound <= upperBound:
        midIndex = (lowerBound  +   upperBound) // 2
        midValue = DataStored[midIndex]

        if midValue == Target:
            # print(f"Target is at index {midIndex}")
            # break
            return midIndex
        elif midValue < Target:
            lowerBound = midIndex + 1
        else:
            upperBound = midIndex - 1
    
    return -1



global NumberItems #INTEGER
global DataStored #Array of integers - size 20
DataStored = []
NumberItems = 0
Initialise()
BubbleSort()
print(DataStored)
TargetNum = int(input("Please enter a number to find: "))
print(BinarySearch(TargetNum))



