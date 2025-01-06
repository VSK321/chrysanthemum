import random

def evaluate_tsp_solution(problem: list[tuple[float, float]], solution: list[int]) -> float:
    total_distance = 0
    for position in range(1, len(solution)):
        position_1 = problem[solution[position]]
        position_2 = problem[solution[position-1]]
        total_distance += ((position_2[1] - position_1[1])**2 + (position_2[0] - position_1[0])**2)**0.5
    position_1 = problem[0]
    position_2 = problem[solution[position]]
    total_distance += ((position_2[1] - position_1[1])**2 + (position_2[0] - position_1[0])**2)**0.5
    return total_distance

def load_tsp_problem(path: str) -> list[tuple[float, float]]:
    with open(path, 'r') as file:
        data = file.read()
    data = data.replace("   ", " ")
    data = data.splitlines()
    dimensions = int(data[3].split()[-1])
    tsp_data: list[tuple[float, float]] = []
    for line in data[11:11+dimensions]:
        line = line.split()
        tsp_data.append((int(line[1]), int(line[2])))
    return tsp_data

def tsp_solution_generator(length: int) -> list[int]:
    solution = list(range(1, length))
    random.shuffle(solution)
    return solution

