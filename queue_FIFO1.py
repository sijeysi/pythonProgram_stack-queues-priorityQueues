from queues import Queue

fifo = Queue("1st", "2nd", "3rd")

print(len(fifo))
# Expected Output
# 3

for element in fifo:
    print(element)
# Expected Output
# 1st 
# 2nd
# 3rd

print(len(fifo))
# Expected Output
# 0