import random

def hamming_distance(text_a: list[str], text_b: str) -> int:
    counter = 0
    for item_index in range(len(text_a)):
        #if text_a[item_index][0] == "|":
        #    counter += 1
        if text_b[item_index] not in text_a[item_index]:
            counter += 1
            #if text_a[item_index][0] == "|":
            #    counter += 1
    return counter

def evaluate_motif_solution(problem: list[str], solution: list[str]) -> float:
    #Time complexity is an issue
    hamming_counter = 0
    solution_length = len(solution)
    #solution = ''.join(solution)
    for string in problem:
        lowest_hamming_counter = 10**10
        for index in range(len(string)-solution_length+1):
            curr_hamming_distance = hamming_distance(solution, string[index:index+solution_length])
            if curr_hamming_distance < lowest_hamming_counter:
                lowest_hamming_counter = curr_hamming_distance
        hamming_counter += lowest_hamming_counter
    return hamming_counter

def load_motif_problem(path: str) -> list[str]:
    with open(path, 'r') as file:
        data = file.read()
    data = data.splitlines()[1:]
    return data

def motif_solution_generator(length: int, symbols: list[object]) -> list[str]:
    solution = [random.choice(symbols) for _ in range(length)]
    return solution