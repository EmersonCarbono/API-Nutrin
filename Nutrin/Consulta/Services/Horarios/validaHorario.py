from Nutrin.Consulta.Model.Horarios import Horarios
from Nutrin.Consulta.Services.Horarios.readHorario import readHorario
from Nutrin import db

def validaHorario(data, hora):
    status, dado = readHorario(data, hora)
    if status:
        if dado['utilizado']:
            return True, "Horário já esta sendo utilizado"
        return False, "Horário disponível para agendamento"
    return None, dado



