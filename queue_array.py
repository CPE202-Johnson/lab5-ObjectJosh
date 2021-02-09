# Queue Implements an array-based, efficient first-in first-out Abstract Data Type using a Python array (faked using a List)
class Queue:
    '''Implements an array-based, efficient first-in first-out Abstract Data Type 
       using a Python array (faked using a List)'''
    
    # Creates an empty Queue with a capacity
    # capacity is an int
    def __init__(self, capacity):
        '''Creates an empty Queue with a capacity'''
        self.capacity = capacity
        self.items = [None] * capacity
        self.num_items = 0
        self.head = self.tail = 0

    # Returns True if the Queue is empty, and False otherwise
    def is_empty(self):
        '''Returns True if the Queue is empty, and False otherwise
           MUST have O(1) performance'''
        return self.num_items == 0

    # Returns True if the Queue is full, and False otherwise
    def is_full(self):
        '''Returns True if the Queue is full, and False otherwise
           MUST have O(1) performance'''
        return self.num_items == self.capacity

    # If Queue is not full, enqueues (adds) item to Queue. If Queue is full when enqueue is attempted, raises IndexError
    # item can be any data type
    def enqueue(self, item):
        '''If Queue is not full, enqueues (adds) item to Queue 
           If Queue is full when enqueue is attempted, raises IndexError
           MUST have O(1) performance'''
        if self.is_full():
            raise IndexError
        # Before:
        '''
        if self.is_empty():
            self.items[self.tail] = item
        else:
            self.tail = (self.tail + 1) % self.capacity
            self.items[self.tail] = item
        self.num_items += 1
        '''
        # After:
        self.items[self.tail] = item
        self.tail = (self.tail + 1) % self.capacity
        self.num_items += 1

    # If Queue is not empty, dequeues (removes) item from Queue and returns item. If Queue is empty when dequeue is attempted, raises IndexError
    def dequeue(self):
        '''If Queue is not empty, dequeues (removes) item from Queue and returns item.
           If Queue is empty when dequeue is attempted, raises IndexError
           MUST have O(1) performance'''
        if self.is_empty():
            raise IndexError
        removed_item = self.items[self.head]
        self.head = (self.head + 1) % self.capacity
        self.num_items -= 1
        return removed_item

    # Returns the number of elements currently in the Queue, not the capacity
    def size(self):
        '''Returns the number of elements currently in the Queue, not the capacity
           MUST have O(1) performance'''
        return self.num_items
