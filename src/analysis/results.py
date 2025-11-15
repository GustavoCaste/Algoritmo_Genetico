# gera tabela comparativa dos resultados (estudante)

def gerar_tabela(final_results):
    """
    final_results esperado:
    {
        4: {"melhor_fitness": float, "melhor_x": float},
        8: {...},
        12: {...}
    }
    """
    print("\n========== TABELA COMPARATIVA ==========\n")
    print("Pop   |   Melhor Fitness   |   Melhor x")
    print("----------------------------------------")

    tabela = {}

    for pop_size in sorted(final_results.keys()):
        dados = final_results[pop_size]
        melhor = dados.get("melhor_fitness")
        melhor_x = dados.get("melhor_x")
        tabela[pop_size] = {"melhor": melhor, "x": melhor_x}

        print(f"{pop_size:<5} | {melhor:<17} | {melhor_x}")

    print("\n=========================================\n")
    return tabela


def salvar_csv(tabela, nome_arquivo="results.csv"):
    """
    Recebe o dicionário gerado por gerar_tabela e salva um CSV simples.
    """
    linhas = ["populacao,melhor_fitness,melhor_x\n"]

    for pop, dados in tabela.items():
        linha = f"{pop},{dados['melhor']},{dados['x']}\n"
        linhas.append(linha)

    with open(nome_arquivo, "w") as f:
        f.writelines(linhas)

    print(f"Tabela salva em: {nome_arquivo}")
