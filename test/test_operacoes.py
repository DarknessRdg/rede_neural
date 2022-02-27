from unittest import TestCase

from src import config
from test.utils import TestCaseNeuronio


class TestUsandoOR(TestCaseNeuronio, TestCase):
    operacao = config.Operacao.OR
    cases = config.OR


class TestUsandoAND(TestCaseNeuronio, TestCase):
    operacao = config.Operacao.AND
    cases = config.AND


class TestUsandoNOR(TestCaseNeuronio, TestCase):
    operacao = config.Operacao.NOR
    cases = config.NOR


class TestUsandoNAND(TestCaseNeuronio, TestCase):
    operacao = config.Operacao.NAND
    cases = config.NAND


class TestUsandoXOR(TestCaseNeuronio, TestCase):
    operacao = config.Operacao.XOR
    cases = config.XOR



