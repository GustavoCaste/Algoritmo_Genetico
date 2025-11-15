# main.py final - roda tudo conforme especificação do trabalho

import random
from analysis.results import gerar_tabela, salvar_csv
from analysis.plots import plotar_grafico, executar_e_coletar
from genetic.population import Population

def run_single_execution(pop_size, num_generations=10):
    """
    Roda UMA execução do AG (pop_size) por num_generations gerações
    e retorna (best_fitness, best_x) para essa execução, e o historico de melhores por geração.
    """
    pop = Population(pop_size)
    pop.initialize()
    pop.evaluate()

    historico = [pop.best.fitness]  # geração 0

    for _ in range(num_generations):
        pop.evolve()
        historico.append(pop.best.fitness)

    # retorna o melhor encontrado nessa execução e o histórico
    return pop.best.fitness, pop.best.decoded_value, historico


def run_all(pop_sizes=(4, 8, 12), executions=100, generations=10):
    random.seed(42)  # reprodutibilidade

    final_results = {}
    history_pop8_for_plot = None

    for p in pop_sizes:
        print(f"\n=== Rodando população {p} ===")
        best_overall = None
        best_x_overall = None

        for run in range(executions):
            best_fitness, best_x, hist = run_single_execution(p, num_generations=generations)

            # guarda histórico da primeira execução de pop=8 para plot
            if p == 8 and run == 0:
                history_pop8_for_plot = hist

            # escolhe o melhor entre as 100 execuções (minimização)
            if best_overall is None or best_fitness < best_overall:
                best_overall = best_fitness
                best_x_overall = best_x

        final_results[p] = {
            "melhor_fitness": best_overall,
            "melhor_x": best_x_overall
        }

        print(f"Pop {p} -> melhor fitness entre 100 execuções: {best_overall} (x={best_x_overall})")

    return final_results, history_pop8_for_plot


def main():
    resultados, historico_pop8 = run_all(pop_sizes=(4,8,12), executions=100, generations=10)

    # gera tabela impressa e salva CSV
    tabela = gerar_tabela(final_results=resultados)
    salvar_csv(tabela, nome_arquivo="results.csv")

    # gera gráfico da população 8 (histórico da primeira execução de pop=8)
    if historico_pop8 is not None:
        plotar_grafico(historico_pop8, titulo="População 8 - Melhor por Geração", salvar_arquivo="plot_8_individuos.png")
        print("Gráfico salvo em plot_8_individuos.png")
    else:
        # fallback: gerar novo histórico e plotar
        hist = executar_e_coletar(pop_size=8, num_generations=10)
        plotar_grafico(hist, titulo="População 8 - Melhor por Geração (fallback)", salvar_arquivo="plot_8_individuos.png")
        print("Gráfico salvo em plot_8_individuos.png (fallback)")

    print("\nArquivo results.csv gerado com a tabela final.")


if __name__ == "__main__":
    main()
