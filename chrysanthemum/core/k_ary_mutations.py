import random

def single_point_mutation(solution: list[object], symbols: list[object]) -> list[object]:
    index = random.randint(0, len(solution)-1)
    solution[index] = random.choice([symbol for symbol in symbols if symbol != solution[index]])
    return solution


def equal_probability_mutation(solution: list[object], symbols: list[object]) -> list[object]:
    probability = 1/len(solution)
    for index in range(len(solution)):
        if random.random() <= probability:
            solution[index] = random.choice([symbol for symbol in symbols if symbol != solution[index]])
    return solution