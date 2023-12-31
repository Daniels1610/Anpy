# Anpy 🐜

**Anpy** is a python object oriented library that implements one main Ant Colonization Optimization (ACO) algorithm 
and 2 variants to solve the 0/1 Knapsack Problem. This approach aims to model the actual behaviour of an Ant Colony
through the use of entities such as Ant, Object and Neighborhood.

**ACO Algorithms:**

**_aco.py_** : Neighborhood is compiled to a new state every time an Ant selects an object. 
           Pheromone update and evaporation mechanisms are applied in order to avoid a
           rapid convergence to a locally optimal solution. Heuristics as μ are used
           to get the ratio of object's weights and values. Parameters such as α and
           β are included when calculating the object's probabilities. The maximum 
           recorded result for Z (Profit) was 1458.
          
**_aco_rep.py:_** Allows ants to select the same object multiple times to his partial solution.
              Due to object replacement, this particular variant yields the highest Z. 
              The maximum recorded result for Z (Profit) was 1485.

**_aco_norep.py:_** Allows ants to select an object once to his partial solution due to 
                non-replaceable objects. The maximum recorded result for Z (Profit) was 1458.

It should be mentioned that both aco_rep.py and aco_no_rep.py doesn't follow the pheromone
principles as usual, because the object's probabilities are static, and just get calculated
once in all their execution.

For that reason, the main version of the algoritm aco.py, is a better option that doesn't rely
heavily on the selections randomness due to their pheromone adjustments.

Main ACO algorithm was based of this article:
Schiff, K. (2013) _Ant Colony Optimization for the 0-1 Knapsack Problem_ .

You can download the PDF [here](https://www.ejournals.eu/Czasopismo-Techniczne/2013/Automatyka-Zeszyt-3-AC-(11)-2013/art/3594)

To get this repository, it is recommended to use _git clone_ command:
```bash
git clone https://github.com/Daniels1610/Anpy.git
```
Or use the option "Download ZIP" on the repository's green button labeled as "code". 

If you experience problems regarding filename size, employ this command **git config --global core.longpaths true** to allow more characters in files and directories names.
