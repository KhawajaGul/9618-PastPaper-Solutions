def IterativeVowels(Value):
    Total = 0
    LengthString = len(Value)
    for X in range(LengthString):
        FirstCharacter = Value[0]
        if FirstCharacter == 'a' or FirstCharacter == 'e' or FirstCharacter == 'i' or FirstCharacter == 'o' or FirstCharacter == 'u':
            Total = Total + 1
        Value = Value[1:LengthString]
    return Total 

NumVowels = IterativeVowels("house")
print(NumVowels)


# NOTE: ALWAYS RMMBR TO THINK OF THE BASE CASE FOR RECURSION

def RecursiveVowels(value):
    if len(value) == 0:
        return 0
    else:
        FirstCharacter = value[0]
        if FirstCharacter == 'a' or FirstCharacter == 'e' or FirstCharacter == 'i' or FirstCharacter == 'o' or FirstCharacter == 'u':
            return 1 + RecursiveVowels(value[1:len(value)])
        else:
            return RecursiveVowels(value[1:len(value)])
        
'''
house

R1
is h vowel?
NO -> TUM BTAO R2 with "ouse"
            is o a vowel?
            YES -> 1 + TUM BTAO R3 "use"
                YES ->1 + 
'''