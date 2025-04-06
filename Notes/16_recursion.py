'''
In order to understand recusrion, you must first understand recursion

Recursion is teh act of calling a function from within a function
'''

def double(x):
    y = 2 * x
    print(y)
    double(y)

# double(1)

'''
The function keeps on calling itself for infinity
The only to avoid this error is to STOP RECURSION

IN order to stop recursion, we need a 'base case'
A base case is literally an if statement which will stop recursion
'''


def double(x):
    y = x * 2
    if y > 1000:
        return y
    else:
        print(y)
        double(y)

# alpha = double(1)
# print(f"The val of alpha is: {alpha}")


'USING RECURSION, count backwards from a number that user passes till 0'

def count_down(num):
    if num >= 0:
        print(num)
        num -= 1    #num = num - 1
        count_down(num)
    else:
        return-1

# count_down(9)

'''
Factorial Calculator Using Recusrion
The function will take as input an integer and it needs to return teh factorial of the 
passed integer.

fact(5) -> 5*4*3*2*1        = 120
fact(9) -> 9*8*7*6*5*4*3*2*1

fact(0) -> 1
fact(1) -> 1
NO FACTORIAL FOR NEGATIVE NUMBERS

5! = 5 * 4!
        4! = 4 * 3!
                3! = 3 * 2!
                        2! = 2 * 1!
                                1! = 1 * 0!
                                        0! = 1
'''

def fact(n):
    if n < 0:
        return -1
    elif n == 0:
        return 1
    else:
        return (n * fact(n-1))

print (fact(3))
'''
fact(3)
        return 3 * fact(2)
                    return 2 * fact(1)
                                return 1 * fact(0)
                                            return 1
'''