from queues import Queue

fifo = Queue()

fifo.enqueue("1st")
fifo.enqueue("2nd")
fifo.enqueue("3rd")

fifo.dequeque()
'1st'
fifo.dequeque()
'2nd'
fifo.dequeque()
'3rd'