from queues import Queue

fifo = Queue("1st", "2nd", "3rd")

print(len(fifo))    # Output: 3

for element in fifo:
    print(element)
# Output:
# 1st 
# 2nd
# 3rd

print(len(fifo))    # Output: 0