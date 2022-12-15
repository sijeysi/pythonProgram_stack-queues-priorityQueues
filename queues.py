from collections import deque
from heapq import heappop, heappush

# A class that will delegate the enqueue and dequeue operations to dequeue.append() and dequeue.popleft()
class Queue():
    # Making the class iterable and able to report its length and accept initial elements
    def __init__(self, *elements):
        self.__elements = deque(elements)

    def __len__(self):
        return len(self.__elements)

    def __iter__(self):
        while len(self) > 0:
            yield self.dequeue()
    
    def enqueue(self, element):
        self.__elements.append(element)

    def dequeue(self):
        return self.__elements.popleft()

# A class using inheritance and override the .dequeue() method to remove elements from the top of the stack
class Stack(Queue):
    def dequeue(self):
        return self._elements.pop()

# class PriorityQueue
class PriorityQueue:
    def __init__(self):
        self._elements = []

    def enqueue_with_priority(self, priority, value):
        heappush(self._elements, (priority, value))

    def dequeue(self):
        return heappop(self._elements)[1]