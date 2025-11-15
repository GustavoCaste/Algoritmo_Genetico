from genetic.population import Population

def main():
    print("=== Teste com população de 4 indivíduos ===")

    try:
        pop = Population(size=4)

        pop.initialize()
        pop.evaluate()

        print("Melhor indivíduo da geração:")
        print("  Valor real inicial:", pop.best.value)
        print("  Valor decodificado:", pop.best.decoded_value)
        print("  Fitness:", pop.best.fitness)

    except Exception as e:
        print("Erro ao rodar teste:", e)


if __name__ == "__main__":
    main()
