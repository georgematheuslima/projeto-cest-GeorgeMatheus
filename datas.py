from datetime import date
def Cadastro_dia(day, month, year):
    DIAS = [
        'Segunda-feira',
        'Terça-feira',
        'Quarta-feira',
        'Quinta-Feira',
        'Sexta-feira',
        'Sábado',
        'Domingo'
    ]


    # aplicando as datas no método date
    data = date(year=year, month=month, day=day)

    #convertendo ao método brasileiro
    padrao_brasil = data.strftime('%d/%m/%Y')
    print(padrao_brasil)

    # apresentando o dia da semana.
    indice_da_semana = data.weekday()

    # printando o dia da semana.
    dia_da_semana = DIAS[indice_da_semana]
    print(dia_da_semana)

