def updateConsulta(id_consulta, paciente_id, tipoAtendimento_id, horario_id, tipoEstado_id, pagamento ):
    from Nutrin.Consulta.Services.Consulta.readConsulta import readConsultaId
    status, c = readConsultaId(id_consulta,True)
    if status:
        c.paciente_id = paciente_id
        c.tipoAtendimento_id = tipoAtendimento_id
        c.horario_id = horario_id
        c.tipoEstado_id = tipoEstado_id
        c.pagamento = pagamento
        from Nutrin import db
        db.session.commit()
        return True, "Consulta alterada com sucesso"
    return False, "Consulta não encontrada"

def updateHorarioConsulta(id_consulta, paciente_id, tipoAtendimento_id, horario_id, tipoEstado_id, pagamento ):
    from Nutrin.Consulta.Services.Consulta.readConsulta import readConsultaId
    status, c = readConsultaId(id_consulta,True)
    if status:
        c.paciente_id = paciente_id
        c.tipoAtendimento_id = tipoAtendimento_id
        c.horario_id = horario_id
        c.tipoEstado_id = tipoEstado_id
        c.pagamento = pagamento
        from Nutrin import db
        db.session.commit()
        return True, "Consulta alterada con sucesso"
    return False, "Consulta não encontrada"

def updateAntropometriaConsulta(id_consulta, paciente_id, tipoAtendimento_id, horario_id, tipoEstado_id, pagamento ):
    from Nutrin.Consulta.Services.Consulta.readConsulta import readConsultaId
    status, c = readConsultaId(id_consulta,True)
    if status:
        c.paciente_id = paciente_id
        c.tipoAtendimento_id = tipoAtendimento_id
        c.horario_id = horario_id
        c.tipoEstado_id = tipoEstado_id
        c.pagamento = pagamento
        from Nutrin import db
        db.session.commit()
        return True, "Consulta alterada con sucesso"
    return False, "Consulta não encontrada"

def updateDietaConsulta(id_consulta, paciente_id, tipoAtendimento_id, horario_id, tipoEstado_id, pagamento ):
    from Nutrin.Consulta.Services.Consulta.readConsulta import readConsultaId
    status, c = readConsultaId(id_consulta,True)
    if status:
        c.paciente_id = paciente_id
        c.tipoAtendimento_id = tipoAtendimento_id
        c.horario_id = horario_id
        c.tipoEstado_id = tipoEstado_id
        c.pagamento = pagamento
        from Nutrin import db
        db.session.commit()
        return True, "Consulta alterada con sucesso"
    return False, "Consulta não encontrada"







