from chrysanthemum.core.settings import Settings, Algorithm_Type, Return_Parameters
from chrysanthemum.core.generic_so_algorithm import Generic_SO_Algorithm
from chrysanthemum.core.selection import tournament_so_wrapper
from chrysanthemum.core.permutation_crossovers import OX1
from chrysanthemum.core.permutation_mutations import swap_mutation
from chrysanthemum.problems.travelling_salesperson_problem import evaluate_tsp_solution, load_tsp_problem, tsp_solution_generator

def tsp_test():
    p = load_tsp_problem('./test_data/280_dataset.txt')
    settings = Settings(population_count=100, maximize=False, solution_generator=tsp_solution_generator, 
                        solution_generator_parameters=[len(p)], fitness_calculator=evaluate_tsp_solution, 
                        fitness_calculator_parameters=[p], 
                        crossover=OX1, selection=tournament_so_wrapper, selection_parameters=[2], selection_count=280, 
                        mutation=swap_mutation, mutation_rate=0.05, mutation_parameters=[], 
                        algorithm_type=Algorithm_Type.STEADY_STATE_REPLACE_WEAKEST, termination_generation=50, 
                        return_parameters=[Return_Parameters.BEST_CANDIDATE])
    genetic_algorithm = Generic_SO_Algorithm(settings)
    return_values = genetic_algorithm.main()
    print(return_values[0].solution)
    print(return_values[0].fitness)
