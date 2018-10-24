from Nutrin.Consulta.Services.Ocupado.createOcupado import createOcupado
from Nutrin.Consulta.Services.Ocupado.readOcupado import readOcupadoNoPeriodo
from Nutrin.Consulta.Services.Horarios.listHorario import listHorarioData

def createConsulta(paciente_id, tipoAtendimento_id, data, hI, hF, tipoEstado_id):
    statusHora, periodo = listHorarioData(data)
    if statusHora:
        status, msg = createOcupado(periodo[0]['hora_id'], hI, hF)
        if status:
            statusHid, msgHora = readOcupadoNoPeriodo(periodo_id)
            if statusHid:
                for o in msgHora:
                    if o['horaI'] == hI and o['horaF'] == hF:
                        from Nutrin.Consulta.Model.Consulta import Consulta
                        consulta = Consulta(paciente_id, tipoAtendimento_id, o['id'] , tipoEstado_id)
                        from Nutrin import db
                        db.session.add(consulta)
                        db.session.commit()
                        return True, "Consulta cadastrada com sucesso"
                    return False, 'ID Ocupado não encomtrado'
            return statusHid, msgHora
        return status, msg
    return statusHora, periodo

