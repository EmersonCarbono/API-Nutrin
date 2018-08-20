def converterData(data_str):
    import datetime
    dia = int(data_str[0:2])
    mes = int(data_str[2:4])
    ano = int(data_str[4:])
    data = datetime.datetime(ano, mes, dia)
    return data
