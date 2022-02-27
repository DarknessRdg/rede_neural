from src import config
from src.config import Operacao
from src.perceptron import Neuronio


class RedeNeuralService:

    def _get_treino(self, operacao):
        if operacao == Operacao.OR:
            return config.OR
        elif operacao == Operacao.AND:
            return config.AND
        elif operacao == Operacao.NOR:
            return config.NOR
        elif operacao == Operacao.XOR:
            return config.XOR
        elif operacao == Operacao.NAND:
            return config.NAND

    def validar(self, a, b, operacao: Operacao):
        if operacao == Operacao.XOR:
            return self.validar_xor(a, b)

        return self.get_neuronio(operacao).resultado(a, b)

    def validar_xor(self, a, b):
        _nand = self.get_neuronio(Operacao.NAND)
        _or = self.get_neuronio(Operacao.OR)

        resultado_nand = _nand.resultado(a, b)
        resultado_or = _or.resultado(a, b)

        a, b = resultado_nand.value, resultado_or.value
        return self.get_neuronio(Operacao.AND).resultado(a, b)

    def get_neuronio(self, operacao):
        return Neuronio(
            treinamento=self._get_treino(operacao),
            option=operacao,
            possiveis_entradas=[config.ATIVADO, config.DESATIVADO],
            max_epocas=config.QNT_MAX_EPOCAS,
            taxa_de_aprendizagem=config.TAXA_APRENDIZAGEM
        )
