import datetime

def stringToDate(data_str):
    dia = int(data_str[0:2])
    mes = int(data_str[2:4])
    ano = int(data_str[4:8])
    data = datetime.datetime(ano, mes, dia)
    return data

def dateToString(data_obj):
    dia = data_obj.strftime("%d")
    mes = data_obj.strftime("%m")
    ano =data_obj.strftime("%Y")
    return str("{}-{}-{}".format(ano,mes,dia))

