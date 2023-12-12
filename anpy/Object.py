from typing import Union

class Object:
    def __init__(self, value:Union[float, int], weight:Union[float, int], pheromone:float):
        self.value = value
        self.weight = weight
        self.pheromone = pheromone
