
##  PART 1

"""
    The class below implements a stack data structure using a python list.
    The program creates the stack object using supporting methods from the classes below.
    pop() - returns the last element pushed into the stack then removes it from the stack.
    push(e) - pushes an element into the stack.
    isEmpty()- returns a boolean based on the availability of element(s) within stack.
    size() - returns the number of elements in the stack.
    top() - return last element in the stack.
"""
    
class Stack:
    
    def __init__(self):
        self.arrList = list()   # Initialize stack to empty list

    def isEmpty():
        if len(arrList) == 0:
            return True         # If stack is empty return True
        else:
            return False        # Else (stack is not empty) return False

    def push(self, item):
        self.arrList.append(item)   # Append the item into the stack
        
    def pop(self):
        item = self.arrList[len(self.arrList) - 1]  # Fetches last element from stack, stored in variable item
        self.arrList.remove(item)   # Removes the item from the stack
        return item

    def top(self):
        item = self.arrList[len(self.arrList) - 1]  # Fetches last element from stack, stored in variable item
        return item

    def size(self):
        return len(self.arrList)    # Returns number of elements within the stack


##  PART 2

class Queue(object):    # Queue class used to implement level order traversal
    
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop()

    def isEmpty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.isEmpty():
            return self.items[-1].val

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)

class Node(object):

    def __init__(self, val=None):   # Constructor to create new node
        self.val = val
        self.leftChild = None       # Initialize left child to None
        self.rightChild = None      # Initialize right child to None

class BinaryTree():

    def __init__(self):     # BinaryTree Constructor
        self.root = None    # Initialize root to None

    def insert(self, item):         # Insert new node in tree
        if self.root is None:       # Check if root is None
            self.root = Node(item)  # If root is None, make Node(item) the root
        else:
            self._insert(item, self.root)   # Else call helper function to place node in correct position

    def _insert(self, item, currNode):      # Helper Function of Insert
        if item < currNode.val:
            if currNode.leftChild is None:
                currNode.leftChild = Node(item)
            else:
                self._insert(item, currNode.leftChild)
        elif item > currNode.val:
            if currNode.rightChild is None:
                currNode.rightChild = Node(item)
            else:
                self._insert(item, currNode.rightChild)
        else:
            print("Value is already present in tree.")

    def levelOrderTraversal(self, start):   # Implements Queue class to perform level order traversal on tree
        if start is None:
            return
        queue = Queue()
        queue.enqueue(start)
        traversal = ""
        while len(queue) > 0:
            traversal += str(queue.peek()) + "\n"
            node = queue.dequeue()
            if node.leftChild:
                queue.enqueue(node.leftChild)
            if node.rightChild:
                queue.enqueue(node.rightChild)
        print(traversal)

    def printTree(self):    # Helper Function to implement level order traversal
        return self.levelOrderTraversal(self.root)


##  PART 3

    def loadTreeFromFile(self, fileName):
        stack = Stack();
        with open(fileName) as fp:  # Open file
            for line in fp:         # For each line in the file (with content)
                sep = line.split()
                n = Node(sep[0])
                # print(n)
                if int(sep[2]) == 1:
                    n.rightChild = stack.pop() #rtree = Stack.pop()
                if int(sep[1]) == 1:
                    n.leftChild = stack.pop()   #ltree = Stack.pop()
                tree = BinaryTree()
                tree.root = n
                tree.root.leftChild = n.leftChild
                tree.root.rightChild = n.rightChild
                stack.push(tree)
        return stack.top()


##  PART 4

if __name__ == '__main__':

    tree = BinaryTree()
    tree.insert(8)
    tree.insert(4)
    tree.insert(9)
    tree.insert(2)
    tree.insert(7)
    tree.insert(10)

    tree.printTree() # level order traversal

    
    tree2 = BinaryTree()

    # Must change absolute path below to correct path of text file
    
    tree2.loadTreeFromFile("C:\\Users\\rtane\\OneDrive\\Documents\\Queen's Undergraduate - Year 3\\Semester 1\\CISC 235\\Assignments\\Assignment 2\\20058783_Assn2\\4.3.txt")

    tree2.printTree()
