from queues import Queue

fifo = Queue()

fifo.enqueue("1st")
fifo.enqueue("2nd")
fifo.enqueue("3rd")

print(fifo.dequeque())
print(fifo.dequeque())
print(fifo.dequeque())

# Expected Output
# 1st
# 2nd 
# 3rd