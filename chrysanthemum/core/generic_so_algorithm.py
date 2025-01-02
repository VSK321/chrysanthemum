import copy
import random
import time

from chrysanthemum.core.settings import Settings, Algorithm_Type, Return_Parameters
from chrysanthemum.core.chromosome import Chromosome

class Generic_SO_Algorithm:
    
    def __init__(self, settings: Settings):
        self.settings: Settings = settings
        self.setup()
    
    def setup(self):
        self.population: list[Chromosome] = [Chromosome(self.settings.solution_generator(*self.settings.solution_generator_parameters)) 
                                             for _ in range(self.settings.population_count)]
        
        for chromosome in self.population:
            chromosome.fitness = self.settings.fitness_calculator(*self.settings.fitness_calculator_parameters, chromosome.solution)
        

    def average_in_population(self) -> float:
        s = [chromosome.fitness for chromosome in self.population]
        return sum(s)/self.settings.population_count

    def main(self) -> list[object]:
        start = time.time()

        averages: list[float] = []
        best_values: list[Chromosome] = []
        worst_values: list[Chromosome] = []

        relations = {Return_Parameters.CHANGE_IN_AVERAGE: averages, Return_Parameters.CHANGE_IN_BEST: best_values, 
                     Return_Parameters.CHANGE_IN_WORST: worst_values}

        for generation in range(self.settings.termination_generation):
            #Sort population and collect data
            self.population.sort(key=lambda chromosome: chromosome.fitness, reverse=self.settings.maximize)
            best_values.append(self.population[0])
            worst_values.append(self.population[-1])
            averages.append(self.average_in_population())

            new_population: list[Chromosome] = []

            for crossover_selection in range(self.settings.selection_count):
                parent_a, parent_b = self.settings.selection(self.population, *self.settings.selection_parameters)

                new_population += [Chromosome(self.settings.mutation(child, *self.settings.mutation_parameters)) if random.random() <= self.settings.mutation_rate else Chromosome(child) 
                                   for child in list(self.settings.crossover(parent_a, parent_b))]
            
            for chromosome in new_population:
                chromosome.fitness = self.settings.fitness_calculator(*self.settings.fitness_calculator_parameters, chromosome.solution)

                
            if self.settings.algorithm_type == Algorithm_Type.GENERATIONAL:
                self.population = new_population.copy()
            elif self.settings.algorithm_type == Algorithm_Type.GENERATIONAL_ELITIST:
                new_population.sort(key=lambda chromosome: chromosome.fitness, reverse=self.settings.maximize)
                self.population = new_population[:self.settings.population_count]
            elif self.settings.algorithm_type == Algorithm_Type.STEADY_STATE_REPLACE_WEAKEST:
                self.population += new_population
                self.population.sort(key=lambda chromosome: chromosome.fitness, reverse=self.settings.maximize)
                self.population = self.population[:self.settings.population_count]
            elif self.settings.algorithm_type == Algorithm_Type.STEADY_STATE_REPLACE_FIRST_WEAKEST:
                raise NotImplementedError
            else:
                raise NotImplementedError
        
        self.population.sort(key=lambda chromosome: chromosome.fitness, reverse=self.settings.maximize)
        best_values.append(self.population[0])
        worst_values.append(self.population[-1])
        averages.append(self.average_in_population())

        relations[Return_Parameters.AVERAGE_CANDIDATE] = averages[-1]
        relations[Return_Parameters.BEST_CANDIDATE] = best_values[-1]
        relations[Return_Parameters.WORST_CANDIDATE] = worst_values[-1]

        final_time = time.time() - start

        print("Time Taken:", final_time)

        return_values = [relations[val] for val in self.settings.return_parameters]

        return return_values
