from dataclasses import dataclass

@dataclass
class Message:
    event: str 

wipers = Message("Winshield wipers turned on")
hazard_lights = Message("Hazard loghts turned on")

wipers < hazard_lights  # Output: TypeError: '<' not supported between instances of 'Message' and 'Message'

...

messages = PriorityQueue()

messages.enqueue_with_priority(CRITICAL, wipers)
messages.enqueue_with_priority(IMPORTANT, hazard_lights)

messages.enqueue_with_priority(CRITICAL, Message("ABS engaged"))

# Output: TypeError: '<' not supported between instances of 'Message' and 'Message'