from src import config
from src.config import Operacao
from src.perceptron import Neuronio


class RedeNeuralService:
    def __init__(self, option: Operacao):
        self.option = option

        self.neuronio = Neuronio(
            treinamento=self._get_treino(),
            option=self.option,
            possiveis_entradas=[config.ATIVADO, config.DESATIVADO],
            max_epocas=config.QNT_MAX_EPOCAS,
            taxa_de_aprendizagem=config.TAXA_APRENDIZAGEM
        )

    def _get_treino(self):
        if self.option == Operacao.OR:
            return config.OR
        elif self.option == Operacao.AND:
            return config.AND
        elif self.option == Operacao.NOR:
            return config.NOR
        elif self.option == Operacao.XOR:
            return config.XOR
        elif self.option == Operacao.NAND:
            return config.NAND

    def validar(self, a, b):
        return self.neuronio.resultado(a, b)
