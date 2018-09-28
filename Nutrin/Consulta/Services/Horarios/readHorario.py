from Nutrin.Consulta.Model.Horarios import Horarios
from Nutrin import db

def readHorario(data, hora, f =False):
    h = Horarios.query().filter(data==data, hora==hora)
    if h != None:
        if f:
            return True, h
        else:
            hora = {
                'hora_id' = h.id,
                'data' = h.data,
                'hora' = h.hora,
                'utilizado' = h.utilizado
            }
        return True, hora
    return False, "Horário não cadastrado"

