'''
arr = [a, b, c, d, |e|, f, g, h, i]

How many iterations do I require to find the index of a?
1
How many iterations do I require to find the index of d?
4
How many iterations do I require to find the index of i?
9

This array has a special property   -> IT IS SORTED

FOR SORTED ARRAYS 
1. We go to the middle index : mid = len(arr)//2
    Lets call the number I want to search as "Target"
2. Now I need to check whether:
                                Target > mid?
                                Target = mid?
                                Targer < mid?

'''

# print(3/2)
# print(3//2) # DROPS THE DECIMAL PART / ALWAYS ROUNDS DOWN

def binSearch(Target, arr):
    upperBound = len(arr) - 1
    lowerBound = 0

    while lowerBound <= upperBound:
        midIndex = (lowerBound  +   upperBound) // 2
        midValue = arr[midIndex]

        if midValue == Target:
            print(f"Target is at index {midIndex}")
            break
        elif midValue < Target:
            lowerBound = midIndex + 1
        else:
            upperBound = midIndex - 1