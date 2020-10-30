# RECEBENDO A ENTRADA DO USUÁRIO E ARMAZENANDO NO DICIONARIO.
from tabulate import tabulate
from tarefas import Tarefas

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

    # colocando dados em um arquivo .txt
    arquivo = open("tarefas.txt","a")
    dados = list()
    dados.append(str(identificacao ))
    dados.append(str(descricao ))
    dados.append(str(dia_semana ))
    dados.append(str(local ))
    dados.append(str(status ))
    arquivo.writelines(dados )

    arquivo = open("tarefas.txt","r")
    print(arquivo.readlines())

