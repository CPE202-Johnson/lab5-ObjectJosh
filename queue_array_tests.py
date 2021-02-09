import unittest
from queue_array import Queue
#from queue_linked import Queue

# Testing for lab1
class TestLab1(unittest.TestCase):
    # Trivial test to ensure method names and parameters are correct
    def test_queue(self):
        '''Trivial test to ensure method names and parameters are correct'''
        q = Queue(5)
        q.is_empty()
        q.is_full()
        q.enqueue('thing')
        q.dequeue()
        q.size()

        n = Queue(5)
        n.enqueue(1)
        n.enqueue(2)
        n.enqueue(3)
        n.enqueue(4)
        n.enqueue(5)
        # test: check if full
        self.assertTrue(n.is_full())
        # test: check if empty
        self.assertFalse(n.is_empty())
        # test: check the size
        self.assertEqual(n.size(), 5)
        # test: enqueue when full
        with self.assertRaises(IndexError):
            n.enqueue(6)
        # test: dequeueing
        self.assertEqual(n.dequeue(), 1)
        # test: check size
        self.assertEqual(n.size(), 4)
        # test: dequeueing
        self.assertEqual(n.dequeue(), 2)
        # test: dequeueing
        self.assertEqual(n.dequeue(), 3)
        # test: dequeueing
        self.assertEqual(n.dequeue(), 4)
        # test: check size
        self.assertEqual(n.size(), 1)
        # test: dequeueing
        self.assertEqual(n.dequeue(), 5)
        # test: dequeue when already empty
        with self.assertRaises(IndexError):
            n.dequeue()
        # test: check if empty
        self.assertTrue(n.is_empty())
        # test: check if full
        self.assertFalse(n.is_full())

if __name__ == '__main__': 
    unittest.main()
