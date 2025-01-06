# Chrysanthemum: Generic Genetic Algorithm in Python

A pure Python implementation of genetic algorithms with multiple crossovers, mutations and selection methods. Currently a WIP but examples for the knapsack problem, motif search problem and TSP are included. 

Made to be easy to configure and modify for specific use cases. 

Inspired by [pymoo](https://github.com/anyoptimization/pymoo).

Named after "Girl with Chrysanthemums" by Olga Boznanska. 

## Installation

Currently not packaged for PyPI so cloning the repository would be the easiest way to get started.

```
git clone https://github.com/VSK321/chrysanthemum
```

## Example Usage

A problem requires a solution generator, for the initial population, and an evaluator. The solution generator is required to follow `generator(params) -> list[object]` as its general structure. These params can be specified when designing the genetic algorithm. 

The Evaluator is required to follow `calculator(params, solution: list[object]) -> float|list[float]` with the params, again, specified when designing the genetic algorithm. Currently only single-objective problems are supported so only floats should be returned. 

Once the problem has been specified, the genetic algorithm can be designed. The generic structure would be:

```
from chrysanthemum.core.settings import Settings, Algorithm_Type, Return_Parameters
from chrysanthemum.core.generic_so_algorithm import Generic_SO_Algorithm
from chrysanthemum.core.selection import tournament_so_wrapper
from chrysanthemum.core.k_ary_crossovers import twoPointCrossover
from chrysanthemum.core.k_ary_mutations import single_point_mutation
from your_problem import problem_loader, generator, calculator

symbols = [] #Load list of symbols for k-ary coded problems
p = problem_loader() #load a generic problem
settings = Settings(population_count=100, maximize=True,
                    solution_generator=generator, 
                    solution_generator_parameters=[len(p)], 
                    fitness_calculator=calculator, 
                    fitness_calculator_parameters=[p], 
                    crossover=twoPointCrossover, 
                    selection=tournament_so_wrapper, 
                    selection_parameters=[2], selection_count=50, 
                    mutation=single_point_mutation, 
                    mutation_rate=0.05, mutation_parameters=[symbols], 
                    algorithm_type=Algorithm_Type.GENERATIONAL, 
                    termination_generation=256, 
                    return_parameters=[Return_Parameters.BEST_CANDIDATE])
genetic_algorithm = Generic_SO_Algorithm(settings)
return_values = genetic_algorithm.main()
print(return_values[0].solution)
print(return_values[0].fitness)
```

## Next Steps
- Add more permutation crossovers and mutations
- Add real-value mutations
- Add roulette wheel and rank based selection
- Create pre-configured settings
- Improve documentation
- Add multi-objective generic genetic algorithm (potentially NSGA-II)
- Package the project, potentially, for PyPI

