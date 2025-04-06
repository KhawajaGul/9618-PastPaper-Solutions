# ========================
# EXTENSIVELY COMMENTED
# ========================

class Node:
    # Each node in our tree stores:
    # - An integer value (data)
    # - A reference to its left child (index in the Tree array)
    # - A reference to its right child (index in the Tree array)

    def __init__(self, data):
        self.__data = data  # the value held by this node
        self.__LeftPointer = -1  # index of left child (-1 means no child yet)
        self.__RightPointer = -1  # index of right child (-1 means no child yet)

    # Getter method to access the data (value)
    def GetData(self):
        return self.__data

    # Setter method to update the data
    def SetData(self, data):
        self.__data = data

    # Getter for left child index
    def GetLeft(self):
        return self.__LeftPointer

    # Setter to change left child index
    def SetLeft(self, index):
        self.__LeftPointer = index

    # Getter for right child index
    def GetRight(self):
        return self.__RightPointer

    # Setter to change right child index
    def SetRight(self, index):
        self.__RightPointer = index


# ========================
# Tree Class
# ========================

class TreeClass:
    # This class holds a binary search tree using a fixed-size array
    # Instead of creating dynamic links (like in typical linked structures), we store Nodes in an array
    # Each node stores *indices* of its children, not direct references

    def __init__(self):
        self.FirstNode = -1  # Index of the root node (-1 means tree is empty)
        self.NumberNodes = 0  # Total number of nodes added so far
        self.Tree = [Node(-1) for _ in range(20)]  # Create a list of 20 empty nodes (placeholder values)

    # Method to insert a new node into the tree
    def InsertNode(self, NewNode):
        # Case 1: Tree is currently empty
        if self.FirstNode == -1:
            self.Tree[self.NumberNodes] = NewNode  # Place the new node at index 0
            self.FirstNode = 0  # Mark it as the root node
            self.NumberNodes += 1  # Increase the node count

        # Case 2: Tree is not empty — find correct position using BST rules
        else:
            # Check if the array is already full
            if self.NumberNodes > 19:
                print("The tree is full!")  # Cannot insert more nodes
            else:
                self.Tree[self.NumberNodes] = NewNode  # Place the node at the next available index
                tempPointer = self.FirstNode  # Start traversal from the root

                # Loop to find the correct position
                while True:
                    # If new data is less than current node's data, go to the left subtree
                    if NewNode.GetData() < self.Tree[tempPointer].GetData():
                        if self.Tree[tempPointer].GetLeft() == -1:
                            # If left child is empty, insert here
                            self.Tree[tempPointer].SetLeft(self.NumberNodes)
                            break
                        else:
                            # Move to left child
                            tempPointer = self.Tree[tempPointer].GetLeft()
                    else:
                        # If new data is greater than or equal to current, go right
                        if self.Tree[tempPointer].GetRight() == -1:
                            # If right child is empty, insert here
                            self.Tree[tempPointer].SetRight(self.NumberNodes)
                            break
                        else:
                            # Move to right child
                            tempPointer = self.Tree[tempPointer].GetRight()

                # Increase the node count after successful insertion
                self.NumberNodes += 1

    # Method to output the entire tree structure
    def OutputTree(self):
        if self.NumberNodes == 0:
            print("The tree is empty")
        else:
            print("Tree Structure:")
            for i in range(self.NumberNodes):
                node = self.Tree[i]
                # Show the index of left child, the data, and the index of right child
                print(f"Node Index {i}:  Left: {node.GetLeft()}  Data: {node.GetData()}  Right: {node.GetRight()}")


# ========================
# MAIN PROGRAM
# ========================

# Create the tree object
TheTree = TreeClass()

# List of integers to insert into the tree
# These will determine the tree's structure based on BST logic
numbers = [10, 11, 5, 1, 20, 7, 15]

# Loop through each number and insert it as a new Node
for i in numbers:
    newNode = Node(i)           # Create a node object
    TheTree.InsertNode(newNode)  # Insert it into the tree

# Display the final tree structure
TheTree.OutputTree()
