#### each individual form ###
import analysis
from encoder import decode_individual
# [ [course_1, lecturer_1, time_slot_1,hall],
#   [course_2, lecturer_2, time_slot_2,hall],
#   [course_3, lecturer_1, time_slot_3,hall], and so on ... ]
from fit import *
from gui import visualize_timetable, plot_fitness
from select_1 import *
from crossover import *
from Mutation import *
import random
from Data import *
import matplotlib.pyplot as plt
import numpy as np


# generate population
def generate_population(num_of_individuals):
    population = []

    for _ in range(num_of_individuals):
        individual = []

        # track the total number of courses assigned to each lecturer
        lecturer_total_courses = {lecturer: 0 for lecturer in lecturers}

        for course, slots_needed in zip(Courses,org_course_requirements.values()):
            for _ in range(slots_needed):
                lecturer = random.choice(lecturers)

                # ensure  that lecturer doesn't exceed their course teaching limit
                while lecturer_total_courses[lecturer] >= 3:
                    lecturer = random.choice(lecturers)

                hall = random.choice(halls)  # assign a hall randomly
                time_slot = random.choice(time_slots)  # assign a time slot randomly

                # assign the lecture after ensuring that he does not above his limit
                individual.append(f"{course}-{lecturer}-{time_slot}-{hall}")
                lecturer_total_courses[lecturer] += 1

        population.append(individual)
    return population

def genetic_algorithm(population, generations=100, mutation_rate=0.1):
    fit_dec = []
    for generation in range(generations):
        # Step 1: Evaluate fitness of each individual
        pop_scores = fitness_scores(population)

        # Step 2: Select parents using roulette wheel selection
        new_population = []
        for _ in range(len(population) // 2):  # Produce pairs of children
            parent1 = tournament_selection(population, pop_scores,len(population) // 10)
            parent2 = tournament_selection(population, pop_scores, len(population) // 10)

            # Step 3: Perform crossover
            child1, child2 = two_point_crossover_timetable(parent1, parent2)

            # Step 4: Mutate children

            if random.random() < mutation_rate:
                child1 = mutate_timetable(child1)
            if random.random() < mutation_rate:
                child2 = mutate_timetable(child2)

            new_population.extend([child1, child2])

        # Step 5: Replace old population with the new one
        population = new_population

        # Optional: Track and print the best solution in the current generation
        best_individual = min(population, key=total_fitness_score)
        fit_dec.append(total_fitness_score(best_individual))
        print(f"Generation {generation + 1}, Best Fitness: {total_fitness_score(best_individual)}")

    # Return the best individual after all generations
    return min(population, key=total_fitness_score), fit_dec




def generate_course_report_to_file(lecture_data):
    """
    Processes lecture data and generates a report organized by courses, saving it to a file.

    Args:
        lecture_data (list): A list of lecture details where each entry is a list in the format
                             [course, doctor, day_time, hall].
        filename (str): The name of the file to save the report (default: "course_report.txt").
    Returns:
        dict: A dictionary containing organized lecture data by courses.
    """
    filename = "course_report.txt"
    course_report = {}

    # Process the lecture data
    for course, doctor, day_time, hall in lecture_data:
        if course not in course_report:
            course_report[course] = []
        course_report[course].append({'doctor': doctor, 'day_time': day_time, 'hall': hall})

    # Write the report to a file
    with open(filename, "w") as file:
        for course, lectures in course_report.items():
            file.write(f"Report for Course: {course}\n")
            for lecture in lectures:
                file.write(f"- Doctor: {lecture['doctor']}, Day/Time: {lecture['day_time']}, Hall: {lecture['hall']}\n")
            file.write("\n" + "=" * 40 + "\n\n")

    return course_report


def generate_doctor_report_to_file(lecture_data):
    """
    Processes lecture data and generates a report organized by doctor's name, saving it to a file.

    Args:
        lecture_data (list): A list of lecture details where each entry is a list in the format
                             [course, doctor, day_time, hall].
        filename (str): The name of the file to save the report (default: "doctor_report.txt").
    Returns:
        dict: A dictionary containing organized lecture data by doctor's name.
    """
    filename = "doctor_report.txt"
    doctor_report = {}

    # Process the lecture data
    for course, doctor, day_time, hall in lecture_data:
        if doctor not in doctor_report:
            doctor_report[doctor] = []
        doctor_report[doctor].append({'course': course, 'day_time': day_time, 'hall': hall})

    # Write the report to a file
    with open(filename, "w") as file:
        for doctor, lectures in doctor_report.items():
            file.write(f"Report for Dr. {doctor}:\n")
            for lecture in lectures:
                file.write(f"- Course: {lecture['course']}, Day/Time: {lecture['day_time']}, Hall: {lecture['hall']}\n")
            file.write("\n" + "=" * 40 + "\n\n")

    return doctor_report



# Example usage
if __name__ == "__main__":
    # Initialize a random population of timetables
    population_size = 150
    population = generate_population(population_size)
    for p in population:
        print(p)

    # Run the genetic algorithm
    best_timetable,fs = genetic_algorithm(
        population,
        generations=100,
        mutation_rate=0.1
    )
    #analysis.analyze(population)
    tb = decode_individual(best_timetable,org_lecturers,org_halls,org_time_slots,org_course_requirements)
    print(tb)
    generate_course_report_to_file(tb)
    print("---------------------------------------------------------------------------")
    generate_doctor_report_to_file(tb)
    plot_fitness(fs)
    visualize_timetable(tb)