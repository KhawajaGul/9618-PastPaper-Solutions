'''
What if I only want to read ONE LINE from the entire file
Ofc since I am still reading, I will definitely still open the file in read mode
'''
# file = open("temp.txt", "r")
# line1 = file.readline()
# print(line1)
# file.close()

'How to read x number of lines - LOOPS'
# file = open("temp.txt", "r")
# for i in range(4):
#     line = file.readline()
#     print(line)
# file.close()

"The blanks being print after every line are extra whitespaces(new line characters)"
"HOW TO FIX? Strip our string of these extra whitespaces"
# file = open("temp.txt", "r")
# for i in range(4):
#     line = file.readline()
#     print(line.strip())
# file.close()

'What if I want to read teh entire file usingh loops but dk the num of lines'
file = open('temp.txt', 'r')
for j in file:
    print(j.strip())
file.close()