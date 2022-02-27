import enum
import random


class Resultado(enum.Enum):
    ATIVADO = 1
    DESATIVADO = 0


class Perceptron:
    bias_value = -1

    def __init__(self, treinamento, possiveis_entradas, option, max_epocas,
                 taxa_de_aprendizagem):
        self.taxa_de_aprendizagem = taxa_de_aprendizagem
        self.treinamento = treinamento
        self.option = option
        self.possiveis_entradas = possiveis_entradas

        self.max_epocas = max_epocas

        self.pesos = self._get_pesos_iniciais()
        self.treinar()

    def resultado(self, a, b) -> Resultado:
        amostra = self.criar_amostra(a, b)
        soma = self.somatorio(amostra)
        return Resultado(soma)

    def treinar(self):
        print(f'treinando a neurônio de {self.option} ...')

        epoca = 0
        while True:
            sem_error = True

            for treino in self.treinamento:
                amostra = self.criar_amostra(treino.a, treino.b)

                soma = self.somatorio(amostra)
                if soma != treino.esperado:
                    self.ajustar_pesos(soma, treino.esperado, amostra)
                    sem_error = False

            epoca += 1

            if sem_error or epoca >= self.max_epocas:
                break
        print(f'Treino finalizado com {epoca} épocas !')

    def somatorio(self, amostra):
        soma = sum(
            amostra[i] * self.pesos[i]
            for i in range(len(amostra))
        )
        return self.degrau(soma)

    def ajustar_pesos(self, degrau, esperado, amostra):
        """Atualiza os pesos utilizando regra Delta"""
        error = esperado - degrau
        for i in range(len(self.pesos)):
            delta = (self.taxa_de_aprendizagem * esperado - degrau) * amostra[i]
            self.pesos[i] += delta

    def degrau(self, somatorio):
        return 1 if somatorio > 0 else 0

    def criar_amostra(self, a, b):
        return [a, b, self.bias_value]

    def _get_pesos_iniciais(self):
        """
        Retorna valores aleatórios entre [-1, 0, 1]
        para cada uma das entradas + bias
        """

        bias = 1
        qnt_pesos = len(self.possiveis_entradas) + bias
        # bias também deve possuir um peso

        return [
            random.choice([-1, 0, 1])
            for _ in range(qnt_pesos)
        ]


class Neuronio(Perceptron):
    """
    Classe de domínio para uma melhor escrita do código
    criando um neuronio Perceptron
    """
    pass
