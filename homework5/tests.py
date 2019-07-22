import unittest
from PriorityQueue import PriorityQueue


class testPq(unittest.TestCase):

    def testHelloWorld(self):
        pq = PriorityQueue()
        print(pq.vector)
        self.assertEqual("Hello", pq.helloWorld())

if __name__ == '__main__':
    unittest.main()
