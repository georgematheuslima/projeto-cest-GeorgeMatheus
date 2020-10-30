# RECEBENDO A ENTRADA DO USUÁRIO E ARMAZENANDO NO DICIONARIO.
from tabulate import tabulate
from tarefas import Tarefas
import csv

table = [["Adicionar Nova Tarefa: ", "1"],
         ["Realizar Pesquisa: ", "2"],
         ["Ver tarefas cadastradas no Sistema: ", "3"]]
print(tabulate(table))

opcao = int(input('Digite a opção desejada: '))

if opcao == 1:
    confirma = print('Adicionar Nova tarefa.')
    identificacao = int(input('Digite a identificação numerica da tarefa: '))
    descricao = input('Descrição da tarefa: ')
    dia_semana = input('Dia da semana: ')
    local = input('Local da tarefa: ')
    status = input('Status da tarefa: ')
    tarefas = Tarefas(identificacao, descricao, dia_semana, local, status)

    # colocando dados em um arquivo .csv

    with open("tarefas.csv", "w", newline='') as arquivo_csv:
        colunas = ['identificação', 'descrição', 'Dia da semana', 'Local', 'Status']

        escreva = csv.DictWriter(arquivo_csv, fieldnames=colunas, delimiter=',', lineterminator='\n')

        escreva.writeheader()

        escreva.writerow({'identificação': identificacao,'descrição': descricao,
                         'Dia da semana': dia_semana, 'Local': local, 'Status':status})











