from Nutrin.Consulta.Model.Horarios import Horarios
from Nutrin import db

def readHorario(data, horaInicio, horaFim, f =False):
    h = Horarios.query().filter(data==data, horaInicio==horaInicio, horaFim==horaFim)
    if h != None:
        if f:
            return True, h
        else:
            hora = {
                'hora_id' = h.id,
                'data' = h.data,
                'horaInicio' = h.horaInicio,
                'horaFim' = h.horaFim
            }
        return True, hora
    return False, "Período não cadastrado"

