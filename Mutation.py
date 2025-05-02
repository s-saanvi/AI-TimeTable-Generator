import random
from Data import Courses, lecturers, time_slots, halls


def mutate_timetable(individual):
    """
    Mutate a timetable by randomly changing one of its entries.
    """
    mutated = individual.copy()
    index = random.randint(0, len(individual) - 1)  # Pick a random slot
    course = individual[index].split("-")[0]
    new_slot = f"{course}-{random.choice(lecturers)}-{random.choice(time_slots)}-{random.choice(halls)}"
    mutated[index] = new_slot  # Randomly modify the slot
    return mutated

