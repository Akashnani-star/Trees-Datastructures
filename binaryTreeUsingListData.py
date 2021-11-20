
# a class to create Tree object
class Tree:

    # inner class to create nodes in tree
    class Node:
        def __init__(self,data,left=None,right=None):
            self.data = data
            self.left = left
            self.right = right
        def __str__(self):
            return f"{self.left} {self.data} {self.right}"

    # this method takes list and create tree
    def takeListAndCreateTree(self,listOfValues):
        root = self.Node(listOfValues[0])
        i = 1
        prev = root
        while(i<len(listOfValues)):
            if(prev.left is None):
                prev.left = self.Node(listOfValues[i])
                i += 1
                continue
            elif(prev.right is None):
                prev.right = self.Node(listOfValues[i])
                i += 1
                continue
            else:
                prev = prev.left
        return root

    @staticmethod
    def inOrder(root):
        if(root == None):
            return
        Tree.inOrder(root.left)
        print(root.data,end=" ")
        Tree.inOrder(root.right)

    @staticmethod
    def preOrder(root):
        if(root == None):
            return
        print(root.data,end=" ")
        Tree.preOrder(root.left)
        Tree.preOrder(root.right)

    @staticmethod
    def postOrder(root):
        if(root == None):
            return
        Tree.postOrder(root.left)
        Tree.postOrder(root.right)
        print(root.data,end=" ")
        
root = Tree().takeListAndCreateTree([10,20,30,40,50])
Tree.postOrder(root)