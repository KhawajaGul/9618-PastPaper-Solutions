# Declare global variables to be used across functions
global Queue  # A list of size 50, used to implement a queue (data type: STRING)
global HeadPointer  # Points to the front of the queue (for dequeue)
global TailPointer  # Points to the end of the queue (for enqueue)

# Initialize the queue and pointers
Queue = [""] * 50  # A fixed-size queue of 50 empty string slots
HeadPointer = -1  # -1 means the queue is currently empty
TailPointer = 0  # Points to the next available position to insert data

# Function to add data to the queue
def Enqueue(data):
    global Queue
    global HeadPointer
    global TailPointer

    # Check if the queue is full
    if TailPointer == 50:
        print("The queue is full")
    else:
        # Insert data at the tail position
        Queue[TailPointer] = data
        TailPointer += 1

        # If this is the first item, move the head pointer to 0
        if HeadPointer == -1:
            HeadPointer = 0

# Function to remove data from the front of the queue
def Dequeue():
    global Queue
    global HeadPointer

    # If the queue is empty
    if HeadPointer == -1 or TailPointer == HeadPointer:
        print("The queue is already empty")
        return "Empty"
    else:
        # Remove the front item and return it
        dequeued = Queue[HeadPointer]
        Queue[HeadPointer] = ""  # Optional: clear the slot
        HeadPointer += 1
        return dequeued

# Function to read data from a file and enqueue it
def ReadData():
    try:
        # Open the file (note: double backslash used in path to avoid errors)
        file = open("E:\\AL P4\\9618_w23_sf_41\\11_9618_41_SourceFiles\\QueueData.txt")

        # Read each line from the file, remove newline, and enqueue it
        for line in file:
            Enqueue(line.strip())

        file.close()
    except IOError:
        print("An IO Error occurred while trying to read the file.")

# A class to store each unique ID and how many times it appeared
class RecordData():
    # self.id : STRING
    # self.total : INTEGER
    def __init__(self, id, total):
        self.id = id
        self.total = total

# Function to process each item from the queue and count its occurrences
def TotalData():
    global NumberRecords
    global Records

    DataAccessed = Dequeue()  # Get the next item from the queue
    Flag = False  # To check if data was found in Records

    # If this is the first record being processed
    if NumberRecords == 0:
        Records.append(RecordData(DataAccessed, 1))  # Add new record
        Flag = True
        NumberRecords += 1
    else:
        # Check if this data already exists in Records
        for X in range(NumberRecords):
            if Records[X].id == DataAccessed:
                Records[X].total += 1  # Increment the count
                Flag = True

    # If it was not found in Records, create a new one
    if not Flag:
        Records.append(RecordData(DataAccessed, 1))
        NumberRecords += 1

# Function to display all the records and their totals
def OutputRecords():
    for X in range(NumberRecords):
        data = Records[X].id
        total = Records[X].total
        print(f'ID {data}     Total {total}')

# ========================
# MAIN PROGRAM EXECUTION
# ========================

# Initialize global structures
NumberRecords = 0
Records = []  # A list of RecordData objects, size 50
Queue = [""] * 50
HeadPointer = -1
TailPointer = 0

# Step 1: Read data from file and enqueue it
ReadData()

# Step 2: Process the queue until it's empty
while TailPointer != HeadPointer:
    TotalData()

# Step 3: Display the final tally of all IDs
OutputRecords()
