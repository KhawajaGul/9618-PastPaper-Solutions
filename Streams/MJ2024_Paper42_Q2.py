class Node:
    # self.LeftPointer : INTEGER
    # self.RightPointer : INTEGER
    # self.Data : INTEGER
    def __init__(self, data):
        self.data = data
        self.LeftPointer = -1
        self.RightPointer = -1

    def GetLeft(self):
        return self.LeftPointer
    def GetRight(self):
        return self.RightPointer
    def GetData(self):
        return self.data
    
    def SetLeft(self, data):
        self.LeftPointer = data
    def SetRight(self, data):
        self.RightPointer = data
    def SetData(self, data):
        self.data = data



class TreeClass:
    # self.Tree[0:19] : ARRAY of type Node
    # self.FirstNode : INTEGER
    # self.NumberNodes : INTEGER
    def __init__(self):
        self.FirstNode = -1
        self.NumberNodes = 0
        self.Tree = [Node(-1) for i in range(20)]

    def InsertNode(self, NewNode):
        if self.FirstNode == -1:
            self.Tree[self.NumberNodes] = NewNode
            self.FirstNode = 0
            self.NumberNodes +=1

        else:
            if self.NumberNodes > 19:
                print("The tree is full!")
            else:
                self.Tree[self.NumberNodes] = NewNode
                tempPointer = self.FirstNode

                while True:
                    if NewNode.GetData() < self.Tree[tempPointer].GetData():
                        if self.Tree[tempPointer].GetLeft() == -1:
                            self.Tree[tempPointer].SetLeft(self.NumberNodes)
                            break
                        else:
                            tempPointer = self.Tree[tempPointer].GetLeft()
                    else:
                        if self.Tree[tempPointer].GetRight() == -1:
                            self.Tree[tempPointer].SetRight(self.NumberNodes)
                            break
                        else:
                            tempPointer = self.Tree[tempPointer].GetRight()
                self.NumberNodes += 1
                
    def OutputTree(self):
        if self.NumberNodes == 0:
            print("The tree is empty")
        else:
            for i in range(self.NumberNodes):
                node = self.Tree[i]
                print(f"Left: {node.GetLeft()}  Data: {node.GetData()}  Right: {node.GetRight()}")

    


# def main():
#     TheTree = TreeClass()

#     numbers = [10,11,5,1,20,7,15]
#     for i in numbers:
#         newNode = Node(i)
#         TheTree.InsertNode(newNode)

#     TheTree.OutputTree()


# main()

TheTree = TreeClass()

numbers = [10,11,5,1,20,7,15]
for i in numbers:
    newNode = Node(i)
    TheTree.InsertNode(newNode)

TheTree.OutputTree()
    
        
