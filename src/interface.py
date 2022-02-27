from src.config import Operacao
from src.services import RedeNeuralService


class Interface:
    """
    Classe principal com interface no terminal para selecionar o tipo
    de operação realizada.
    """
    user_option: Operacao
    rede_neural_serive = RedeNeuralService()

    def run(self):
        self.user_option = self.get_opcao_do_usuario()

        a, b = self.get_valores_do_usuario()
        result = self.rede_neural_serive.validar(a, b, self.user_option)
        self.show_resultado(result)

    def menu(self):
        """
        Cria uma string de menu com as opções de input do usuário
        """

        return '\n'.join(map(
            lambda opt: f'[{opt.value}] - {opt.name}',
            Operacao.ordenados()
        ))

    def get_opcao_do_usuario(self) -> Operacao:
        """
        Retorna a respectiva Operacao selecionada pelo usuário,
        será solicitado enquanto o usuário não digitar uma opção válida
        """

        def get_input():
            print('\n' + self.menu())
            return int(input('Escolha uma opção: '))

        value = get_input()
        if value not in Operacao.todos_valores():
            print('Opção inválida.\n')
            value = get_input()

        return Operacao(value)

    def get_valores_do_usuario(self):
        return int(input('Digite o valor de A: ')), \
               int(input('Digite o valor de B: '))

    def show_resultado(self, result):
        """Mostra ao usuário o resultado do neurônio"""
        value = result.value
        print('Resultado: ', value)
