from Nutrin import db
from Nutrin.Consulta.Services.Horarios.readHorario import readHorario

def deleteHorario(data, hora):
    status, dado = readHorario(data, horaInicio, horaFim, True)
    if status:
        if dado.utilizado:
            return False, "Não é possivel excluir. Há um paciente utilizando o horário"
        else:
            db.session.delete(dado)
            db.session.commit()
            return True, "Periodo excluido"
    return status, dado
    