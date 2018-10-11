def updateConsulta(id_consulta, paciente_id, tipoAtendimento_id, hora, data, tipoEstado_id, antropometria_id, dieta, pagamento ):
    from Nutrin.Consulta.Services.Consulta.readConsulta import readConsulta
    consultas = readConsulta(True)
    for c in consultas:
        if c.id == id_consulta:
            c.paciente_id = paciente_id
            c.tipoAtendimento_id = tipoAtendimento_id
            c.hora = hora
            c.data = data
            c.tipoEstado_id = tipoEstado_id
            c.antropometria_id = antropometria_id
            c.dieta = dieta
            c.pagamento = pagamento
            from Nutrin import db
            db.session.commit()
            return True, "Consulta alterada con sucesso"
    return False, "Consulta não encontrada"

