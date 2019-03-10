# Stochastic_Algorithms 
 Algorithms that rely on random variables.These algorithms are predominately global optimization
 algorithms and metaheuristics.
 
 ---
 
 ### Random Search:
 Random Search sample solutions from across the entire search space using a uniform probability distribution.
 It's  derivative-free which means it can be used for non-continuous function too.
 

 
### Adaptive Random Search :
The Strategy of the Adaptive Step Size Random Search algorithm is to trial a larger step in each iteration and adopt the larger step if it results in an improvement. Very large step sizes are trialled in the same manner although with a much lower frequency. This strategy of preferring large moves is intended to allow the technique to escape local optima.
The Adaptive Random Search algorithm was designed to address the limitations of the fixed step size in the Creeping Random Search algorithm and the naive step size in random search.


### Stochastic hill climbing:
The strategy of the Stochastic Hill Climbing algorithm is iterate the process of randomly selecting a neighbor for a candidate solution and only accept it if it results in an improvement

It was proposed to address the limitations of __deterministic hill climbing techniques__(that were likely to get stuck in local optima due to their greedy acceptance of neighboring moves.):

* __simple hill climbing:__ It examines the neighboring one by one and selects the first neighbor which optimizes the current cost as next state
* __Steepest-Ascent Hill Climbing:__ It first examines all the neighbors and then selects the closest solution to the optimal state as next.
