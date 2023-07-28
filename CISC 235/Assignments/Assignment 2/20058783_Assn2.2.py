class Stack:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return None
        return self.items.pop()

    def size(self):
        return len(self.items)

    def top(self):
        if (self.items != []):
            return self.items[-1]
        else:
            return None



class BinarySearchTree:

    def __init__(self, val, depth):

        self.left = None

        self.right = None

        self.val = val

        self.depth = depth


    def insert(self,val, depth = None):

        if (depth == None):

            depth = 0

        if (self.val is None):

            self.val = val

            self.depth = 0

        else:

            if val < self.val:

                if self.left is None:

                    self.left = BinarySearchTree(val, (depth + 1))

                else:

                    self.left.insert(val, (depth + 1))

            elif val > self.val:

                if self.right is None:

                    self.right = BinarySearchTree(val, (depth + 1))

                else:

                    self.right.insert(val, (depth + 1))

                    
    def searchPath(self, val, pathLst = None):

        if pathLst == None:

            pathLst = []

        if val < self.val:

            if self.left is None:

                pathLst.append(self.val)

                return pathLst

            pathLst.append(self.val)

            return self.left.searchPath(val, pathLst)

        elif val > self.val:

            if self.right is None:

                pathLst.append(self.val)

                return pathLst

            pathLst.append(self.val)

            return self.right.searchPath(val, pathLst)

        else:

            pathLst.append(self.val)

            return pathLst


    def getTotalDepth(self):

        if self.left and self.right:

            return self.depth + self.left.getTotalDepth() + self.right.getTotalDepth()

        elif self.left:

            return self.depth + self.left.getTotalDepth()

        elif self.right:

            return self.depth + self.right.getTotalDepth()

        else:

            return self.depth
        

    def totalNodes(self):

        if self.left and self.right:

            return 1 + self.left.totalNodes() + self.right.totalNodes()

        elif self.left:

            return 1 + self.left.totalNodes()

        elif self.right:

            return 1 + self.right.totalNodes()

        else:

            return 1


    def getWeightBalanceFactor(self):

        if self.left is not None:

            leftCount = self.left.totalNodes()

        if self.right is not None:

            rightCount = self.right.totalNodes()

        difference = abs(leftCount - rightCount)

        temp = abs((leftCount + 1) - rightCount)

        if temp > difference:

            difference = temp

        temp = abs(leftCount - (rightCount + 1))

        if temp > difference:

            difference = temp

        return difference


    def loadTreeFromFile(self, fileName):

        counter = 1

        treeStack = Stack()

        rightTree = BinarySearchTree(None,None)

        leftTree = BinarySearchTree(None,None)

        with open(fileName) as openfileobject:

            for line in openfileobject:

                temp = line

                temp = [ int(x) for x in temp.split()]            

                if temp[-1] == 1 and counter != 1:

                    rightTree = treeStack.pop()
                    
                if temp [-2] == 1 and counter != 1:

                    leftTree = treeStack.pop()

                if rightTree.val is None and leftTree.val is None:

                    newTree = BinarySearchTree(None,None)

                    newTree.insert(temp[0])

                else:

                    newTree = BinarySearchTree(None,None)

                    newTree.insert(temp[0])

                    if rightTree.val != None:                       

                        newTree.right = rightTree

                    if leftTree.val != None:

                        newTree.left = leftTree

                    rightTree = BinarySearchTree(None,None)

                    leftTree = BinarySearchTree(None,None)

                treeStack.push(newTree)

                counter += 1

        T = treeStack.top()

        T.setDepth()

        return T


    def setDepth(self, depth = None):

        if depth == None:

            depth = 0

            self.depth = depth

        else:

            self.depth = depth

        if self.left and self.right:

            self.left.setDepth(depth + 1)

            self.right.setDepth(depth + 1)

        elif self.left:

            self.left.setDepth(depth + 1)

        elif self.right:

            self.right.setDepth(depth + 1)
            

    def PrintTree(self):

        if self.left:

            self.left.PrintTree()

        print( self.val)

        if self.right:

            self.right.PrintTree()

            

class AVLNode(object):

    def __init__(self, key, val = None):

        self.key = key

        if val is None:

            self.val = []

        else:

            self.val = val

        self.left = None

        self.right = None
        

class AVLTreeMap(object):

    def __init__(self):

        self.node = None

        self.height = 1

        self.balance = 0


    def put(self, key, val):

        if self.node is None:

            temp = [val]

            self.node = AVLNode(key,temp)

            self.node.left = AVLTreeMap()

            self.node.right = AVLTreeMap()

        else:

            if key < self.node.key:

                self.node.left.put(key,val)

            elif key > self.node.key:

                self.node.right.put(key, val)

            else:

                newLst = self.node.val

                newLst.append(val)

                leftC = self.node.left

                rightC = self.node.right

                self.node = AVLNode(key,newLst)

                self.node.left = leftC

                self.node.right = rightC

            self.setHeight()

            self.setBalances()

            if self.balance > 1:

                if self.balance < 0:

                    self.node.left.leftRotate()

                self.rightRotate()

                self.setHeight()

            if self.balance < -1:

                if self.balance > 0:

                    self.node.right.rightRotate()

                self.leftRotate()

                self.setHeight()


    def setHeight(self):

        if self.node:

            if self.node.left:

                self.node.left.setHeight()

            if self.node.right:

                self.node.right.setHeight()

            self.height = 1 + max(self.node.left.height, self.node.right.height)

        else:

            self.height = 1


    def setBalances(self):

        if self.node:

            if self.node.left:

                self.node.left.setBalances()

            if self.node.right:

                self.node.right.setBalances()

            self.balance = self.node.left.height  - self.node.right.height

        else:

            self.balance = 0


    def leftRotate(self):

        root = self.node.right.node

        leftSubT = root.left.node

        oldRoot = self.node

        self.node = root

        oldRoot.right.node = leftSubT

        root.left.node = oldRoot


    def rightRotate(self):

        root = self.node.left.node

        leftSubT = root.right.node

        oldRoot = self.node

        self.node = root

        oldRoot.left.node = leftSubT

        root.right.node = oldRoot


    def searchPath(self, key, keyList = None):

        if keyList == None:

           keyList = []

        if self.node is None:

            return keyList

        else:

            if key < self.node.key:

                if self.node.left is None:

                    keyList.append(self.node.key)

                    return keyList

                keyList.append(self.node.key)

                return self.node.left.searchPath(key,keyList)

            elif key > self.node.key:

                if self.node.right is None:

                    keyList.append(self.node.key)

                    return keyList

                keyList.append(self.node.key)

                return self.node.right.searchPath(key,keyList)

            else:

                keyList.append(self.node.key)

                return keyList
 

    def get(self, key):

        if self.node is None:

            return None

        if self.node.key == key:

            return self.node.val

        else:

            if self.node.key > key:

                if self.node.left is None:

                    return None

                return self.node.left.get(key)

            elif self.node.key < key:

                if self.node.right is None:

                    return None

                return self.node.right.get(key)
            

    def printTree(self):

        if self.node is None:

            return

        if self.node.left:

            self.node.left.printTree()

        print("key :", self.node.key, ", val: ", self.node.val)

        if self.node.right:

            self.node.right.printTree()

            


if __name__ == "__main__":

    print("__________Testing Stack__________")

    stack = Stack()

    print("is empty:", stack.isEmpty())

    stack.push(1)

    stack.push(2)

    stack.push(3)

    stack.push(4)

    print("is empty:", stack.isEmpty())

    print("size:", stack.size())

    print("top:", stack.top())

    print("pop:", stack.pop())

    print("top:", stack.top())

    print("\n")



    print("__________Testing BST__________")

    tree = BinarySearchTree(None, None)

    

    tree.insert(8)

    tree.insert(9)

    tree.insert(10)

    tree.insert(4)

    tree.insert(7)

    tree.insert(2)

    tree.PrintTree()

    

    

    print("Path list:", tree.searchPath(7))

    print("Path list:", tree.searchPath(1))

    print("Path list:", tree.searchPath(77))

    print("Total Depth:", tree.getTotalDepth())

    print("Balance Factor:", tree.getWeightBalanceFactor())



    print("\n")

    print("__________Testing LoadTreeFromFile__________")

    

    loadTree = BinarySearchTree(None, None)

    loadTree = loadTree.loadTreeFromFile("BinaryTree.txt")

    print("Printing tree loaded from file:")

    loadTree.PrintTree()



    print("\n")

    #creating BST by reading arbitrary values from a text file

    mainTree = BinarySearchTree(None, None)

    mainTree = mainTree.loadTreeFromFile("BinaryTree.txt")



    #Total Depth

    print("Total Depth:", mainTree.getTotalDepth())



    #Weight balance for the BST

    print("Weight Balance:", mainTree.getWeightBalanceFactor())



    mainTree.insert(5)



    print("Path for searching 5:", mainTree.searchPath(5))



    #Total Depth

    print("Total Depth:", mainTree.getTotalDepth())



    #Weight balance for the BST

    print("Weight Balance:", mainTree.getWeightBalanceFactor())


    #Part 2: AVLTreeMap

    tree = AVLTreeMap()

    tree.put(15,"bob")

    tree.put(20,"anna")

    tree.put(24, "tom")

    tree.put(10, "david")

    tree.put(13, "david")

    tree.put(7, "ben")

    tree.put(30,"karen")

    tree.put(36, "erin")

    tree.put(25, "david")

    tree.put(13, "nancy")

    print("\nprinting values from AVL Tree that were inserted")

    tree.printTree()



    print("\nList of keys when searching for a specific key")

    print(tree.searchPath(36))

    print(tree.searchPath(20))

    print(tree.searchPath(1))

    print(tree.searchPath(50))

    print(tree.searchPath(14))



    print("\nRetreiving values from AVL tree if they exist")

    print(tree.get(13))

    print(tree.get(1))

    print(tree.get(50))

    print(tree.get(25))
