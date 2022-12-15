from dataclasses import dataclass

@dataclass
class Message:
    event: str 

wipers = Message("Winshield wipers turned on")
hazard_lights = Message("Hazard loghts turned on")

wipers < hazard_lights  # Output: TypeError: '<' not supported between instances of 'Message' and 'Message'
