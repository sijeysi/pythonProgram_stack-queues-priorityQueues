from queues import PriorityQueue

CRITICAL = 3
IMPORTANT = 2
NEUTRAL = 1

messages = PriorityQueue()
messages.enqueue_with_priority(IMPORTANT, "Winshield wipers turned on")
messages.enqueue_with_priority(NEUTRAL, "Radio station turned in")
messages.enqueue_with_priority(CRITICAL, "Brake pedal depressed")
messages.enqueue_with_priority(IMPORTANT, "Hazard lights turned on")

print(messages.dequeue()) # Output: (1, 'Radio station turned in')

print(messages.dequeue())
print(messages.dequeue())
print(messages.dequeue())
print(messages.dequeue())