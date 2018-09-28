from Nutrin import db
from Nutrin.Consulta.Services.Horarios.readHorario import readHorario

def deleteHorario(data, hora):
    status, dado = readHorario(data, hora, True)
    if status:
        db.session.delete(dado)
        db.session.commit()
        return True, "Horário excluido"
    return status, dado

    

