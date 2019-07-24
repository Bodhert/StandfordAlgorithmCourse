import math

class PriorityQueue:

    def __init__(self):
        self.vector = []

    # children of i are 2i, 2i+1

    def bubbleUp(childIndex):
        print("dsa")

    def insertNode(self, child):
        if not self.vector:
            self.vector.append(child)
        else:
            #nito preguntar es por el "padre"
            candidatePos = len(self.vector)
            parentIndex = None
            if candidatePos % 2 == 0:
                parentIndex = candidatePos / 2
            else:
                parentIndex = math.floor(candidatePos / 2)
            
            print(child[0])
            self.vector.append(child)




    
    def helloWorld(self):
        return "Hello"
