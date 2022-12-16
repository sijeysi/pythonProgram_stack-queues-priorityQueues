from queues import Queue

fifo = Queue()

fifo.enqueue("1st")
fifo.enqueue("2nd")
fifo.enqueue("3rd")

print(fifo.dequeue())   # Output: 1st
print(fifo.dequeue())   # Output: 2nd
print(fifo.dequeue())   # Output: 3rd