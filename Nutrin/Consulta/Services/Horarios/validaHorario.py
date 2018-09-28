from Nutrin.Consulta.Model.Horarios import Horarios
from Nutrin.Consulta.Services.Horarios.readHorario import readHorario
from Nutrin import db

def validaHorario(data, hora):
    status, dado = readHorario(data, hora)
    if status:
        if dado('utilizado'):
            return False, "Horário já esta sendo utilizado"
        return True, "Horário disponível para agendamento"



