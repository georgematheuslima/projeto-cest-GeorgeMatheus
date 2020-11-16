from datetime import date, datetime


class Data:

    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    @staticmethod
    def dia_atual():
        now = datetime.now()
        dia_formatado = f'{now.day}/{now.month}/{now.year}'
        return dia_formatado

    def executar_tarefa(dia, mes, ano):
        DIAS = [
            'Segunda-feira',
            'Terça-feira',
            'Quarta-feira',
            'Quinta-Feira',
            'Sexta-feira',
            'Sábado',
            'Domingo'
        ]

        data = date(day=dia, month=mes, year=ano)
        data_formatada = ('{}/{}/{}'.format(dia, mes, ano))
        print(data_formatada)

        indice_da_semana = data.weekday()

        dia_da_semana = DIAS[indice_da_semana]
        print(dia_da_semana)

        return data_formatada

