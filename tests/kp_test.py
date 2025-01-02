from chrysanthemum.core.settings import Settings, Algorithm_Type, Return_Parameters
from chrysanthemum.core.generic_so_algorithm import Generic_SO_Algorithm
from chrysanthemum.core.selection import tournament_so_wrapper
from chrysanthemum.core.k_ary_crossovers import twoPointCrossover
from chrysanthemum.core.k_ary_mutations import single_point_mutation
from chrysanthemum.problems.knapsack_problem import knapsack_loader_from_ttp, knapsack_fitness_calculator, knapsack_solution_generator

def kp_test():
    symbols = [0, 1]
    p = knapsack_loader_from_ttp('./test_data/280_dataset.txt')
    settings = Settings(population_count=560, maximize=True, solution_generator=knapsack_solution_generator, 
                        solution_generator_parameters=[len(p.problem)], fitness_calculator=knapsack_fitness_calculator, 
                        fitness_calculator_parameters=[p], 
                        crossover=twoPointCrossover, selection=tournament_so_wrapper, selection_parameters=[2], selection_count=280, 
                        mutation=single_point_mutation, mutation_rate=0.05, mutation_parameters=[symbols], 
                        algorithm_type=Algorithm_Type.GENERATIONAL, termination_generation=256, 
                        return_parameters=[Return_Parameters.BEST_CANDIDATE])
    genetic_algorithm = Generic_SO_Algorithm(settings)
    return_values = genetic_algorithm.main()
    print(return_values[0].solution)
    print(return_values[0].fitness)
