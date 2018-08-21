import datetime

def stringToDate(data_str):
    dia = int(data_str[0:2])
    mes = int(data_str[2:4])
    ano = int(data_str[4:])
    data = datetime.datetime(ano, mes, dia)
    return data

def dateToString(data_obj):
    return data_obj.strftime("%x")

