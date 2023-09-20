import time

with open('./inputs/Entrada-800.txt', 'r') as file:
	lines = file.readlines()
	input800 = [int(line.strip()) for line in lines]

with open('./inputs/Entrada-8000.txt', 'r') as file:
	lines = file.readlines()
	input8000 = [int(line.strip()) for line in lines]

with open('./inputs/Entrada-80000.txt', 'r') as file:
	lines = file.readlines()
	input80000 = [int(line.strip()) for line in lines]


# It makes 2 for loops, the first one [i] is to iterate over the list, the second one [j] is to compare the current element with the next one, if the current element is greater than the next one, it swaps them.
def bubble(input : list[int])-> {list[int],int}:
	now = time.time()
	for i in range(len(input)):
		for j in range(len(input)-1):
			if input[j] > input[j+1]:
				input[j], input[j+1] = input[j+1], input[j]
	return {'sortedList': input, 'time': time.time() - now}

# It makes 2 for loops, the first one [i] is to iterate over the list, the second one [j] is to find the minimum value in the rest of the list, when the second loop ends, it swaps the current element [i] with the minimum value [min].
def selection(input : list[int])-> {list[int],int}:
	now = time.time()
	for i in range(len(input)):
		min = i
		for j in range(i+1, len(input)):
			if input[min] > input[j]:
				min = j
		input[i], input[min] = input[min], input[i]
	return {'sortedList': input, 'time': time.time() - now}

