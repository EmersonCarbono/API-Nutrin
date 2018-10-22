from Nutrin.Consulta.Model.Horarios import Horarios
from Nutrin import db
from Nutrin.Controle.converter_data import *

def readHorario(data, horaInicio, horaFim, f =False):
    dataObj = stringToDate(data)
    horaI = stringToTime(horaInicio)
    horaF = stringToTime(horaFim)
    h = db.session.query(Horarios).filter(data==data)
    print(h)
    if h != None:
        if f:
            return True, h
        else:
            hora = {
                'hora_id' : h.id,
                'data' : h.data,
                'horaInicio' : h.horaInicio,
                'horaFim' : h.horaFim
            }
        return True, hora
    return False, "Período não cadastrado"

def readHorarioById(id, f= False):
    h = db.session.query(Horarios).filter(Horarios.id==id)
    if h != None:
        if f:
            return True, h
        else:
            hora = {
                'hora_id' : h.id,
                'data' : h.data,
                'horaInicio' : h.horaInicio,
                'horaFim' : h.horaFim
            }
        return True, hora
    return False, "Período não cadastrado"

