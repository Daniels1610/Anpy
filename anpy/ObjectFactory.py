from anpy.Object import Object
from typing import Union

class ObjectFactory():
    @staticmethod
    def create(value:Union[float,int], weight:Union[float,int], pheromone:float) -> Object:
        return Object(value, weight, pheromone)