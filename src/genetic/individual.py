# classe do indivíduo

from .utils import real_to_binary, binary_to_real, fitness_function

class Individual:
    def __init__(self, value):
        # valor real que o AG manipula
        self.value = value

        # representações exigidas pelo trabalho
        self.binary = None
        self.decoded_value = None

        # resultado do fitness
        self.fitness = None

    def encode(self):
        """
        Converte o valor real para binário (5 bits).
        Como o trabalho usa apenas 5 bits, o valor real
        precisa ser ajustado para o intervalo válido.
        """
        try:
            self.binary = real_to_binary(self.value)
        except Exception:
            # fallback para evitar crash inicial
            self.binary = "10000"  # 0 no intervalo

    def decode(self):
        """
        Converte binário para valor real aproximado.
        """
        if self.binary is None:
            return

        try:
            self.decoded_value = binary_to_real(self.binary)
        except Exception:
            # fallback caso o binário esteja incorreto
            self.decoded_value = 0

    def evaluate(self):
        """
        Codifica, decodifica e avalia o fitness no valor convertido.
        """
        self.encode()
        self.decode()

        if self.decoded_value is None:
            self.fitness = float("inf")
        else:
            self.fitness = fitness_function(self.decoded_value)
