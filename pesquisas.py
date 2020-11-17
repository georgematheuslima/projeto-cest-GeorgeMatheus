import pandas as pd


class Pesquisa:

    def __init__(self, opcao, pesquisar_tarefas, apresentar_colunas):
        self.opcao = opcao
        self.pesquisar_tarefas = pesquisar_tarefas
        self.apresentar_colunas = apresentar_colunas

    @staticmethod
    def apresentar_tarefas():
        pesquisar_tarefas = pd.read_csv("tarefas.csv")
        apresentar_colunas = pd.DataFrame(data=pesquisar_tarefas, columns=['Descrição', 'Status'])
        print(apresentar_colunas)

    def pesquisa_tarefas(self):
        pesquisar_tarefas = pd.read_csv("tarefas.csv")
        indice_da_pesquisa = (self)
        apresentar_tarefa = pesquisar_tarefas.loc[indice_da_pesquisa]
        print(apresentar_tarefa)
