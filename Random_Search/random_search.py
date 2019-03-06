from random import random,seed
#function to optimize
def objective_function(vector):
	sum=0
	for x in vector:
		sum+=(x**2)
	return sum

def optimize(best,search_space,max_iter,obj_func):
	bounds = len(search_space)
	for i in range(max_iter):
		#Random chosen candidate for prameter space
		candidate = [search_space[d][0] + random()*(search_space[d][1] - search_space[d][0]) for d in range(bounds)]
		f_target = obj_func(candidate)
		if f_target < best:
			best = f_target
	return best
#Example

#Settings
search_space = [[-5,5],[-5,5]]
max_iter = 10000000
starting_point = 0.005
seed(1)
print(optimize(starting_point,search_space,max_iter,objective_function))

