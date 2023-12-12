# ACO Algorithm: Object Non-Replacement Variant
# Single Neighborhood execution
import numpy as np
from anpy.support import random_index_selection
from anpy.Neighborhood import Neighborhood

# Actual Execution has to be with:
# 10 ANTS | 100 ITERATIONS
ANTS_NUMS = 10
KNAPSACK_CAPACITY = 750 # Total Knapsack load capacity

def aco():
    N = setup_neighborhood()
    i = 0
    while i < len(N.ants):
        random_ant = N.ants[np.random.randint(0,len(N.ants))]
        Vc = KNAPSACK_CAPACITY; selected_idxs = []
        objects_probs = N.get_object_prob()
        while not random_ant.hasWorked:
            object_idx = random_index_selection(N.weights, objects_probs)
            while object_idx in selected_idxs: object_idx = random_index_selection(N.weights, objects_probs)
            selected_idxs.append(object_idx)
            obj_weight = N.weights[object_idx]
            if Vc - obj_weight <= 0: random_ant.hasWorked = True; i += 1;break
            random_ant.add_weight_and_value(obj_weight, N.values[object_idx])
            Vc -= obj_weight
    return N

def display_ants(N:Neighborhood):
    for ant in N.ants:
        print(f"Ant ID: {ant.id} | PS: {ant.s} | Z: {ant.z} | V: {sum(ant.s)}")
        
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
    N1 = aco()
    N1.display_ants()