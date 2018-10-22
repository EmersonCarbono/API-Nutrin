from Nutrin import db
from Nutrin.Consulta.Services.Ocupado.readOcupado import readOcupadoNoPeriodo
from Nutrin.Consulta.Model.Ocupado import Ocupado


def createOcupado(periodo_id,hI,hF):
    status, dado = readOcupadoNoPeriodo(periodo_id)
    if status:
        for ocup in dado:
            if hF >= ocup['horaI'] and hI <= ocup['horaF']:
                permissao = True
            else:
                return False, "Horário esta ocupado"
    elif status == False or permissao:
        o = Ocupado(periodo_id, hI, hF)
        db.session.add(o)
        db.session.commit()
        return True, "Horário foi preenchido com sucesso"

#se no dia ha algum ocupado
#se sim verifica se é o mesmo horario
14:00 as 16:00
