import random

from fit import combine_conflict_masks


def two_point_crossover_timetable(parent1, parent2):
    crossover_point1 = random.randint(1, len(parent1) - 2)
    crossover_point2 = random.randint(crossover_point1 + 1, len(parent1) - 1)

    # Swap the parts between the two crossover points
    child1 = parent1[:crossover_point1] + parent2[crossover_point1:crossover_point2] + parent1[crossover_point2:]
    child2 = parent2[:crossover_point1] + parent1[crossover_point1:crossover_point2] + parent2[crossover_point2:]

    return child1, child2


def crossover_with_mask(parent1, parent2):
    conflict_mask = combine_conflict_masks(parent1)
    child1, child2 = parent1[:], parent2[:]  # Create copies of parents

    for i in range(len(conflict_mask)):
        if conflict_mask[i] == 1:  # Only swap conflicted genes
            child1[i], child2[i] = child2[i], child1[i]

    return child1, child2