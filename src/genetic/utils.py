# conversão binária e funções auxiliares

def real_to_binary(x):
    """
    Converte um valor real para binário de 5 bits:
    SMMMM  (1 bit de sinal + 4 bits magnitude)
    """
    # sinal: 1 positivo, 0 negativo
    sinal = 1 if x >= 0 else 0

    # magnitude por arredondamento
    mag = abs(int(round(x)))

    # mantém no intervalo permitido
    if mag > 15:
        mag = 15

    # 4 bits de magnitude
    mag_bin = format(mag, "04b")

    return f"{sinal}{mag_bin}"


def binary_to_real(b):
    """
    Converte de string binária SMMMM para valor real.
    Retorna None em caso de erro.
    """
    if b is None or len(b) != 5:
        return None

    try:
        sinal = int(b[0])
        mag = int(b[1:], 2)
    except:
        return None

    if sinal == 1:
        return float(mag)
    else:
        return -float(mag)


def fitness_function(x):
    """
    Função f(x) = x² - 4x + 4
    Retorna infinito caso x seja inválido.
    """
    if x is None:
        return float("inf")

    return (x ** 2) - (4 * x) + 4
