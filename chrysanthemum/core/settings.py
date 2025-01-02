
from enum import Enum
from typing import Callable

from chrysanthemum.core.chromosome import Chromosome


class Return_Parameters(Enum):
    #Candidate will always return the fitness
    BEST_CANDIDATE = 1
    WORST_CANDIDATE = 2
    #Mean average
    AVERAGE_CANDIDATE = 3
    #Change at each generation
    CHANGE_IN_BEST = 4
    CHANGE_IN_WORST = 5
    CHANGE_IN_AVERAGE = 6


class Algorithm_Type(Enum):
    GENERATIONAL = 1
    GENERATIONAL_ELITIST = 2
    STEADY_STATE_REPLACE_WEAKEST = 3
    STEADY_STATE_REPLACE_FIRST_WEAKEST = 4

class Settings:

    def __init__(self, population_count: int, maximize: bool, solution_generator: Callable[[list[object]], list[object]],
                 solution_generator_parameters: list[object], fitness_calculator: Callable[[list[object], list[object]], float|list[float]],
                 fitness_calculator_parameters: list[object], crossover: Callable[[list[object], list[object]], tuple[list[object], list[object]]],
                selection: Callable[[list[list[Chromosome]], tuple[list[object], list[object]]], list[object]], selection_parameters: list[object], 
                selection_count: int, mutation: Callable[[list[object], list[object]], list[object]], mutation_rate: float, mutation_parameters: list[object],
                algorithm_type: Algorithm_Type = Algorithm_Type.GENERATIONAL, termination_generation: int = 512, return_parameters: list[Return_Parameters]|None = None):
        self.population_count: int = population_count
        self.maximize: bool = maximize
        self.solution_generator: Callable[[list[object]], list[object]] = solution_generator
        self.solution_generator_parameters: list[object] = solution_generator_parameters
        self.fitness_calculator: Callable[[list[object], list[object]], float|list[float]] = fitness_calculator
        self.fitness_calculator_parameters: list[object] = fitness_calculator_parameters
        self.crossover: Callable[[list[object], list[object]], tuple[list[object], list[object]]] = crossover
        self.selection: Callable[[list[list[Chromosome]], list[object]], tuple[list[object], list[object]]] = selection
        self.selection_parameters: list[object] = selection_parameters
        self.selection_count: int = selection_count
        self.mutation: Callable[[list[object], list[object]], list[object]] = mutation
        self.mutation_rate: float = mutation_rate
        self.mutation_parameters: list[object] = mutation_parameters
        self.algorithm_type: Algorithm_Type = algorithm_type
        self.termination_generation: int = termination_generation
        if return_parameters == None:
            return_parameters = []
        self.return_parameters: list[Return_Parameters] = return_parameters

