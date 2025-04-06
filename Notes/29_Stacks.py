'''
                                    Stack
A stack follows Last In First Out behaviour
Stack pointer refers to the first free space(index) in our stack
Push: Adds a val to the stack
Pop: Removes a value from the stack

Just like queues, we begin with an empty array if the given size
'''

stackSize = 5
Names = [""] * stackSize
# ["9", "", "", "", ""]

stackPtr = 0

def Push(data):
    global Names
    global stackPtr

    if stackPtr >= stackSize:
        print("sorry bhai jgha nahien hai")
    else:
        Names[stackPtr] = data
        stackPtr += 1

def Pop():
    global Names
    global stackPtr

    if stackPtr == 0:
        print("bhai kuchh hai hi nahien, kya pop kroon")
    else:
        popped = Names[stackPtr - 1]
        print(popped)
        Names[stackPtr - 1] = ""
        stackPtr -= 1


'''
The user shoud be prompted as follows:
    Please select a to push, b to pop or input "exit" to quit the program

If the user selects push, take an input and push into teh stack. Of pop, show them the popped element
'''