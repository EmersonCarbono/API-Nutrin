from Nutrin import db
from Nutrin.Consulta.Services.Horarios.validaHorario import validaHorario

def updateHorario(data, hora, verdade):
    false se for true

    status, dado = validaHorario(data, hora)
    if status:
        if verdade:
            return False, "Horário já está sendo utilizado"
        else:
            dado.utilizado = verdade
            db.session.commit()
            return True, "Horário foi liberado"
    elif status == False:
        if verdade:
            dado.utilizado = verdade
            db.session.commit()
            return True, "Horário foi ocupado"
        return False, "Horario já esta liberado"
    return False, dado




