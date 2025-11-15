# operações genéticas simples (estudante)

import random
from .individual import Individual

def tournament_selection(population):
    a = random.choice(population.individuals)
    b = random.choice(population.individuals)

    # menor fitness = melhor (minimização)
    if a.fitness is None or b.fitness is None:
        return random.choice([a, b])

    return a if a.fitness < b.fitness else b


def one_point_crossover(parent1, parent2):
    """
    Crossover de 1 ponto entre as strings binárias SMMMM.
    Retorna dois objetos Individual já com binary e decoded_value e value atualizados.
    """
    parent1.encode()
    parent2.encode()

    b1 = parent1.binary
    b2 = parent2.binary

    # corte entre 1 e 4
    cut = random.randint(1, 4)

    child1_bin = b1[:cut] + b2[cut:]
    child2_bin = b2[:cut] + b1[cut:]

    child1 = Individual(0)
    child2 = Individual(0)

    child1.binary = child1_bin
    child2.binary = child2_bin

    # decodifica e garante que .value acompanha o valor decodificado
    child1.decode()
    child2.decode()

    # se decode definiu decoded_value, faz value igual a ele (para próximas operações)
    if child1.decoded_value is not None:
        child1.value = child1.decoded_value
    if child2.decoded_value is not None:
        child2.value = child2.decoded_value

    return child1, child2


def mutate_flip_bit_in_individual(individual, pos):
    """
    Aplica flip em uma posição pos (0..4) na representação binária do indivíduo.
    Atualiza binary, decoded_value e value.
    """
    if individual.binary is None:
        individual.encode()

    bin_list = list(individual.binary)
    bin_list[pos] = "1" if bin_list[pos] == "0" else "0"
    new_bin = "".join(bin_list)

    individual.binary = new_bin
    individual.decode()

    # atualiza value para o valor decodificado (importante para próximos passos)
    if individual.decoded_value is not None:
        individual.value = individual.decoded_value

    return individual
