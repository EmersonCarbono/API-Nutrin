def createConsulta(paciente_id, tipoAtendimento_id, hora, data, tipoEstado_id):
    from Nutrin.Consulta.Model.Consulta import Consulta
    consulta = Consulta(paciente_id, tipoAtendimento_id, hora, data, tipoEstado_id)
    from Nutrin import db
    db.session.add(consulta)
    db.session.commit()
    return True, "Consulta cadastrada com sucesso"
