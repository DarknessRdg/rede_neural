from typing import List

from src import config
from src.config import Operacao
from src.perceptron import Neuronio


class TestCaseNeuronio:
    operacao: Operacao
    cases: List[config.EntradaDeTreino]

    def setUp(self) -> None:
        self.neuronio = Neuronio(
            taxa_de_aprendizagem=config.TAXA_APRENDIZAGEM,
            max_epocas=config.QNT_MAX_EPOCAS,
            possiveis_entradas=[config.ATIVADO, config.DESATIVADO],
            option=self.operacao,
            treinamento=self.cases
        )

    def test_esperado_resultado_de_amostragem(self):
        for case in self.cases:
            result = self.neuronio.resultado(case.a, case.b)
            self.assertEqual(
                result.value, case.esperado,
                f'Valores de entrada: a={case.a}, b={case.b}'
            )

