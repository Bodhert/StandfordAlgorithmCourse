import math

class PriorityQueue:

    def __init__(self):
        self.tree = []
        self.tree.append((None,None))

    # children of i are 2i, 2i+1

    def getParentIndex(self, childIndex):
        parentIndex = None
        if childIndex % 2 == 0:
            parentIndex = int(childIndex / 2)
        else:
            parentIndex = math.floor(childIndex / 2)
        return parentIndex

    def bubbleUp(self, childIndex):
        if childIndex == 1:
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
        #nito preguntar es por el "padre"
        self.tree.append(child)
        if len(self.tree) >= 3:
            childPos = len(self.tree)-1
            parentIndex = self.getParentIndex(childPos)

            if child[1] < self.tree[parentIndex][1]:
                self.bubbleUp(childPos)

    def getChilds(self, parentIndex):
        treeSize = len(self.tree)
        firstChildIndex = parentIndex * 2
        secondChildIndex = (parentIndex * 2) + 1
        childsIndexes = []

        if firstChildIndex < treeSize:
            childsIndexes.append(firstChildIndex)
        
        if secondChildIndex < treeSize:
            childsIndexes.append(secondChildIndex)
        
        return childsIndexes


    def bubbleDown(self, nodeIndex):
        if nodeIndex > len(self.tree):
            return
        
        childsIndexes = self.getChilds(nodeIndex)

        if len(childsIndexes) > 0:
            currentNode = self.tree[nodeIndex]
            firstChild = self.tree[childsIndexes[0]]
            biggerKnowChildPos = childsIndexes[0]
            secondChild = None
            if len(childsIndexes) == 2:
                secondChild = self.tree[childsIndexes[1]]
                if firstChild[1] > secondChild[1]:
                    biggerKnowChildPos = childsIndexes[1]
            
            if currentNode[1] > self.tree[biggerKnowChildPos][1]:
                self.tree[nodeIndex], self.tree[biggerKnowChildPos] =  self.tree[biggerKnowChildPos], self.tree[nodeIndex]
                self.bubbleDown(biggerKnowChildPos)






    def getMin(self):
        min  = self.tree[1]
        self.tree.pop(1)

        lastLeaf = self.tree.pop()
        self.tree.insert(1,lastLeaf)

        self.bubbleDown(1)
        return min
