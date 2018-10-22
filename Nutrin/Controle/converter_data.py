import datetime
from dateutil.parser import parse

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

def timeToString(time_obj):
    hora = time_obj.strftime("%H")
    minuto = time_obj.strftime("%M")
    return str("{}:{}".format(hora,minuto))


def stringToTime(time_str):
    datetime_format = "%H:%M"
    #return datetime.strptime(time_str, datetime_format)
    return parse(time_str)
