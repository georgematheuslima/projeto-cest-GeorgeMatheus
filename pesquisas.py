class Pesquisa:

    def __init__(self, opcao):
        self.opcao = opcao

    @property
    def altera_status(self):
        if self == 'sim'.upper():
            return True

        elif self == 'não'.upper():
            return False
        else:
            raise ValueError('Valor inválido')
