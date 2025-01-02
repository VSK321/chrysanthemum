
class Chromosome:
    
    def __init__(self, solution: list[object], fitness: float|list[float] = None) -> None:
        self.solution: list[object] = solution
        self.fitness: float|list[float] = fitness

        #Parameters for NSGA2
        self.rank: int = 0
        self.dominates: list[Chromosome] = []
        self.dominated_by: int = 0

    def reset(self):
        '''
        Function to reset NSGA2 parameters
        '''
        self.dominates = []
        self.dominated_by = 0
        self.rank = 0