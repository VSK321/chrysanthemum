import random

def swap_mutation(solution: list[object]) -> list[object]:
    index_a = random.randint(0, len(solution)-1)
    index_b = random.randint(0, len(solution)-1)
    while index_b == index_a:
        index_b = random.randint(0, len(solution)-1)
    solution[index_a], solution[index_b] = solution[index_b], solution[index_a]
    return solution

