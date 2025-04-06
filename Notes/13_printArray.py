# DECLARE Students : ARRAY[0:2] OF STRING
Students = ["Moiz", "Muqtaza", "Ahmed"]

'How do I print all the elements in this array?'
# print(Students)
'''
The problem with technique is, it is printing teh entire array.
I NEED JUST THE ELEMENTS FROM THE ARRAY
'''
# print(Students[0])
# print(Students[1])
# print(Students[2])
'''
The above, while a correct method, is very time consuming
SUSTTTTTTTTT hoon mein toh
Repetitive work, therefore loops
    Since size is know, for loop
'''

# for i in range(len(Students)):
#     print(i)
# This is wrong

# for i in range(len(Students)):
#     print(Students[i])
# Completely correct


for i in Students:
    print(i)