

class Tarefas:

    def __init__(self,identificacao, descricao, dia_semana, local_tarefa, status_tarefa):
        self.identificacao = identificacao
        self.descricao = descricao
        self.dia_semana = dia_semana
        self.local_tarefa = local_tarefa
        self.status_tarefa = status_tarefa

    def recebe_informacoes(self):
        informacoes = {"Identificação: ":self.identificacao,
                       "Descrição: ":self.descricao,
                       "Dia da semana: ":self.dia_semana,
                       "Local da Tarefa: ":self.local_tarefa,
                       "Status: ":self.status_tarefa}
        return informacoes




arquivo = open("tarefas.txt", "a")

