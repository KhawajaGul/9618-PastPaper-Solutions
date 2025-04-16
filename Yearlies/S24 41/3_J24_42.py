global QueueData
global QueueHead
global QueueTail

QueueData = [""]*20
QueueHead = -1
QueueTail = -1

def Enqueue(data):
    global QueueData
    global QueueHead
    global QueueTail

    if QueueTail == 19:
        return False
    else:
        if QueueHead == -1:
            QueueHead = 0
            if QueueTail == -1:
                QueueTail = 0
                QueueData[QueueTail] = data
        else:
            QueueTail += 1
            QueueData[QueueTail] = data
            return True
            
def Dequeue():
    global QueueData
    global QueueHead
    global QueueTail

    if QueueHead < 0:
        return False
    else:
        dequeued = QueueData[QueueHead]
        QueueData[QueueHead] = ""
        QueueHead += 1
        if QueueHead > QueueTail:
            QueueHead = -1
            QueueTail = -1
        return dequeued
    

def StoreItems():
    global QueueData
    global QueueHead
    global QueueTail

    count = 0
    for i in range(10):
        data = input("Please enter a number: ")
        sum = data[0]*1+data[1]*3+data[2]*1 +data[3]*3+data[4]*1+data[5]*3
        final = int(sum/10)
        if final == 10:
            final = "X"
        if final == eval(data[6]):
            Result = Enqueue(data[0:6])
            if Result == False:
                print("The Queue is full")

        else:
            count +=1

    print(count)