import unittest
from PriorityQueue import PriorityQueue


class testPq(unittest.TestCase):

    def testInsernodes(self):
        pq = PriorityQueue()
        pq.insertNode((1,1))
        pq.insertNode((333,1))
        print(pq.vector)
        self.assertIsNotNone(pq.vector)

if __name__ == '__main__':
    unittest.main()
