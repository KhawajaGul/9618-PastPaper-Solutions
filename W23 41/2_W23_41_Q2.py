global Queue #size 50 Datatype STRING
global HeadPointer
global TailPointer

# Queue = [""] * 50
# HeadPointer = -1
# TailPointer = 0

def Enqueue(data):
    global Queue #size 50 Datatype STRING
    global HeadPointer
    global TailPointer

    if TailPointer == 50:
        print("The queue is full")
    else:
        Queue[TailPointer] = data
        TailPointer += 1
        if HeadPointer == -1:
            HeadPointer = 0

def Dequeue():
    global Queue #size 50 Datatype STRING
    global HeadPointer
    # global TailPointer

    if HeadPointer == -1 or TailPointer == HeadPointer:
        print("The queue is already empty")
        return "Empty"
    else:
        dequeued = Queue[HeadPointer]
        Queue[HeadPointer] = ""
        HeadPointer += 1
        # if HeadPointer == TailPointer:
        #     HeadPointer = -1
        return dequeued
    

def ReadData():
    try:
        file = open("E:\AL P4\9618_w23_sf_41\\11_9618_41_SourceFiles\QueueData.txt")
        # SINCE FILE NAME HAD A \, I ADDED AN EXTRA BACKSLASH WITH IT SO PYTHON DOESNT GET CONFUSED
        for line in file:
            Enqueue(line.strip())
        file.close()
    except IOError:
        print("an IO Error Occured")

class RecordData():
    # self.ID : STRING
    # self.total : INTEGER
    def __init__(self, id, total):
        self.id = id
        self.total = total

# NumberRecords = 0
# Records = [] #Datatype: RecordData, SIZE : 50

def TotalData():
    global NumberRecords
    global Records
    DataAccessed = Dequeue()
    Flag = False


    if NumberRecords == 0:
        Records.append(RecordData(DataAccessed, 1))
        Flag = True
        NumberRecords = NumberRecords + 1
    else:
        for X in range (NumberRecords):
            if Records[X].id == DataAccessed:
                Records[X].total = Records[X].total + 1
                Flag = True

    if Flag == False:
        Records.append(RecordData(DataAccessed, 1))
        NumberRecords = NumberRecords + 1
    # print(len(Records))
    


def OutputRecords():
    for X in range(NumberRecords):
        data = Records[X].id
        total = Records[X].total
        print(f'ID {data}     Total {total}')

# main
NumberRecords = 0
Records = [] #Datatype: RecordData, SIZE : 50
Queue = [""] * 50
HeadPointer = -1
TailPointer = 0

ReadData()

while TailPointer != HeadPointer:
    TotalData()
OutputRecords()