import random



class MinHeap(object):

    def __init__(self, matrix):

        self.heap = [None] # first (i.e. position 0) index must be empty

	self.P = [None]*len(matrix) # contains locations of nodes in heap


    def add(self, node):

        x = len(self.heap) # current index of node

	parent = x/2 # current index of parent node

	self.heap.append(node) # add the node to end of heap

	self.bubbleUp(x) # push x up until it's in the appropriate position within the heap



    def removeHead(self):

	if len(self.heap) <= 1: # base case

	    return None

	head = self.heap[1] # value returned at the end of the function

	self.P[head.index] = None # clear the reference to head's index from P

	if len(self.heap) == 2:

            del self.heap[1] # delete element in list

	else: # i.e. len(self.heap) > 2

            self.heap[1] = self.heap.pop(-1) # first element = last element, shortens list by 1

	    self.bubbleDown(1) # push first element down until it's in the appropriate position within the heap

	return head


    def editNode(self, index, weight, predecessor):

	x = self.P[index] # x = index in heap

	self.heap[x].weight = weight

	self.heap[x].predecessor = predecessor

	self.bubbleUp(x) # read x in the heap according to new weight



    def getNode(self, index):

	return self.heap[self.P[index]]



    def bubbleUp(self, x):

	parent = x/2

	while parent > 0 and self.heap[parent].weight > self.heap[x].weight: # while parent exists and has weight > x

	self.P[self.heap[parent].index] = x # before swap, assign parent's new heap index in P

	self.heap[x], self.heap[parent] = self.heap[parent], self.heap[x] # swap x with parent

	x = parent # x = parent

	parent = parent/2 # parent = parent of parent

        self.P[self.heap[x].index] = x # save x's new heap index in P



    def bubbleDown(self, x):

	leftChild = x*2 # index of left child

	rightChild = leftChild+1 # index of right child

	leftExists = leftChild < len(self.heap) # boolean = True if leftChild exists

	while leftExists: # while x has at least one child

            rightExists = rightChild < len(self.heap) # boolean = True if rightChild exists

            leftLess = self.heap[leftChild].weight <= self.heap[x].weight # boolean = True if leftChild's weight <= x's weight

            if rightExists:

		rightLess = self.heap[rightChild].weight <= self.heap[x].weight # boolean = True if rightChild's weight <= x's weight

		if leftLess:

		    if rightLess:

			if self.heap[leftChild].weight < self.heap[rightChild].weight: # pick the least weighted of the two

                            swap = leftChild

			else:

			    swap = rightChild

		    else:

                        swap = leftChild

		elif rightLess:

		    swap = rightChild

		else:
                                    
		    break

	    elif leftLess:

		swap = leftChild

	    else:

		break

	    self.P[self.heap[swap].index] = x # before swap, record swap's new heap index in P

	    self.heap[x], self.heap[swap] = self.heap[swap], self.heap[x] # swap parent with smaller weight child

	    x = swap # set up next comparison/swap, x = greater priority child

	    leftChild = x*2

	    rightChild = leftChild+1

	    leftExists = leftChild < len(self.heap) # update leftExists

        self.P[self.heap[x].index] = x # save x's new heap index in P



    def findErrors(self, x): # tool for purpose of debugging in case of errors during runtime

	leftChild = x*2 # index of left child

	rightChild = leftChild+1 # index of right child

	if leftChild >= len(self.heap): # if left child doesn't exist

	    return

	elif self.heap[leftChild].weight < self.heap[x].weight: # if left child has a smaller weight than x

	    print "Heap Organisation Error: heap {} < heap {},\nheap={}".format(self.heap[leftChild], self.heap[x], self)

	    return

	elif rightChild >= len(self.heap): # if rightChild doesn't exist

	    return

	elif self.heap[rightChild].weight < self.heap[x].weight: # if right child has a smaller weight than x

	    print "Heap Organisation Error: heap {} < heap {}!\nheap={}".format(self.heap[rightChild], self.heap[x], self)

	    return

	else: # children exist and are properly organised, use recursion on children

	    self.findErrors(leftChild)

	    self.findErrors(rightChild)



    def checkP(self):   # another debugger

        filterP = [x for x in self.P if x != None]

	filterP.append(None)

	setP = set(self.P)

	if len(filterP) > len(setP):

	print "Redundancy Error!\nheap = {}\nP = {}\nP filter = {}\nset of P = {}\n".format(self, self.P, filterP, setP)



    def __str__(self):

	string = "[" + str(self.heap[0])

	for i in xrange(1, len(self.heap)):

	    string = string + ", " + str(self.heap[i])

	return string + "]"



class Node(object):

    def __init__(self, index, weight, predecessor):

	self.index = index

	self.weight = weight

	self.predecessor = predecessor


    def __str__(self):

	return "({0}, {1}, {2})".format(self.index, self.weight, self.predecessor)



#----------GLOBAL VARIABLES AND FUNCTIONS----------#

adjMatrix = [[0, 15, 0, 7, 10, 0],

			 [15, 0, 9, 11, 0, 9],

			 [0, 9, 0, 0, 12, 7],

			 [7, 11, 0, 0, 8, 14],

			 [10, 0, 12, 8, 0, 8],

			 [0, 9, 7, 14, 8, 0]]



def BFS(matrix, startNode): # returns total weight

    visited = [False]*len(matrix) # keeps track of which nodes are marked

    def recurse(x):

	visited[x] = True # mark this node

	weight = 0

	for y in xrange(len(matrix[x])): # for all adjacent nodes

	    if not visited[y] and matrix[x][y] != 0: # check if node is unvisited and connection exists

	    weight = weight + matrix[x][y] + recurse(y) # sum weights

	return weight # end function

    return recurse(startNode) # begin with random node



def prims(matrix, x):

    x = Node(x, 0, None) # create and start at node x

    VR = MinHeap(matrix) # heap of all unsorted nodes

    for i in (range(x.index) + range(x.index+1,len(matrix))): # add all nodes excluding x to the heap excluding optimal edges

	VR.add(Node(i, float("inf"), None))

    totalWeight = 0

    while x != None: # while VR is not empty

	totalWeight = totalWeight + x.weight # x is part of the MST now, add it's weight to totalWeight

	x = x.index # need x's index

	for y in (range(x) + range(x+1,len(matrix))): #for all neighbors of x

	    if matrix[x][y] != 0 and VR.P[y] != None and matrix[x][y] < VR.getNode(y).weight: # if edge exists within VR and has a weight < all other available edges

		VR.editNode(y, matrix[x][y], x) # set as neighbor's new smallest edge

	    x = VR.removeHead() # get smallest edge in VR

    return totalWeight



def randomGraph(n): # returns randomly generated adjacency matrix

    matrix = [[0 for i in xrange(n)] for j in xrange(n)]

    for i in xrange(1, n): # i is an integer in the range [1 .. n-1]

	x = random.randint(0,i-1) # x is a random integer in the range [0 .. i-1]

	S = random.sample(xrange(i), x) # let S be a randomly selected sample of x values from the set {0, ..., i-1}

	for s in S:

	    w = random.randint(10,100)

	    matrix[i][s] = w # add an edge between vertex i and vertex s, with weight w

	    matrix[s][i] = w

    return matrix



#---------MAIN PROGRAM----------#

x = random.randint(0,len(adjMatrix)-1)

print "BFS weight:", BFS(adjMatrix, x)

print "prims weight:", prims(adjMatrix, x)



for n in [200, 400, 600]: # let n be the number of vertices in the graph

    ratio = 0

	for test in xrange(10): # for each n run 10 seperate tests and average their results

            graph = randomGraph(n) # construct a random graph on n vertices, in which each edge has a randomly assigned weight in the range [10 .. 100]

	    x = random.randint(0,n-1) # starting at a randomly chosen vertex

	    ratio = ratio + prims(graph, x)/float(BFS(graph, x)) # compute the ratio of Prim's_tree_total_weight / DFS_tree_total_weight

	print "prims/BFS weight={} for n={}".format(ratio/10.0, n) # compute the average ratio for n
