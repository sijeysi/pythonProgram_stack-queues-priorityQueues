from heapq import heappush

fruits = []

heappush(fruits, "orange")
heappush(fruits, "apple")
heappush(fruits, "banana")

print(fruits)   # Output: ['apple', 'orange', 'banana']

from heapq import heappop
heappop(fruits) # Popping/removing the first element
print(fruits)   # Output: ['banana', 'orange']