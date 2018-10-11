from Nutrin.Consulta.Model.Horarios import Horarios
from Nutrin.Consulta.Services.Horarios.readHorario import readHorario
from Nutrin.Consulta.Services.Horarios.listHorario import listHorarioData, listHorario
from Nutrin import db

def validaCadastro(data, hI,hF):
    periodos = listHorarioData(periodo.data)
    permissao = None
    for p in periodos:
        if hF > p['horaInicio'] and hI < p['horaFim']:
            permissao = True
        else:
            return False
    return permissao

def createHorario(data, horaInicio, horaFim):
    status, dado = readHorario(data, horaInicio, horaFim, True)
    if status:
        return False, "Este periodo já está disponível"
    else:
        if validaCadastro(data, hI, hF):
            horario = Horarios(data, horaInicio, horaFim)
            db.session.add(horario)
            db.session.commit()
            return True, "Período cadastrado com sucesso!"
        return False, "Periodo está em conflito com outro"
    

        