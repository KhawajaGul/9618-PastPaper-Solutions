# This function counts the number of vowels in a string using iteration
def IterativeVowels(Value):
    Total = 0  # Initialize a counter to keep track of vowels
    LengthString = len(Value)  # Get the length of the string

    # Loop runs once for each character in the string
    for X in range(LengthString):
        FirstCharacter = Value[0]  # Always pick the first character of the current string

        # Check if the character is a lowercase vowel
        if FirstCharacter == 'a' or FirstCharacter == 'e' or FirstCharacter == 'i' or FirstCharacter == 'o' or FirstCharacter == 'u':
            Total = Total + 1  # If it is a vowel, increment the counter

        # Remove the first character to move to the next one in the next iteration
        Value = Value[1:LengthString]  

    return Total  # Return the final count

# Call the iterative function on the word "house"
NumVowels = IterativeVowels("house")
print(NumVowels)  # Output will be 3 (o, u, e)


# NOTE: ALWAYS REMEMBER TO THINK OF THE BASE CASE FOR RECURSION

# This function counts the number of vowels in a string using recursion
def RecursiveVowels(value):
    # Base case: If the string is empty, return 0
    if len(value) == 0:
        return 0
    else:
        FirstCharacter = value[0]  # Get the first character of the string

        # If the first character is a vowel
        if FirstCharacter == 'a' or FirstCharacter == 'e' or FirstCharacter == 'i' or FirstCharacter == 'o' or FirstCharacter == 'u':
            # Count 1 for the current vowel, and recurse on the rest of the string
            return 1 + RecursiveVowels(value[1:len(value)])
        else:
            # If not a vowel, just recurse on the rest of the string without incrementing
            return RecursiveVowels(value[1:len(value)])


'''
Illustration of how recursion works on the string "house"

R1: Is 'h' a vowel? → No → call R2 with "ouse"
R2: Is 'o' a vowel? → Yes → 1 + call R3 with "use"
R3: Is 'u' a vowel? → Yes → 1 + call R4 with "se"
R4: Is 's' a vowel? → No → call R5 with "e"
R5: Is 'e' a vowel? → Yes → 1 + call R6 with "" (empty string)
R6: Base case hit → return 0

So total becomes: 1 (o) + 1 (u) + 1 (e) = 3
'''
