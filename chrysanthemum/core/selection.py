import random

from chrysanthemum.core.chromosome import Chromosome

def tournament_so(candidates: list[Chromosome]) -> Chromosome:
    candidates.sort(key=lambda chromosome: chromosome.fitness)
    return candidates[-1]

def tournament_so_wrapper(population: list[Chromosome], tournament_size: int) -> tuple[list[object], list[object]]:
    candidates_round_one: list[Chromosome] = []
    while len(candidates_round_one) != tournament_size:
        potential_candidate = random.choice(population)
        if potential_candidate in candidates_round_one:
            continue
        candidates_round_one.append(potential_candidate)
    
    candidates_round_two: list[Chromosome] = []
    while len(candidates_round_two) != tournament_size:
        potential_candidate = random.choice(population)
        if potential_candidate in candidates_round_two:
            continue
        candidates_round_two.append(potential_candidate)

    parent_a = tournament_so(candidates_round_one)
    parent_b = tournament_so(candidates_round_two)

    return parent_a.solution, parent_b.solution