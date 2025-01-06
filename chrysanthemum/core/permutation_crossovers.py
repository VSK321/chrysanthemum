import random

def OX1(parent_a: list[object], parent_b: list[object]) -> tuple[list[object], list[object]]:
    crossover_points = []
    while len(crossover_points) != 2:
        candidate = random.randint(1, len(parent_a)-1)
        if candidate not in crossover_points:
            crossover_points.append(candidate)
    crossover_points.sort()
    child_a = [None for _ in range(len(parent_a))]
    child_b = child_a.copy()
    child_a[crossover_points[0]:crossover_points[1]] = parent_a[crossover_points[0]:crossover_points[1]]
    child_b[crossover_points[0]:crossover_points[1]] = parent_b[crossover_points[0]:crossover_points[1]]
    genes_in_a = [gene for gene in parent_a if gene not in child_b]
    genes_in_b = [gene for gene in parent_b if gene not in child_a]
    counter = 0
    for gene_position in range(len(child_a)):
        if child_a[gene_position] == None:
            child_a[gene_position] = genes_in_b[counter]
            counter += 1
    counter = 0
    for gene_position in range(len(child_b)):
        if child_b[gene_position] == None:
            child_b[gene_position] = genes_in_a[counter]
            counter += 1
    return child_a, child_b