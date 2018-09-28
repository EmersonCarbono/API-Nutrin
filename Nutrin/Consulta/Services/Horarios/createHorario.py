from Nutrin.Consulta.Model.Horarios import Horarios
from Nutrin.Consulta.Services.Horarios.readHorario import readHorario
from Nutrin import db

def createHorario(data, hora):
    status, dado = readHorario(data, hora)
    if status:
        return False, "Horário já está cadastrado como disponível"
    else:
        horario = Horarios(data, hora)
        db.session.add(horario)
        db.session.commit()
        return True, "Horário cadastrado com sucesso!"
    

        