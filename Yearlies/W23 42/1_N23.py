# DECLARE StackVowel [0:99] OF STRING
# DELCARE StackConsonant [0:99] OF STRING

StackVowel = []
StackConsonant = []

# global VowelTop #INTEGER
# global ConsonantTop #INTEGER

# VowelTop = 0
# ConsonantTop = 0


def PushData(letter):
    global VowelTop
    global ConsonantTop

    vowels = ['a', 'e', 'i', 'o', 'u']
    if letter in vowels:
        if VowelTop == 100:
            print("Vowel Stack Full!!")
        else:
            StackVowel.append(letter)
            # CANT DO StackVowel[VowelTop]
            # If i wanted to do this, I shouldve also done: [""] * 100
            VowelTop += 1

    else:
        if ConsonantTop == 100:
            print("Consonant Stack Full!!")
        else:
            StackConsonant.append(letter)
            # CANT DO StackConsonant[ConsonantTop]
            # If i wanted to do this, I shouldve also done: [""] * 100
            ConsonantTop += 1

def ReadData():
    try:
        file = open("9618_w23_sf_42\\11_9618_42_SourceFiles\StackData.txt")
        for line in file:
            PushData(line.strip())
        file.close()
    except:
        print("File not found")


def PopVowel():
    global VowelTop

    if VowelTop == 0:
        print("The stack os already empty")
    else:
        popped = StackVowel[VowelTop - 1]
        StackVowel[VowelTop - 1] = ""
        VowelTop -= 1
        return popped
    
def PopConsonant():
    global ConsonantTop

    if ConsonantTop == 0:
        print("The stack os already empty")
    else:
        popped = StackConsonant[ConsonantTop - 1]
        StackConsonant[ConsonantTop - 1] = ""
        ConsonantTop -= 1
        return popped
    

global VowelTop #INTEGER
global ConsonantTop #INTEGER

VowelTop = 0
ConsonantTop = 0

ReadData()

letters = ""

while len(letters) < 5:
    choice = int(input("Please press 1 for Consonant or 2 for Vowel"))
    if choice == 1:
        poppedData = PopConsonant()
        letters = letters + poppedData
    else:
        poppedData = PopVowel()
        letters = letters + poppedData

print(letters)