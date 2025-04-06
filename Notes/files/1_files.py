'''
HOW TO READ FROM A FILE
    CHECK if file is present in teh same folder as your code


We always start by opening a file
we will use the character 'r' to signify read mode    
'''
file = open("temp.txt", 'r')

text = file.read()
print(text)

file.close()
