
def ReadWords(fileName):
    global WordArray
    global NumberWords
    try:
        file = open(fileName, "r")
        for line in file:
            WordArray.append(line.strip())
        NumberWords = len(WordArray) - 1
        file.close()
        Play()

    except:
        print("An exception occured")


def Play():
    global WordArray
    global NumberWords

    print(f"The main word is {WordArray[0]}")
    print(f"We can make {NumberWords} from the main word")

    userIn = "yes"
    count = 0
    while userIn != "no":
        userIn = input("Please enter a word: ").lower()
        if userIn != "no":
            flag = False
            for i in range(len(WordArray)):
                if userIn == WordArray[i]:
                    count += 1
                    WordArray[i] = ""
                    flag = True
                    break
            if flag == True:
                print("Found Correct")
            else:
                print("found incorre")
    
    print(f"Total Correct Answers: {count}")
    percentFound = (count/NumberWords)*100
    print("Percent words found: ", percentFound)
    for i in WordArray:
        if i != "":
            print(i)



global WordArray
global NumberWords
WordArray = []

selection = input("Please choose one from easy/medium/hard")
if selection.lower() == "easy":
    ReadWords("Easy.txt")
elif selection.lower() == "medium":
    ReadWords("Medium.txt")
elif selection.lower() == "hard":
    ReadWords("Hard.txt")