import math

class PriorityQueue:

    def __init__(self):
        self.tree = []

    # children of i are 2i, 2i+1

    def getParentIndex(self, childIndex):
        parentIndex = None
        if childIndex % 2 == 0:
            parentIndex = int(childIndex / 2)
        else:
            parentIndex = math.floor(childIndex / 2)
        return parentIndex

    def bubbleUp(self, childIndex):
        if childIndex == 0:
            return
        
        parentIndex = self.getParentIndex(childIndex)

        childWeight = self.tree[childIndex][1]
        parenWeight =  self.tree[parentIndex][1]

        if childWeight < parenWeight:
            self.tree[childIndex], self.tree[parentIndex] = self.tree[parentIndex], self.tree[childIndex]
            self.bubbleUp(parentIndex)
        else :
            return

        
    def insertNode(self, child):
        if not self.tree:
            self.tree.append(child)
        else:
            #nito preguntar es por el "padre"
            self.tree.append(child)
            childPos = len(self.tree)-1
            parentIndex = self.getParentIndex(childPos)

            if child[1] < self.tree[parentIndex][1]:
                self.bubbleUp(childPos)
                print(child[1])




    
    def helloWorld(self):
        return "Hello"
