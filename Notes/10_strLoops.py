sen1 = " krlo SharamCAIES aa rahay hain"

'I wAnt to print individual characters of this string'

# for i in sen1:
#     print(i)

"Write a code that counts the number of As (upper and lower case) in sen1"

# DECLARE count : INTEGER
# count = 0
# for i in sen1:
#     if i == "a" or i =="A":
#         count +=1
# print(count)


count = 0
for i in sen1:
    if i.lower() == "a":
        count += 1
print(count)