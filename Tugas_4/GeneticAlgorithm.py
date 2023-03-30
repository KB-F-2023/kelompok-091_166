import time
import random

# Constants
BOARD_SIZE = 8
POPULATION_SIZE = 100
MUTATION_RATE = 1
MAX_GENERATIONS = 100

def initialize_population(population_size):
    # Initialize a population of random chromosomes
    population = []
    for i in range(population_size):
        chromosome = list(range(BOARD_SIZE))
        random.shuffle(chromosome)
        population.append(chromosome)
    return population

def evaluate_fitness(chromosome):
    # Calculate the number of non-attacking queen pairs in the chromosome
    non_attacking_pairs = 0
    for i in range(BOARD_SIZE):
        for j in range(i+1, BOARD_SIZE):
            if chromosome[i] != chromosome[j] and abs(chromosome[i] - chromosome[j]) != j - i:
                non_attacking_pairs += 1
    return non_attacking_pairs

def tournament_selection(population, tournament_size=2):
    # Select a parent chromosome using tournament selection
    tournament = random.sample(population, tournament_size)
    best_chromosome = min(tournament, key=lambda x: evaluate_fitness(x))
    return best_chromosome

def crossover(parent1, parent2):
    # Perform crossover between two parent chromosomes
    crossover_point = random.randint(0, BOARD_SIZE-1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

def mutate(chromosome):
    # Mutate the chromosome by randomly swapping two genes
    if random.random() < MUTATION_RATE:
        i, j = random.sample(range(BOARD_SIZE), 2)
        chromosome[i], chromosome[j] = chromosome[j], chromosome[i]
    return chromosome

def replace_worst(population, offspring):
    # Replace the worst chromosome in the population with the offspring chromosome using elitism
    worst_chromosome = min(population, key=evaluate_fitness)
    population.remove(worst_chromosome)
    population.append(offspring)
    return population

def genetic_algorithm(population_size, max_generations):
    random.seed(time.time())

    # Initialize the population
    population = initialize_population(population_size)

    # Initialize the best chromosome and its fitness
    best_chromosome = None
    best_fitness = 0
    best_chromosome_eachgen = []

    # Iterate over the generations
    for generation in range(max_generations):
        # Create the next generation
        next_generation = []
        for i in range(population_size):
            # Select two parent chromosomes
            parent1 = tournament_selection(population)
            parent2 = tournament_selection(population)

            # Create two child chromosomes
            child1, child2 = crossover(parent1, parent2)

            # Mutate the child chromosomes
            child1 = mutate(child1)
            child2 = mutate(child2)

            # Evaluate the fitness of the child chromosomes
            fitness1 = evaluate_fitness(child1)
            fitness2 = evaluate_fitness(child2)

            # Add the child with the better fitness to the next generation
            if fitness1 > fitness2:
                next_generation.append(child1)
                if fitness1 > best_fitness:
                    best_chromosome = child1
                    best_fitness = fitness1
            else:
                next_generation.append(child2)
                if fitness2 > best_fitness:
                    best_chromosome = child2
                    best_fitness = fitness2

        # Replace the population with the next generation
        population = next_generation

        # # Print the best solution so far
        best_chromosome_eachgen.append(best_chromosome)
        # Terminate if the solution is found
        if best_fitness == 28:
            print("Solution found!")
            break

    # Return the best chromosome and its fitness
    return best_chromosome, best_fitness, best_chromosome_eachgen

solution, fitness, myList = genetic_algorithm(population_size=POPULATION_SIZE, max_generations=MAX_GENERATIONS)

while(fitness!=28):
    solution, fitness, myList = genetic_algorithm(population_size=POPULATION_SIZE, max_generations=MAX_GENERATIONS)

if(fitness == 28):
    print(f"Solution: {solution}")
    print(f"Fitness: {fitness}")
    print(f"number of generations : {len(myList)}")
    for i in range(len(myList)) :
        print(myList[i])
for row in range(8):
    # Print out the positions of the queens in this row
    for col in range(8):
        if solution[row] == col:
            print("Q", end=" ")
        else:
            print(".", end=" ")
    print()
