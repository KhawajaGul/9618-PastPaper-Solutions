def ReadData():
    try:
        colors = []
        file = open("Data.txt")
        for line in file:
            colors.append(line.strip())
        file.close()
        return colors
    except:
        print("AN exception occured!")

def FormatArray(myArr):
    outputStr = ""
    for i in myArr:
        outputStr = outputStr + i + " "

    outputStr = outputStr.strip()
    return outputStr

# arr = ReadData()
# print(FormatArray(arr))


def CompareStrings (First, Second):
    for i in range(len(First)):
        if First[i]>Second[i]:
            return 2
        elif Second[i] > First[i]:
            return 1
        
def Bubble(arr):
    maxComp = len(arr) - 1
    flag = False

    while not flag:     #while flag == False
        flag = True
        for i in range(maxComp):
            # if arr[i] > arr[i+1]:
            #     arr[i], arr[i+1] = swap(arr[i], arr[i+1])
            #     flag = False
            comp = CompareStrings(arr[i], arr[i+1])
            if comp == 2:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
        maxComp -= 1

    return arr


arr = ReadData()
# arr = FormatArray(arr)
arr = Bubble(arr)
arr = FormatArray(arr)
print(arr)