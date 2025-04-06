'''
What does a Node consist of
    1. Data     - ANY DATA
    2. Pointer

Each node is made up of same 2 things
A linked List made up of multiple nodes LINKED together

How did we make a node in AS - Psuedocode
We studied classes which are a close similar
'''

class Node():
    def __init__(self, data, pointer):
        self.data = data
        self.pointer = pointer

# Initialise a LL of 10 noded
'''
A ll is basically just a lot of nodes strung together
->We need a place to store these lots of nodes in
        An Array sounds like a good idea

        0 reresents NO DATA
Head pointer - POints towards teh head of the list
Free Ptr - first free elem
'''

# DECLARE linkedList : ARRAY [1:10] OF Node
linkedList = [
    Node(1,1), Node(5,4), Node(6,7), Node(7,5), Node(2,2),
    Node(0,6), Node(0,8), Node(56,3), Node(0,9), Node(0, -1)

]
'1->5->2->6->56->7'

Headpointer = 0
freePointer = 5

def addNode(data):
    global freePointer
    if freePointer == -1:
        print("LIST FULL (chal bhag jaa)")
    else:
        # linkedList[freePointer] = data        CANT SAY THIS
        # linkedList[freePointer]   -> Now I am accessing the object node
        linkedList[freePointer].data = data
        'Is the free ptr still free? NO -> I NEED TO UPDATE IT'
        'Since I have to update it from within the function -> NEED TO TAKE IT AS global'
        freePointer = linkedList[freePointer].pointer

def searchElement(target):
    tempPointer = Headpointer

    while tempPointer != -1:
        if linkedList[tempPointer].data == target:
            print(f"{target} found at Index {tempPointer}")
            return tempPointer
        else:
            tempPointer = linkedList[tempPointer].pointer
    
    return -1



def searchElement(target):
    tempPointer = Headpointer

    while tempPointer != -1:
        if linkedList[tempPointer].data == target:
            print(f"{target} found at Index {tempPointer}")
            return tempPointer
        else:
            tempPointer = linkedList[tempPointer].pointer
    