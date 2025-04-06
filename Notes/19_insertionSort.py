'''
[2, 8, 5, 3, 9, 4]

2, 8, 5
i = 2
key = 5
preKeyIndex = 1

WHILE: TRUE(1>=0) and TRUE(8>5)
arr[preKeyIndex + 1] -> arr[1+1] -> arr[2] = 5
arr[preKeyIndex + 1] = arr[preKeyIndex]  : arr[2] = arr[1]
        [2, 8, 8, 3, 9, 4]

        preKeyIndex -= 1 -> 0

WHILE: TRUE (0>=0) and FALSE(2 > 5)
    LOOP BREAK

arr[preKyIndex+1]   -> arr[1]
arr[preKeyIndex+1] = key
[2, 5, 8, 2, 9, 4]

i = 3
key = 2
preKeyIndex = 2
'''

def insertionSort(arr):
    for i in range(len(arr)):
        key = arr[i]
        preKeyIndex = i - 1
        while preKeyIndex >= 0 and arr[preKeyIndex] > key:
            arr[preKeyIndex + 1] = arr[preKeyIndex]
            preKeyIndex -= 1
        arr[preKeyIndex+1] = key

        