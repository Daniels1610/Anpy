import numpy as np

def random_selection(objects:np.ndarray, sum_pi:np.ndarray):
    for _ in range(len(objects)):
        x = np.random.uniform()
        for j in range(len(sum_pi)):
            if sum_pi[j] > x: return objects[j]; 
            else: continue

def random_index_selection(objects:np.ndarray, sum_pi:np.ndarray):
    for _ in range(len(objects)):
        x = np.random.uniform()
        for j in range(len(sum_pi)):
            if sum_pi[j] > x: return j; 
            else: continue