import csv
import pandas as pd
from tabulate import tabulate
from datas import Data


class Tarefas:

    def __init__(self, identificacao, descricao, dia_semana, executar, local_tarefa, status_tarefa):
        self.identificacao = identificacao
        self.descricao = descricao
        self.dia_semana = dia_semana
        self.executar = executar
        self.local_tarefa = local_tarefa
        self.status_tarefa = status_tarefa

    @staticmethod
    def menu_opcoes():
        table = [["Adicionar Nova Tarefa: ", "1"],
                 ["Realizar Pesquisa: ", "2"],
                 ["Ver tarefas cadastradas no Sistema: ", "3"]]
        print(tabulate(table))

    def recebe_informacoes(self):
        informacoes = {"Identificação: ": self.identificacao,
                       "Descrição: ": self.descricao,
                       "Dia da semana: ": self.dia_semana,
                       "Local da Tarefa: ": self.local_tarefa,
                       "Status: ": self.status_tarefa}
        return informacoes

    def adicionando_csv(self):
        colunas = ['Identificação', 'Descrição', 'Dia do cadastro', 'Dia da execução', 'Local', 'Status']

        with open("tarefas.csv", "a", newline='') as arquivo_csv:
            escrever = csv.DictWriter(arquivo_csv, fieldnames=colunas, delimiter=',', lineterminator='\n')

            escrever.writerow({'Identificação': self.identificacao, 'Descrição': self.descricao,
                               'Dia do cadastro': Data.dia_atual(), 'Dia da execução': self.executar,
                               'Local': self.local_tarefa, 'Status': self.status_tarefa})

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


    def upper(self):
        pass

    def nova_operacao(self):
        nova_operacao = self
        if nova_operacao.upper() == 'SIM':
            return Tarefas.menu_opcoes()
        elif nova_operacao.upper() == 'NÃO':
            Tarefas.encerrar_sistema()
            exit()
        else:
            raise ValueError('Opção inválida')

    @staticmethod
    def apresenta_tarefas_cadastradas():
        apresenta_tabela = pd.read_csv("tarefas.csv")
        table_apresenta_tabela = pd.DataFrame(data=apresenta_tabela, columns=['identificação', 'Descrição', 'Local',
                                                                              'Dia da execução', 'Status'])

        print(tabulate(table_apresenta_tabela))

    @staticmethod
    def encerrar_sistema():
        print('Obrigado por utilizar o sistema.')
