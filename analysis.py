import random

from Mutation import mutate_timetable
from crossover import crossover_with_mask, two_point_crossover_timetable
from fit import fitness_scores, total_fitness_score
from gui import plot_fitness
from select_1 import tournament_selection, roulette_wheel_selection, rank_selection


def analyze(population):
    def to_u(population, generations=100, mutation_rate=0.1):
        fit_dec = []
        for generation in range(generations):
            # Step 1: Evaluate fitness of each individual
            pop_scores = fitness_scores(population)

            # Step 2: Select parents using roulette wheel selection
            new_population = []
            for _ in range(len(population) // 2):  # Produce pairs of children
                parent1 = tournament_selection(population, pop_scores, len(population) // 10)
                parent2 = tournament_selection(population, pop_scores, len(population) // 10)

                # Step 3: Perform crossover
                child1, child2 = crossover_with_mask(parent1, parent2)

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

    def to_2(population, generations=100, mutation_rate=0.1):
        fit_dec = []
        for generation in range(generations):
            # Step 1: Evaluate fitness of each individual
            pop_scores = fitness_scores(population)

            # Step 2: Select parents using roulette wheel selection
            new_population = []
            for _ in range(len(population) // 2):  # Produce pairs of children
                parent1 = tournament_selection(population, pop_scores, len(population) // 10)
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

    def ro_u(population, generations=100, mutation_rate=0.1):
        fit_dec = []
        for generation in range(generations):
            # Step 1: Evaluate fitness of each individual
            pop_scores = fitness_scores(population)

            # Step 2: Select parents using roulette wheel selection
            new_population = []
            for _ in range(len(population) // 2):  # Produce pairs of children
                parent1 = roulette_wheel_selection(population, pop_scores)
                parent2 = roulette_wheel_selection(population, pop_scores)

                # Step 3: Perform crossover
                child1, child2 = crossover_with_mask(parent1, parent2)

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

    def ro_2(population, generations=100, mutation_rate=0.1):
        fit_dec = []
        for generation in range(generations):
            # Step 1: Evaluate fitness of each individual
            pop_scores = fitness_scores(population)

            # Step 2: Select parents using roulette wheel selection
            new_population = []
            for _ in range(len(population) // 2):  # Produce pairs of children
                parent1 = roulette_wheel_selection(population, pop_scores)
                parent2 = roulette_wheel_selection(population, pop_scores)

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

    def ra_u(population, generations=100, mutation_rate=0.1):
        fit_dec = []
        for generation in range(generations):
            # Step 1: Evaluate fitness of each individual
            pop_scores = fitness_scores(population)

            # Step 2: Select parents using roulette wheel selection
            new_population = []
            for _ in range(len(population) // 2):  # Produce pairs of children
                parent1 = rank_selection(population, pop_scores)
                parent2 = rank_selection(population, pop_scores)

                # Step 3: Perform crossover
                child1, child2 = crossover_with_mask(parent1, parent2)

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

    def ra_2(population, generations=100, mutation_rate=0.1):
        fit_dec = []
        for generation in range(generations):
            # Step 1: Evaluate fitness of each individual
            pop_scores = fitness_scores(population)

            # Step 2: Select parents using roulette wheel selection
            new_population = []
            for _ in range(len(population) // 2):  # Produce pairs of children
                parent1 = rank_selection(population, pop_scores)
                parent2 = rank_selection(population, pop_scores)

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

    def analyze_fitness_penalty_system(fitness_scores):
        final_fitness = fitness_scores[-1]
        best_fitness = min(fitness_scores)
        average_fitness = sum(fitness_scores) / len(fitness_scores)
        improvement_rate = (fitness_scores[0] - fitness_scores[-1]) / len(fitness_scores)

        import numpy as np
        fitness_differences = np.diff(fitness_scores)
        convergence_gen = next((i for i, diff in enumerate(fitness_differences) if abs(diff) < 0.01),
                               len(fitness_scores))
        fitness_stability = np.std(fitness_scores)
        auc = np.trapz(fitness_scores)

        # Print the metrics
        print(f"Final Fitness: {final_fitness}")
        print(f"Best Fitness: {best_fitness}")
        print(f"Average Fitness: {average_fitness}")
        print(f"Improvement Rate: {improvement_rate}")
        print(f"Convergence Generation: {convergence_gen}")
        print(f"Fitness Stability: {fitness_stability}")
        print(f"AUC: {auc}")

    _, r1 = to_2(population)
    plot_fitness(r1)
    analyze_fitness_penalty_system(r1)

    _, r2 = to_u(population)
    plot_fitness(r2)
    analyze_fitness_penalty_system(r2)

    _, r3 = ro_2(population)
    plot_fitness(r3)
    analyze_fitness_penalty_system(r3)

    _, r4 = ro_u(population)
    plot_fitness(r4)
    analyze_fitness_penalty_system(r4)

    _, r5 = ra_2(population)
    plot_fitness(r5)
    analyze_fitness_penalty_system(r5)

    _, r6 = ra_u(population)
    plot_fitness(r6)
    analyze_fitness_penalty_system(r6)
