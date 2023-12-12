# ACO Algorithm: Object Non-Replacement and Pheromone Update Variant
# Single Neighborhood execution

import numpy as np
from anpy.support import random_selection
from anpy.Neighborhood import Neighborhood
from anpy.AntFactory import AntFactory

# Actual Execution has to be with:
# 10 ANTS | 100 ITERATIONS
ITERATIONS = 100
ANTS_NUMS = 10
KNAPSACK_CAPACITY = 750 # Total Knapsack load capacity

def aco():
    global_best_ant = AntFactory.create(0)
    N = setup_neighborhood()
    for _ in range(1, ITERATIONS+1):
        iter_best_ant = AntFactory.create(0)
        i = 0
        N.set_ants(ANTS_NUMS)
        while i < len(N.ants):
            random_ant = N.ants[np.random.randint(0,len(N.ants))]
            Vc = KNAPSACK_CAPACITY; 
            N.set_neighborhood(N.current_N)
            while not random_ant.hasWorked:
                available_objects = N.get_available_objects(Vc)
                if len(available_objects) == 0: random_ant.hasWorked = True; i += 1; break
                objects_probs = N.get_object_probs(available_objects)
                object = random_selection(available_objects, objects_probs)
                random_ant.add_object(object)
                N.update_N(object)
                Vc -= object.weight
            if random_ant.z > iter_best_ant.z: iter_best_ant = random_ant
        if iter_best_ant.z > global_best_ant.z: global_best_ant = iter_best_ant
        print(f"BEST ITER ANT: ID: {iter_best_ant.id} | S: {iter_best_ant.s} | Z: {iter_best_ant.z} | V: {sum(iter_best_ant.s)}")
        N.evaporation_mechanism()
        N.set_neighborhood(N.update_pheromones(random_ant, global_best_ant))
    return global_best_ant   

def setup_neighborhood():
    # Create Neighborhood
    N1 = Neighborhood(ANTS_NUMS)
    
    # Set Neighborhood's Weights & Profits
    N1.set_weights("weights.txt")
    N1.set_profits("profits.txt")
    N = N1.generate_neighborhood()
    N1.set_neighborhood(N)
    return N1

if __name__ == "__main__":    
    # Get solutions from each cycle
    best_execution_ant = aco()
    print(f"BEST ANT ID: {best_execution_ant.id} | S: {best_execution_ant.s} | Z: {best_execution_ant.z} | V: {sum(best_execution_ant.s)}")