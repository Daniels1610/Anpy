from anpy.Object import Object
from typing import Union
import numpy as np

class Ant():
    s: np.ndarray  # Ant's Set of Solutions that constitutes the objects loaded into the knapsack
    z: Union[float,int] # Ant's Profit
    id: int # Ant's Identifier
    hasWorked: bool # Detects whether the ant has already worked

    def __init__(self, id:int):
        self.s = np.array([], dtype=np.int32)
        self.z = 0
        self.id = id
        self.hasWorked = False

    def add_object(self, object:Object):
        self.s = np.append(self.s, object.weight)
        self.z += object.value

    def add_weight_and_value(self, weight:Union[float,int], value:Union[float,int]):
        self.s = np.append(self.s, weight)
        self.z += value  

    
