# Anpy 🐜

**Anpy** is a python object oriented library that implements one main Ant Colonization Optimization (ACO) algorithm 
and 2 variants to solve the 0/1 Knapsack Problem. This approach aims to model the actual behaviour of an Ant Colony
through the use of entities such as Ant, Object and Neighborhood.

**ACO Algorithms:**

_aco.py_ : Neighborhood is compiled to a new state every time an Ant selects an object. 
           Pheromone update and evaporation mechanisms are applied in order to avoid a
           rapid convergence to a locally optimal solution. Heuristics as μ are used
           to get the ratio of object's weights and values. Parameters such as α and
           β are included when calculating the object's probabilities.
          
_aco_rep.py:_ Allow ants to select a same object multiple times to his partial solution
              due to object replacement. Max result registered was Z (Profit): 1485 


_aco_norep.py:_ Allow ants to select an object once to his partial solution due to 
                non-replaceable objects. Max result registered was Z (Profit): 1458

It should be mentioned that both aco_rep.py and aco_no_rep.py doesn't follow the pheromone
principles as normal, because the object's probabilities are static, and just got calculated
one in all the execution.

For that reason, the main version of the algoritm aco.py, is a better option that doesn't rely
heavily on random selections due to their pheromone adjustments.
