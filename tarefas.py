from datas import Data
import csv

class Tarefas:

    def __init__(self, identificacao, descricao, dia_semana, executar, local_tarefa, status_tarefa):
        self.identificacao = identificacao
        self.descricao = descricao
        self.dia_semana = dia_semana
        self.executar = executar
        self.local_tarefa = local_tarefa
        self.status_tarefa = status_tarefa

    def recebe_informacoes(self):
        informacoes = {"Identificação: ":self.identificacao,
                       "Descrição: ":self.descricao,
                       "Dia da semana: ":self.dia_semana,
                       "Local da Tarefa: ":self.local_tarefa,
                       "Status: ":self.status_tarefa}
        return informacoes


    def adicionando_csv(self):
        colunas = ['identificação', 'descrição', 'Dia do cadastro','Dia da execução' , 'Local', 'Status']

        with open("tarefas.csv", "a", newline='') as arquivo_csv:
            escrever = csv.DictWriter(arquivo_csv, fieldnames=colunas, delimiter=',', lineterminator='\n')

            escrever.writerow({'identificação': self.identificacao, 'descrição':self.descricao,
                               'Dia do cadastro': Data.dia_atual(),'Dia da execução': self.executar,
                               'Local':self.local_tarefa, 'Status': self.status_tarefa})



