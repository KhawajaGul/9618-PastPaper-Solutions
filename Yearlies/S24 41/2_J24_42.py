# TODO: Code intentionally left incorrect for you to debug

class Tree:
    # private growth, private maxH, private maxW : INTEGER
    # private name, private Evergreen : STRING
    def __init__(self, name, growth, maxH, maxW, Evergreen):
        self.__name = name
        self.__growth = growth
        self.__maxH = maxH
        self.__maxW = maxW
        self.__Evergreen = Evergreen

    def GetTreeName(self):
        return self.__name
    
    def GetMaxHeight(self):
        return self.__maxH
    def GetMaxWidth(self):
        return self.__maxW
    def GetGrowth(self):
        return self.__growth
    def GetEvergreen(self):
        return self.__Evergreen
        


def ReadData():
    Trees = [] #of type Tree
    try:
        file = open("9618_s24_sf_41\Trees.txt", "r")
        for line in file:
            # print(line.strip())
            line = line.strip()
            treeData = (line.split(","))
            myTree = Tree(treeData[0], treeData[1], treeData[2], treeData[3], treeData[4])
            Trees.append(myTree)
            # print(treeData)

        file.close()
    except IOError:
        print("file not found!")
    
    return Trees


def PrintTrees(Item):
    name = Item.GetTreeName()
    maxHeight = Item.GetMaxHeight()
    maxWidth = Item.GetMaxWidth()
    growth = Item.GetGrowth()
    evergreen = Item.GetEvergreen()

    if evergreen == "Yes":
        lastline = "It does not lose its leaves"
    else:
        lastline = "It loses its leaves each year"

    print(f"{name} has a maximum height {maxHeight} a maximum width {maxWidth} and grows {growth}cm a year. {lastline}")


def ChooseTree(Trees):
    Evergreen = input("Is your tree evergreen? Write yes/no: ")
    MaxH = input("Pls enter the max height you want for the tree")
    MaxW = input("Pls enter the max width you want for the tree")

    myTrees = []

    for i in Trees:
        print(i.GetTreeName()," | ", i.GetMaxHeight()," | ", i.GetMaxWidth()," | ", i.GetEvergreen())
        if i.GetMaxWidth() <= MaxW and i.GetMaxHeight() <= MaxH and i.GetEvergreen().lower()==Evergreen.lower():
            myTrees.append(i)
            PrintTrees(i)

    print(len(myTrees))

    if len(myTrees) == 0:
        print("No trees meet the output")

    Flag = False
    while Flag == False:
        purchaseName = input("Please enter tree name: ")
        for i in myTrees:
            if i.GetTreeName() == purchaseName:
                Flag = True
                purchaseHeight = input("Please enter the purchase height of the tree")
                Years = (i.GetMaxHeight()-purchaseHeight)/i.GetGrowth()
                print(Years)






TreeObjects = ReadData()
PrintTrees(TreeObjects[0])
ChooseTree(TreeObjects)