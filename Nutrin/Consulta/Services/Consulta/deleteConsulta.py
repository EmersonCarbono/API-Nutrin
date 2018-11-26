def deleteConsulta(id_consulta):
    from Nutrin.Consulta.Services.Consulta.readConsulta import readConsultaId
    status, consulta = readConsultaId(id_consulta, True)
    if status:
        from Nutrin import db
        from Nutrin.Consulta.Services.Ocupado.readOcupado import readOcupado
        ocupStatus, ocup = readOcupado(consulta.horario_id, True)
        if ocupStatus:
            db.session.delete(ocup)
        db.session.delete(consulta)
        db.session.commit()
        return True, "Periodo excluido"
    return status, consulta



