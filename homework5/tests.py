import unittest
from PriorityQueue import PriorityQueue


class testPq(unittest.TestCase):

    def testInsertnodes(self):
        pq = PriorityQueue()
        pq.insertNode((1,1))
        pq.insertNode((1,-1))
        pq.insertNode((1,-100))

        print(pq.tree)
        self.assertIsNotNone(pq.tree)

if __name__ == '__main__':
    unittest.main()
