import unittest
from PriorityQueue import PriorityQueue
from random import randint


class testPq(unittest.TestCase):

    def testInsertnodes(self):
        pq = PriorityQueue()
        pq.insertNode((1,1))
        pq.insertNode((1,-1))
        pq.insertNode((1,-100))
        pq.insertNode((1,-4))
        pq.insertNode((1,-200))
        pq.insertNode((1,-5))
        pq.insertNode((1,7))

        self.assertIsNotNone(pq.tree)

    def testGetMin(self):
        pq = PriorityQueue()
        randomTuples = self.generateRandomTuples(10000)
        for randomT in randomTuples:
            pq.insertNode(randomT)
        
        currentMin = pq.getMin()
        while len(pq.tree) > 1:
            nextMin = pq.getMin()
            self.assertLessEqual(currentMin[1], nextMin[1])
            currentMin = nextMin

    def generateRandomTuples(self, size):
        return [(int(randint(-99999, 99999)), int(randint(-99999, 99999))) for _ in range(size)]

if __name__ == '__main__':
    unittest.main()
