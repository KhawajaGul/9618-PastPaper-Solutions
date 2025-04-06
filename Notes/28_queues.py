'''
                                Queues
First In First Out

Q. Make a queue of 5 students

NOTE Whenevr you are going to program for a queue, start with an empty queue of the given size
'''

# DECLARE lenQueue, HeadPointer, FreePointer : INTEGER
# DECLARE Names [0 : 4] OF STRING

lenQueue = 5
Names = [""] * lenQueue

HeadPointer = -1
FreePointer = 0


'''
        -1   0      1       2       3       4
Names =     ["",     "",     "",     "",     ""]

Two main functions associated with Queues
        Enqueue and Dequeue
'''

def Enqueue(data):
    global Names
    global HeadPointer
    global FreePointer

    if FreePointer >= lenQueue:
        print("Queue full")
    else:
        Names[FreePointer] = data
        FreePointer += 1
        if HeadPointer == -1:
                HeadPointer = 0

def Dequeue():
        global Names
        global HeadPointer
        global FreePointer

        if HeadPointer== -1:
              print("Nothing to dequeue")
        else:
              dequeued = Names[HeadPointer]
              Names[HeadPointer] == ""
              HeadPointer += 1
              print(f"Dequeued: {dequeued}")

              if HeadPointer == FreePointer:
                    HeadPointer = -1
                    FreePointer = 0