from random import random,seed

def objective_function(vector):
	sum=0
	for x in vector:
		sum+=(x**2)
	return sum

def candidates(min,max):
	return min+ random()*(max-min)

def starting_candidate(bounds):
	vector = []
	for i in range(len(bounds)):
		vector.append(candidates(bounds[i][0],bounds[i][1]))
	return vector

def take_step(bounds,current,step_size):
	position = []
	for i in range(len(current)):
		min_ = max([bounds[i][0],current[i]-step_size])
		max_ = min([bounds[i][1],current[i]+step_size])
		position.append(candidates(min_,max_))
	return position

def large_step_size(iter_,step_size,s_factor,l_factor,iter_mult):
	if iter_ > 0 and (iter_%iter_mult)==0:
		return step_size * l_factor
	else:
		return step_size * s_factor

def take_steps(bounds,current,step_size,big_step_size):
	step = {}
	big_step = {}
	step['vector'] = take_step(bounds,current,step_size)
	step['cost'] = objective_function(step['vector'])
	big_step['vector'] = take_step(bounds,current,big_step_size)
	big_step['cost'] = objective_function(big_step['vector'])
	return step,big_step

def optimize(max_iteration,bounds,init_factor,s_factor,l_factor,iter_mult,max_no_improvement):
	step_size = (bounds[0][1]  - bounds[0][0])* init_factor
	current , count = {},0
	current['vector'] = starting_candidate(bounds)
	current['cost'] = objective_function(current['vector'])
	for i in range(max_iteration):
		big_step_size = large_step_size(i,step_size,s_factor,l_factor,iter_mult)
		step,big_step = take_steps(bounds,current['vector'],step_size,big_step_size)

		if step['cost'] < current['cost'] or big_step['cost'] < current['cost']:
			if big_step['cost'] < step['cost']:
				step_size,current = big_step_size,big_step	
			else:
				current = step
			count = 0
		else:
			count+=1
			
			if count >= max_no_improvement:
				count,step_size = 0, (step_size/s_factor)
		print('Iteration : %d , Best = %f , Step_size = %f'%((i+1),current['cost'],step_size))
	return current
 

#Settings
poblem_size = 2
bounds = [[-5,5],[-5,5]]
max_iter = 10000
init_factor = 0.05
s_factor = 0.3
l_factor = 1
iter_mult = 1 #adjust the step_size
max_no_impr = 30 #adjust if there is improvement or not


seed(1)
best = optimize(max_iter, bounds, init_factor, s_factor, l_factor, iter_mult, max_no_impr)
print('Done.\nBest Solution: cost = {} , vector = {}'.format(best['cost'],best['vector']))