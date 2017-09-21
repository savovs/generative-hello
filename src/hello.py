from difflib import SequenceMatcher
from random import randint, random
from pprint import pprint

GENES = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!."
TARGET = "Hello World!"

def randomCharFromString(string):
	return string[randint(0, len(string) - 1)]

def randomStringFromString(string, length):
	result = ''
	for i in range(length - 1):
		result += randomCharFromString(string)

	return result

# Fitness
def similarityRatioBetween(a, b):
	return SequenceMatcher(None, a, b).ratio()

# Seed Population
population = []
for i in range(10):
	string = randomStringFromString(GENES, len(TARGET))
	population.append(
		(string, similarityRatioBetween(string, TARGET))
	)



# TODO Selection

# TODO Mating

# Mutation
def mutateString(string, genes, probability):
	if random() < probability:
		index = randint(0, len(string) - 1)
		return string[:index] + randomCharFromString(genes) + string[index + 1:]

	return string

pprint(population)