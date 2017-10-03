import random
from operator import itemgetter
from pprint import pprint

GENES = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!."
TARGET = "Hello World!"

# Utility functions
def randomCharFromString(string):
	return string[random.randint(0, len(string) - 1)]


def randomStringFromString(string, length):
	result = ''
	for i in range(length):
		result += randomCharFromString(string)

	return result

# Fitness
def asciiStringDistance(a, b):
	distanceSum = 0
	for charA, charB in zip(a, b):
		distanceSum += abs(ord(charA) - ord(charB))

	return distanceSum

# 2 Tournaments, best of each become parents
def tournament(inputSet):
	first = random.choice(tuple(inputSet))
	second = random.choice(tuple(inputSet))

	if first[1] < second[1]:
		return first
	else:
		return second

def mutateString(string, genes = GENES, probability = 0.15):
	if random.random() < probability:
		index = random.randint(0, len(string) - 1)
		return string[:index] + randomCharFromString(genes) + string[index + 1:]

	return string

# Crossover two tuples (string, fitness) returning tuple of tuples:
def crossover(parent1, parent2, noCrossProbability = 0.05, fitnessFunction = asciiStringDistance):
	if random.random() < noCrossProbability:
		return (parent1, parent2)

	randomIndex = random.randint(0, len(parent1[0]) - 1)

	newString1 = mutateString(
		''.join((parent1[0][:randomIndex], parent2[0][randomIndex:]))
	)

	newString2 = mutateString(
		''.join((parent2[0][:randomIndex], parent1[0][randomIndex:]))
	)

	return (
		(newString1, fitnessFunction(newString1, TARGET)),
		(newString2, fitnessFunction(newString2, TARGET)),
	)

def generatePopulation(old = set([]), currentGeneration = 0, howManyGenerations = 50):
	new = set([])

	fittest = min(old, key = itemgetter(1))
	print('Generation {}, fittest: {}'.format(currentGeneration, fittest))

	if fittest[0] == TARGET:
		print('Got em!')
		return old

	if currentGeneration < howManyGenerations:
		while len(new) < len(old):
			children = crossover(tournament(old), tournament(old))
			for child in children:
				new.add(child)

		return generatePopulation(new, currentGeneration + 1, howManyGenerations)
	return old


# Seed Population with tuples in this shape: (string, asciiStringDistance)
population = set([])

for i in range(500):
	string = randomStringFromString(GENES, len(TARGET))
	population.add(
		(string, asciiStringDistance(string, TARGET))
	)

result = generatePopulation(population, howManyGenerations = 500)
