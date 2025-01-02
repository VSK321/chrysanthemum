import random

class Knapsack_Item:
    def __init__(self, cost: float = 1, weight: float = 1, location: int = None):
        self.weight: float = weight
        self.cost: float = cost
        self.location: int|None = location


class Knapsack:
    def __init__(self, problem: list[Knapsack_Item], capacity: int):
        self.problem: list[Knapsack_Item] = problem
        self.capacity: int = capacity
        self.ideal_ans_generated: int = 0
        self.ideal_ans: list[list[int]] = []
        self.sorted_by_ratio: list[Knapsack_Item] = problem.copy()
        self.sorted_by_ratio = sorted(self.sorted_by_ratio, key=lambda item: item.cost/item.weight, reverse=True)
        self.sigma = self.capacity/len(self.problem)
        #self.sorted_by_ratio.sort(lambda item: item.cost/item.weight, reverse=True)
        
def knapsack_fitness_calculator(items: Knapsack, solution: list[int]) -> list[float]:
    outcome = [0, 0]
    add = lambda a, b: [a[i]+b[i] for i in range(len(a))]
    for item_index in range(len(items.problem)):
        if solution[item_index] == 1:
            outcome = add(outcome, [items.problem[item_index].cost, items.problem[item_index].weight])
    if outcome[1] > items.capacity:
        return items.capacity-outcome[1]
    return outcome[0]

def knapsack_loader_from_ttp(list_location: str) -> Knapsack:
    #Modified from TTP code
    with open(list_location, 'r') as file:
        data = file.read()
    data = data.replace("   ", " ")
    data = data.splitlines()
    dimensions = int(data[3].split()[-1])
    capacity: int = int(data[5].split()[-1])
    #X Y
    tsp_data: list[tuple[float, float]] = []
    #Profit Weight Node
    kp_data: list[tuple[float, float, int]] = []
    for line in data[11:11+dimensions]:
        line = line.split()
        tsp_data.append((int(line[1]), int(line[2])))
    for line in data[12+dimensions:]:
        line = line.split()
        kp_data.append((int(line[1]), int(line[2]), int(line[3])))
    items: list[Knapsack_Item] = []
    for item in kp_data:
        items.append(Knapsack_Item(item[0], item[1], item[2]-1))
    distribution: dict[int, list[Knapsack_Item]] = {}
    for item in items:
        if item.location in distribution:
            distribution[item.location].append(item)
            continue
        distribution[item.location] = [item]
    return Knapsack(items, capacity)

def knapsack_solution_generator(length: int = 8) -> list[int]:
    return [random.choice([0, 1]) for _ in range(length)]

def valid_knapsack_solution_generator(knapsack: Knapsack) -> list[int]:
    weight = 0
    answer = [0 for _ in range(len(knapsack.problem))]
    counter = 0
    for _ in knapsack.problem:
        if (weight + knapsack.sorted_by_ratio[counter].weight) > knapsack.capacity:
            counter += 1
            continue
        if random.random() > 0.5:
            weight += knapsack.sorted_by_ratio[counter].weight
            answer[knapsack.problem.index(knapsack.sorted_by_ratio[counter])] = 1
        counter += 1
    if answer in knapsack.ideal_ans:
        return valid_knapsack_solution_generator(knapsack)
    knapsack.ideal_ans_generated += 1
    knapsack.ideal_ans.append(answer)
    return answer
