# ACO Algorithm executed by runACO.sh Script
import sys
import numpy as np
from anpy.Ant import Ant
import pandas as pd
from anpy.support import random_index_selection
from anpy.Neighborhood import Neighborhood

ITERATIONS = 1000
ANTS_NUMS = 100
KNAPSACK_CAPACITY = 750 # Total Knapsack load capacity

best_ant_iteration = pd.DataFrame(columns=
    ['Iteration',
    'Ant ID',
    'Partial Solution (S)',
    'Profit (Z)',
    'Capacity (V)'])
worst_ant_iteration = pd.DataFrame(columns=
    ['Iteration',
    'Ant ID',
    'Partial Solution (S)',
    'Profit (Z)',
    'Capacity (V)'])
best_ant_run = pd.DataFrame(columns=
    ['Ant ID',
    'Partial Solution (S)',
    'Profit (Z)',
    'Capacity (V)'])
worst_ant_run = pd.DataFrame(columns=
    ['Ant ID',
    'Partial Solution (S)',
    'Profit (Z)',
    'Capacity (V)'])

def setup_neighborhood() -> Neighborhood:
    # Create Neighborhood
    N1 = Neighborhood(ANTS_NUMS)
    
    # Set Neighborhood's Weights & Profits
    N1.set_weights("weights.txt")
    N1.set_profits("profits.txt")
    N = N1.generate_neighborhood()
    N1.set_neighborhood(N) 
    return N1   

def get_best_ant_iter(iteration:int, ant:Ant):
    best_ant_iteration.loc[iteration] = [iteration,
        ant.id,                
        ant.s,
        ant.z,
        np.sum(ant.s)]
    
def get_worst_ant_iter(iteration:int, ant:Ant):
    worst_ant_iteration.loc[iteration] = [iteration,
        ant.id,                
        ant.s,
        ant.z,
        np.sum(ant.s)]

def aco():
    for iter in range(1, ITERATIONS+1):
        N = setup_neighborhood()
        i = 0
        objects_probs = N.get_object_prob()
        while i < len(N.ants):
            random_ant = N.ants[np.random.randint(0,len(N.ants))]
            Vc = KNAPSACK_CAPACITY
            while not random_ant.hasWorked:
                object_idx = random_index_selection(N.weights, objects_probs)
                obj_weight = N.weights[object_idx]
                if Vc - obj_weight <= 0: random_ant.hasWorked = True;i += 1;break
                random_ant.add_weight_and_value(obj_weight, N.values[object_idx])
                Vc -= obj_weight
        ants_profits = [ant.z for ant in N.ants]    
        get_best_ant_iter(iter, N.ants[np.argmax(ants_profits)])
        get_worst_ant_iter(iter, N.ants[np.argmin(ants_profits)])
    best_ant = best_ant_iteration.loc[np.argmax(best_ant_iteration['Profit (Z)'])+1]
    worst_ant = worst_ant_iteration.loc[np.argmin(worst_ant_iteration['Profit (Z)'])+1]
    return f"""
{sys.argv[1]},{best_ant.loc['Ant ID']},{best_ant.loc['Partial Solution (S)']},{best_ant.loc['Profit (Z)']}, {best_ant.loc['Capacity (V)']}
{sys.argv[1]},{worst_ant.loc['Ant ID']},{worst_ant.loc['Partial Solution (S)']},{worst_ant.loc['Profit (Z)']}, {worst_ant.loc['Capacity (V)']}
    """

if __name__ == "__main__":
    print(aco())