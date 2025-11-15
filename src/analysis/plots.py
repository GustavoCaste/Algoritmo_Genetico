import matplotlib.pyplot as plt
from genetic.population import Population

def executar_e_coletar(pop_size=8, num_generations=10):
    """
    Roda UMA execução do AG com população pop_size
    e coleta o melhor fitness de cada geração.
    """
    pop = Population(pop_size)
    pop.initialize()
    pop.evaluate()

    historico = [pop.best.fitness]  # inclui geração 0

    for _ in range(num_generations):
        pop.evolve()
        historico.append(pop.best.fitness)

    return historico


def plotar_grafico(historico, titulo="Melhor indivíduo por geração", salvar_arquivo=None):
    """
    Recebe uma lista com o melhor fitness de cada geração
    e gera o gráfico (estilo simples). Se salvar_arquivo for fornecido,
    salva o gráfico como PNG.
    """
    plt.figure(figsize=(8, 5))
    plt.plot(range(len(historico)), historico, marker='o')
    plt.xlabel("Geração")
    plt.ylabel("Melhor fitness")
    plt.title(titulo)
    plt.grid(True)
    plt.tight_layout()

    if salvar_arquivo:
        plt.savefig(salvar_arquivo)
    else:
        plt.show()

    plt.close()
