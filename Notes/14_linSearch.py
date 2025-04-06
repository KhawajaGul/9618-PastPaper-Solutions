Students = ["Moiz", "Muqtaza", "Ahmed"]
'''
I want to find the index of Muqtaza

Think of a picture book(Album)
    You keep turning pages until you get to the desired photograph

Lin search is essentially the same
    Keep going through elementrs until you get to the desired element

Repetitve work, therefore loops
Length known, therefore FOR LOOPS
'''

# for i in Students:
#     if i == "Muqtaza":
#         print("NOW WE CAN'T RLLY PRINT THE INDEX NUMBER")


for i in range(len(Students)):
    if Students[i] == "Muqtaza":
        print(f"Muqtaza was found in index{i}")

'THIS IS KINDA INEFFICIENT, bcz u r looking for smth eventhough u have found it'


for i in range(len(Students)):
    if Students[i] == "Muqtaza":
        print(f"Muqtaza was found in index{i}")
        break