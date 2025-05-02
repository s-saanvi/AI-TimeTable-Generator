from collections import defaultdict
from Data import Courses, lecturers, time_slots, halls


# find if lecturer is assigned to more than time slot
def lecturer_timeSlot(individual):
    penalty = 0
    lecturer_time_slot = {}
    for gene in individual:
        course, lecturer, time_slot, hall = gene.split('-')
        if (lecturer, time_slot) in lecturer_time_slot:
            penalty += 10
        else:
            lecturer_time_slot[(lecturer, time_slot)] = course
    return penalty


# find if hall contain more than one slot in the same time
def hall_timeSlot(individual):
    penalty = 0
    hall_time_slot = {}
    for gene in individual:
        course, lecturer, time_slot, hall = gene.split('-')
        if (hall, time_slot) in hall_time_slot:
            penalty += 10
        else:
            hall_time_slot[(hall, time_slot)] = course

    return penalty


def unequal_distribution_penalty(individual):
    """
    Penalize unequal distribution of distinct courses across doctors (lecturers).
    """
    lecturer_course_count = defaultdict(set)  # To count distinct courses assigned to each lecturer

    for gene in individual:
        course, lecturer, time_slot, hall = gene.split('-')
        lecturer_course_count[lecturer].add(course)  # Add the course to the set (unique courses)

    # Compute the distribution balance
    max_courses = max(len(courses) for courses in lecturer_course_count.values())
    min_courses = min(len(courses) for courses in lecturer_course_count.values())

    # If the max number of courses assigned to any lecturer is significantly greater than the min,
    # apply a penalty
    if max_courses - min_courses > 2:  # Adjust the threshold based on preference
        penalty = (max_courses - min_courses) * 5  # Multiply by a factor for severity
    else:
        penalty = 0

    return penalty




def gab(individual):
    """
    Calculate the gap between lectures for each lecturer and apply a fixed penalty of 2.5 for each gap
    larger than 2 hours between consecutive lectures.
    """
    lecturer_time_slots = defaultdict(list)  # To store time slots for each lecturer

    # Extract time slots for each lecturer
    for gene in individual:
        course, lecturer, time_slot, hall = gene.split('-')

        # Extract the integer from the time slot notation (e.g., 'TS1' → 1, 'TS2' → 2)
        time_slot_number = int(time_slot[2:])  # Strip 'TS' and convert to integer

        # Store the time slot number for the lecturer
        lecturer_time_slots[course].append(time_slot_number)

    penalty = 0

    # Iterate over each lecturer's time slots
    for course, time_slots in lecturer_time_slots.items():
        time_slots.sort()  # Sort the time slots for the lecturer

        # Calculate gaps between consecutive time slots
        for i in range(1, len(time_slots)):
            gap = time_slots[i] - time_slots[i - 1]

            # If the gap exceeds 2, apply a fixed penalty of 2.5 points
            if gap > 2:
                penalty += 2.5

    return penalty


def unbalanced_distribution_per_day(individual):
    penalty = 0
    days = ["Sat", "Sun", "Mon", "Tue", "Wed", "Thu"]

    # Create a dictionary to count lectures for each lecturer per day
    daily_lecturer_count = {day: {lecturer: 0 for lecturer in lecturers} for day in days}

    # Populate the daily lecturer count
    for gene in individual:
        # Decode the gene (e.g., 'C1-T1-TS1-R1')
        course, lecturer, time_slot_code, hall = gene.split('-')  # Split the string into components
        time_slot_index = int(time_slot_code[2:]) - 1  # Extract time slot index (e.g., "TS1" -> 0)
        time_slot = time_slots[time_slot_index]  # Get the actual time slot from org_time_slots

        day = time_slot.split()[0]  # Extract the day (e.g., "Sat" from "Sat 8-10")

        # Count the lecture for the given day and lecturer
        if day in daily_lecturer_count:
            daily_lecturer_count[day][lecturer] += 1

    # Calculate penalties for each day
    for day, lecturer_counts in daily_lecturer_count.items():
        total_lectures_on_day = sum(lecturer_counts.values())  # Total lectures assigned on this day
        if len(lecturers) > 0:  # Avoid division by zero
            expected_lectures_per_lecturer = total_lectures_on_day / len(lecturers)
        else:
            expected_lectures_per_lecturer = 0

        # Compute penalty
        for lecturer, count in lecturer_counts.items():
            penalty += abs(count - expected_lectures_per_lecturer)

    return int(penalty)


def total_fitness_score(individual):
    lts = lecturer_timeSlot(individual)
    hts = hall_timeSlot(individual)
    udpd = unbalanced_distribution_per_day(individual)
    udp = unequal_distribution_penalty(individual)
    gb = gab(individual)


    total_score = lts + hts + udpd +udp+gb

    return total_score



# calculate the fitness scores of all population
def fitness_scores(population):
    scr_lst = []
    for ind in population:
        scr_lst.append(total_fitness_score(ind))
    return scr_lst



def inverted_fitness(fitness_scores):
    # Invert the fitness values to favor individuals with lower fitness
    max_fitness = max(fitness_scores)
    inverted_scores = [max_fitness - fitness for fitness in fitness_scores]
    return inverted_scores














def combine_conflict_masks(individual):
    masks=[lecturer_timeSlot_conflicts(individual),hall_timeSlot_conflicts(individual)]
    combined_mask = [0] * len(masks[0])  # Assume all masks have the same length
    for mask in masks:
        combined_mask = [cm | m for cm, m in zip(combined_mask, mask)]
    return combined_mask


def lecturer_timeSlot_conflicts(individual):
    conflict_mask = [0] * len(individual)  # Initialize binary conflict mask
    lecturer_time_slot = {}

    for i, gene in enumerate(individual):
        course, lecturer, time_slot, hall = gene.split('-')
        if (lecturer, time_slot) in lecturer_time_slot:
            conflict_mask[i] = 1  # Mark conflict
        else:
            lecturer_time_slot[(lecturer, time_slot)] = course

    return conflict_mask


def hall_timeSlot_conflicts(individual):
    conflict_mask = [0] * len(individual)
    hall_time_slot = {}
    for i, gene in enumerate(individual):
        course, lecturer, time_slot, hall = gene.split('-')
        if (hall, time_slot) in hall_time_slot:
            conflict_mask[i] = 1  # Mark conflict
        else:
            hall_time_slot[(lecturer, time_slot)] = hall

    return conflict_mask