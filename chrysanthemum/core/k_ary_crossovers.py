import random
from collections import deque

POINTS = 2

def onePointCrossover(parent_a: list[object], parent_b: list[object]) -> tuple[list[object], list[object]]:
    crossover_point = random.randint(0, len(parent_a)-1)
    child_a = parent_a[:crossover_point] + parent_b[crossover_point:]
    child_b = parent_b[:crossover_point] + parent_a[crossover_point:]
    return child_a, child_b

def twoPointCrossover(parent_a: list[object], parent_b: list[object]) -> tuple[list[object], list[object]]:
    crossover_points = []
    while len(crossover_points) != 2:
        candidate = random.randint(1, len(parent_a)-1)
        if candidate not in crossover_points:
            crossover_points.append(candidate)
    crossover_points.sort()
    child_a = parent_a[:crossover_points[0]] + parent_b[crossover_points[0]:crossover_points[1]] + parent_a[crossover_points[1]:]
    child_b = parent_b[:crossover_points[0]] + parent_a[crossover_points[0]:crossover_points[1]] + parent_b[crossover_points[1]:]
    return child_a, child_b

def kPointCrossover(parent_a: list[object], parent_b: list[object]) -> tuple[list[object], list[object]]:
    crossover_points = []
    if POINTS % 2 == 1:
        crossover_points.append(0)
    while len(crossover_points) != POINTS:
        candidate = random.randint(1, len(parent_a)-1)
        if candidate not in crossover_points:
            crossover_points.append(candidate)
    crossover_points.sort()
    child_a = parent_a.copy()
    child_b = parent_b.copy()
    for cpi in range(1, len(crossover_points)):
        child_a[crossover_points[cpi-1]:crossover_points[cpi]] = parent_b[crossover_points[cpi-1]:crossover_points[cpi]]
        child_b[crossover_points[cpi-1]:crossover_points[cpi]] = parent_a[crossover_points[cpi-1]:crossover_points[cpi]]
    return child_a, child_b

def uniformCrossover(parent_a: list[object], parent_b: list[object]) -> tuple[list[object], list[object]]:
    crossover_count = random.randint(1, len(parent_a))
    crossover_genes = []
    while len(crossover_genes) != crossover_count:
        candidate = random.randint(0, len(parent_a)-1)
        if candidate not in crossover_genes:
            crossover_genes.append(candidate)
    child_a = parent_a.copy()
    child_b = parent_b.copy()
    for crossover_gene in crossover_genes:
        child_a[crossover_gene] = parent_b[crossover_gene]
        child_b[crossover_gene] = parent_a[crossover_gene]
    return child_a, child_b

def ringCrossover(parent_a: list[object], parent_b: list[object]) -> tuple[list[object], list[object]]:
    crossover_point = random.randint(0, len(parent_a)-1)
    unified_parents = deque(parent_a+parent_b)
    unified_parents.rotate(crossover_point)
    unified_parents = list(unified_parents)
    child_a = unified_parents[:len(parent_a)]
    child_b = unified_parents[len(parent_a):]
    return child_a, child_b

