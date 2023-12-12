import numpy as np
from anpy.Ant import Ant
from typing import Union
from anpy.AntFactory import AntFactory
from anpy.Object import Object
from anpy.ObjectFactory import ObjectFactory
from resources.parse_json import parse_json

dirs = parse_json("resources/dirs.json")
nor = parse_json("resources/nor.json")

class Neighborhood():
    N:list
    current_N: list
    weights:np.ndarray # Weights (N): Set of Available Objects which can be loaded into the knapsack
    values:np.ndarray # Profits (Z): Set of Objects gains
    ants:np.ndarray # Neighborhood's Ants
    nor:dict

    def __init__(self, ant_nums:int):
        self.N = []
        self.current_N = []
        self.weights = np.array([])
        self.values = np.array([])
        self.set_ants(ant_nums)
        self.nor = nor.copy()
        
    # GETTERS
    def get_object_probs(self, N:np.ndarray) -> np.ndarray:
        mu = self.get_mu(); pj = []
        wish_sum = np.sum([(N[i].pheromone ** self.nor['ALPHA']) * (mu[i] ** self.nor['BETA']) for i in range(len(N))])
        for i in range(len(N)):
            pj.append(((N[i].pheromone ** self.nor['ALPHA']) * (mu[i] ** self.nor['BETA'])) / wish_sum)
        return np.cumsum(np.array(pj))

    def get_object_prob(self) -> np.ndarray:
        len_objects = self.weights.size
        return np.cumsum(np.array([self.nor['PHEROMONE'] / len_objects  for _ in range(len_objects)])) 

    def get_available_objects(self, Vc:Union[float, int]) -> np.ndarray:
        i = 0
        while (len(self.N) > 0):
            if i == len(self.N): return self.N
            if Vc - self.N[i].weight <= 0: self.N.pop(self.N.index(self.N[i]))
            else: i += 1
        return self.N
    
    def get_mu(self) -> np.ndarray:
        assert self.values.size > 0 and self.weights.size > 0
        return self.values / (self.weights ** 2)
    
    def get_neighborhood(self):
        return self.N
    
    def get_current_neighborhood(self):
        return self.current_N

    # SETTERS
    def set_weights(self, filename:str):
        self.weights = np.loadtxt(f"{dirs['DATASETS_DIR']}{filename}", dtype=np.int32)

    def set_profits(self, filename:str):
        self.values = np.loadtxt(f"{dirs['DATASETS_DIR']}{filename}", dtype=np.int32)

    def set_neighborhood(self, N):
        self.N = N
        self.current_N = N.copy()

    def set_ants(self, ants_num):
        self.ants = np.array([AntFactory.create(i) for i in range(1, ants_num+1)])
    
    # EXTRA METHODS
    def generate_neighborhood(self):
        return [ObjectFactory.create(self.values[i],self.weights[i],self.nor['PHEROMONE']) for i in range(self.weights.size)]

    def update_N(self, object:Object):
        for i in range(len(self.N)):
            if self.N[i].weight == object.weight: 
                self.N.pop(i)
                return self.N
            else: continue

    def evaporation_mechanism(self):
        self.nor['PHEROMONE'] *= self.nor['EVA_RATE']

    def update_pheromones(self, current_solution:Ant, best_solution:Ant):
        delta_pheromones = 1 / (1 +(best_solution.z-current_solution.z / best_solution.z))
        best_weights = [np.where(self.weights == weight)[0][0] for weight in best_solution.s]
        for idx in best_weights:
            self.current_N[idx].pheromone += delta_pheromones
        return self.current_N
    
    def display_ants(self):
        for ant in self.ants:
            print(f"Ant ID: {ant.id} | S: {ant.s} | Z: {ant.z} | V: {sum(ant.s)}")