# A class that will delegate the enqueue and dequeue operations to dequeue.append() and dequeue.popleft()
from collections import deque

class Queue:
    def __init__(self):
        self.__elements = deque()
    
    def enqueue(self, element):
        self.__elements.append(element)

    def dequeque(self):
        return self.__elements.popleft()

# An iterable class and will able to report its length and accept initial elements
from collections import deque