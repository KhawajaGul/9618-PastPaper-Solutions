for i in range(5):
    print(i)

'''
IN python, loops always start from 0
Therefore, tghe number passed in bracketsis THE UPPER BOUND
    Therefore the loop runs till i<(5)

Now I want the same output using a while loop

while loops DO NOT have integrated counters
we, therefore need to create and manage a counter
'''

# DECLARE Ibrahim : INTEGER
Ibrahim = 0

while Ibrahim < 5:
    print(Ibrahim)
    # Ibrahim = Ibrahim + 1     THIS IS A NOOB WAY
    Ibrahim += 1