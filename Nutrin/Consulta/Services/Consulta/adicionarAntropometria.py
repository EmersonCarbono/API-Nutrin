def adicionarAntropometria(id_consulta, id_antropometria):
    from Nutrin.Consulta.Services.Consulta.readConsulta import readConsultaId
    status, consulta = readConsultaId(id_consulta, True)
    print(consulta.antropometria_id)
    if status:
        consulta.antropometria_id = id_antropometria
        from Nutrin import db
        db.session.commit()
        print(consulta.antropometria_id)
        return True, "Antropometria adicionada com sucesso"
    return False, "Consulta não enconstrada"

