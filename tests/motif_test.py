from chrysanthemum.core.settings import Settings, Algorithm_Type, Return_Parameters
from chrysanthemum.core.generic_so_algorithm import Generic_SO_Algorithm
from chrysanthemum.core.selection import tournament_so_wrapper
from chrysanthemum.core.k_ary_crossovers import twoPointCrossover
from chrysanthemum.core.k_ary_mutations import single_point_mutation
from chrysanthemum.problems.motif_identification_problem import motif_solution_generator, load_motif_problem, evaluate_motif_solution

def motif_test():
    symbols = ['A', 'C', 'G', 'T']
    p = load_motif_problem('./test_data/motif.txt')
    population = 200
    settings = Settings(population_count=population, maximize=False, solution_generator=motif_solution_generator, 
                        solution_generator_parameters=[20], fitness_calculator=evaluate_motif_solution, 
                        fitness_calculator_parameters=[p], 
                        crossover=twoPointCrossover, selection=tournament_so_wrapper, selection_parameters=[2], selection_count=int(population/2), 
                        mutation=single_point_mutation, mutation_rate=0.05, mutation_parameters=[symbols], 
                        algorithm_type=Algorithm_Type.STEADY_STATE_REPLACE_WEAKEST, termination_generation=50, 
                        return_parameters=[Return_Parameters.BEST_CANDIDATE])
    genetic_algorithm = Generic_SO_Algorithm(settings)
    return_values = genetic_algorithm.main()
    print(''.join(return_values[0].solution))
    print(return_values[0].fitness)
