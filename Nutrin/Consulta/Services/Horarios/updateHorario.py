from Nutrin import db
from Nutrin.Consulta.Services.Horarios.validaHorario import validaHorario

def updateHorario(data, hora, verdade):
    false se for true

    status, dado = validaHorario(data, hora)
    if status:
        #Disponivel para virar true
        if status == !verdade:
            return False, 
    return 
    dado.utilizado = verdade
    db.session.commit()

    if verdade:
        return True, "Horário agora esta sendo utilizado"
    return True, "Horário disponóvel para utilização"



