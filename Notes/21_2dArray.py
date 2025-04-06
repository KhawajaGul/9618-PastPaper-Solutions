'''
A 2D array is like a matrix

|1, 5|
|9, 7|

We want to recreate such 2D arrays in python

What is a 1D Array?
        A 1D array is basically ONE ROW with multiple columns -> [1, 2, 3]
What is a 2D Array?
        A bunch of 1D Arrays stacked on top of each other
        Multiple rows and cols
        DIFFERENTIATING FACTOR: MULTIPLE ROWS

What Datatypes can an Array hold?
        INtegers, Strings, Char, Bool, FP/REAL, date
        ANY DATATYPE
        ARRAY - An Array can have Arrays in it asw (IN terms of Python, a List of Lists)

firstArr = [[1, 5, 9, 8], [71, 32, 46, 55], [100, 500, 900, 800]]  -   2D Array
Outer Array: Contains 3 Arrays 
Inner Arrays: 1, 5, 9, 8 - INTEGERS

LET ME HELP YOU VISUALIZE THIS 2D ARRAY BETTER
[[1, 5, 9, 8],
[71, 32, 46, 55],
[100, 500, 900, 800]]

print(firstArr[1, 3]) -> 55     `THIS IS NOT HOW YOU INDEX IN PYTHON`
print(firstArr[1][3]) -> 55

RMMBR ARRAYS IN PYTHON START FROM 0
'''

# DECLARE firstArr : ARRAY[0:2, 0:3] OF INTEGER

firstArr = [[1, 5, 9, 8], [71, 32, 46, 55], [100, 500, 900, 800]]
# print(firstArr) #This prints with brackets and all

print(firstArr[1][3]) 
'The element I want to print is in ROW 1 (Doosri ROW), COL 3(CHOTHA COLUMN)'
