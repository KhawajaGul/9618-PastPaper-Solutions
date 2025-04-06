'Make an array of size 2*3 and initialise it to all 0s and print the array'

# DECLARE noobApproach : ARRAY[0:2, 0:3] OF INTEGER
noobApproach = [[0,0,0], [0,0,0]]

'Lets go back to 1D array'
'An array of size 3 with all 0s'
noob1d = [0,0,0]

'pro way'
pro1d = [0]*3
# print(pro1d)

'Lets talk abt pro 2d'
col = 3
row = 2
pro2d = [[0]*col for i in range(row)]
# print(pro2d)


'HOW TO PRINT AN ARRAY - WITHOUT BRACKETRS AND COMMAS'

# for row in pro2d:
#     print (row)

# for row in pro2d:
#     for col in row:
#         print(col)

pro2d= [[5,8,9],[55,75,65]]

'length of pro2d (the outer array) == NumRows'
for row in range(len(pro2d)):
    for col in range(len(pro2d[row])):
        print(pro2d[row][col])

'''
len(pro2d) = 2
for row in range(2)         --> row = 0

len(pro2d[row])
len(pro2d[0])
len([5,8,9])                -> 3
for col in range(3)         -> col = 0

print(pro2d[0][0])          ->5

NEXT ITERATION OF INNER LOOP
row = 0 (thi si sfixed fo rnow as we are still in inner loop)
col = 1

print(pro2d[0][1])          -> 8

NEXT ITERATION OF INNER LOOP
row = 0
col = 2

print(pro2d[0][2])          -> 9

SINCE _THE INNER LOOP SAYS in range(3), we run till less than 3
THEREFORE INNER LOOP IS NOW COMPLETE
NEXT ITERATION OF OUTER LOOP

row = 1
First iteration of inner loop(round 2)
col = 0

print(pro2d[1][0])            -> 55 
'''