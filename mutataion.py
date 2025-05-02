import random
def mutation (individual):
    # Select a random gene to mutate
    gene_to_mutate = random.randint(0, len(individual) - 1)
    # Mutate the gene or Chromosome
    individual[gene_to_mutate] = random.randint(0, 1)
    return individual
