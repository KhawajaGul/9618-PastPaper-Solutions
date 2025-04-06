'''
Arrays are a collection of items of the SAME datatype stores ina single variable

An array is a contigous chunk of memory - there are no gaps in the memory. Each element is
adjacent to one another
Since it is a contigous chunk you would need to RESERVE SPACE BEFOREHAND
        Therefore, you need to know the size of the array beforehand

PYTHON DOES NOT HAVE A DATASTRUCTYURE NAMED ARRAYS
    Python acc has a much more superior datastruture known as lists
    Your examiner does not want you to use lists
        -Lists are not fixed length
        -Lists can store multiple datatypes

WE ARE SUPPOSED TO PRETEND THAT WE HAVE ACCESS TO AN ARRAY - NOT A LIST


CINEMA
'''

'An Array of strings'
# DECLARE Students : ARRAY[0:2] OF STRING
Students = ["Moiz", "Muqtaza", "Ahmed"]
print(Students)
# DECLARE age : ARRAY[0:2] OF STRING
age = [18, 19, 19]


'Suppose I want to access an element'
name = Students[1]
# print(name)

'''
I have alr made an array, and now i want to add another element to it - HOW TO?
APPENDING TO AN ARRAY
        To add smth at the END of a pre-existing thing(datatype/files)
'''
Students.append("Syed Sami")
print(Students)
