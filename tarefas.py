from datas import Data
import csv
from tabulate import tabulate


class Tarefas:

    def __init__(self, identificacao, descricao, dia_semana, executar, local_tarefa, status_tarefa):
        self.identificacao = identificacao
        self.descricao = descricao
        self.dia_semana = dia_semana
        self.executar = executar
        self.local_tarefa = local_tarefa
        self.status_tarefa = status_tarefa

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
    def menu_opcoes():
        table = [["Adicionar Nova Tarefa: ", "1"],
                 ["Realizar Pesquisa: ", "2"],
                 ["Ver tarefas cadastradas no Sistema: ", "3"]]
        print(tabulate(table))

    def nova_operacao(self):
        nova_operacao = input(self)
        if nova_operacao.upper() == 'SIM':
            return self.menu_opcoes()
        elif nova_operacao.upper() == 'NÃO':
            Tarefas.encerrar_sistema()
        else:
            raise ValueError ('Opção inválida')
    @staticmethod
    def encerrar_sistema():
        print('Obrigado por utilizar o sistema.')