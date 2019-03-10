from random import random,randint
from time import sleep
def one_max(mutant):
	sum = 0
	for i in mutant:
		if i == '1':
			sum+=1
		else:
			sum+=0
	return sum

def random_bitstring(num_bits):
	bits = []
	for i in range(num_bits):
		if random() < .5:
			bits.append("1")
		else:
			bits.append("0")
	return bits
def random_neighbor(bitstring):
	mutant = bitstring
	position = randint(0,len(bitstring)-1)
	if mutant[position] == '1':
		mutant[position] = '0'
	else:
		mutant[position] = '1'

	return mutant

def optimize(max_iteration,num_bits):
	current = {}
	current['mutant'] = random_bitstring(num_bits)
	current['cost'] = one_max(current['mutant'])

	for i in range(max_iteration):
		neighbor = {}
		neighbor['mutant'] = random_neighbor(current['mutant'])
		neighbor['cost'] = one_max(neighbor['mutant'])

		if neighbor['cost']>=current['cost']:
			print(neighbor['mutant'])
			current  = neighbor
		if current['cost'] == num_bits:
			break
		sleep(0.3)

	print('Done')
	return current

#SETTINGS
max_iter = 100
num_bits = 5

print(optimize(max_iter,num_bits))



