from tabulate import tabulate
from datas import Cadastro_dia
#   CRIANDO O MENU DE INTERAÇÃO COM O USUÁRIO
table = [

    ['1 ' 'Adicionar nova tarefa'],
    ['2 ' 'Pesquisar tarefas'],
    ['3 ' 'Mostrar tarefas cadastradas']

]
print(tabulate(table))