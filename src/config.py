import enum
from dataclasses import dataclass
from typing import List


QNT_MAX_EPOCAS = 10000
TAXA_APRENDIZAGEM = 0.1

ATIVADO = 0
DESATIVADO = 1

PESOS = (-1, 0, 1)


@dataclass
class EntradaDeTreino:
    a: int
    b: int
    esperado: int


OR = (
    EntradaDeTreino(a=ATIVADO, b=ATIVADO, esperado=ATIVADO),
    EntradaDeTreino(a=ATIVADO, b=DESATIVADO, esperado=ATIVADO),
    EntradaDeTreino(a=DESATIVADO, b=ATIVADO, esperado=ATIVADO),
    EntradaDeTreino(a=DESATIVADO, b=DESATIVADO, esperado=DESATIVADO),
)

AND = (
    EntradaDeTreino(a=ATIVADO, b=ATIVADO, esperado=ATIVADO),
    EntradaDeTreino(a=ATIVADO, b=DESATIVADO, esperado=DESATIVADO),
    EntradaDeTreino(a=DESATIVADO, b=ATIVADO, esperado=DESATIVADO),
    EntradaDeTreino(a=DESATIVADO, b=DESATIVADO, esperado=DESATIVADO),
)

NOR = (
    EntradaDeTreino(a=ATIVADO, b=ATIVADO, esperado=DESATIVADO),
    EntradaDeTreino(a=ATIVADO, b=DESATIVADO, esperado=DESATIVADO),
    EntradaDeTreino(a=DESATIVADO, b=ATIVADO, esperado=DESATIVADO),
    EntradaDeTreino(a=DESATIVADO, b=DESATIVADO, esperado=ATIVADO),
)

NAND = (
    EntradaDeTreino(a=ATIVADO, b=ATIVADO, esperado=DESATIVADO),
    EntradaDeTreino(a=ATIVADO, b=DESATIVADO, esperado=ATIVADO),
    EntradaDeTreino(a=DESATIVADO, b=ATIVADO, esperado=ATIVADO),
    EntradaDeTreino(a=DESATIVADO, b=DESATIVADO, esperado=ATIVADO),
)

XOR = (
    EntradaDeTreino(a=ATIVADO, b=ATIVADO, esperado=DESATIVADO),
    EntradaDeTreino(a=ATIVADO, b=DESATIVADO, esperado=ATIVADO),
    EntradaDeTreino(a=DESATIVADO, b=ATIVADO, esperado=ATIVADO),
    EntradaDeTreino(a=DESATIVADO, b=DESATIVADO, esperado=DESATIVADO),
)


class Operacao(enum.Enum):
    OR = 1
    AND = 2
    NOR = 3
    NAND = 4
    XOR = 5

    @classmethod
    def ordenados(cls) -> List['Operacao']:
        return sorted(
            cls,
            key=lambda it: it.value
        )

    @classmethod
    def todos_valores(cls) -> List[int]:
        return list(map(lambda it: it.value, cls))
