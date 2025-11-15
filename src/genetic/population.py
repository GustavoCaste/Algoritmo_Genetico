# classe da população (atualizada)

import random
from .individual import Individual
from .operations import tournament_selection, one_point_crossover, mutate_flip_bit_in_individual

class Population:
    def __init__(self, size):
        self.size = size
        self.individuals = []
        self.best = None

    # cria população inicial
    def initialize(self):
        self.individuals = []
        for _ in range(self.size):
            val = random.uniform(-15, 15)
            ind = Individual(val)
            self.individuals.append(ind)

    # avalia todos os indivíduos
    def evaluate(self):
        self.best = None

        for ind in self.individuals:
            ind.evaluate()

            if self.best is None or ind.fitness < self.best.fitness:
                self.best = ind

    # método que cria uma nova geração
    # seguindo a regra: mutação em apenas um gene da população (um flip em um indivíduo)
    def evolve(self):
        new_population = []

        # enquanto não atingir o tamanho desejado
        while len(new_population) < self.size:
            # seleção por torneio (usa a população atual, já avaliada)
            p1 = tournament_selection(self)
            p2 = tournament_selection(self)

            # crossover de um ponto (retorna Individuals já decodificados)
            child1, child2 = one_point_crossover(p1, p2)

            # adiciona na nova geração
            new_population.append(child1)
            if len(new_population) < self.size:
                new_population.append(child2)

        # agora, aplicar mutação: **somente um gene** da população
        # escolhe um indivíduo aleatório e um bit aleatório, e faz flip
        idx = random.randrange(0, self.size)
        bit_pos = random.randint(0, 4)

        # assegurar que o indivíduo tem binary (se não, encode)
        individuo_mutar = new_population[idx]
        mutate_flip_bit_in_individual(individuo_mutar, bit_pos)
        new_population[idx] = individuo_mutar

        # atualiza a população
        self.individuals = new_population

        # avalia a nova geração
        self.evaluate()
