def readConsulta(f=False):
    from Nutrin.Consulta.Model.Consulta import Consulta
    consultas = Consulta.query.all()
    if f:
        return consultas
    consulas_dic = []
    for c in consultas:
        consulas_dic.append({
            'id': c.id,
            'paciente_id': c.paciente_id,
            'tipoAtendimento_id': c.tipoAtendimento_id
            'hora': c.hora
            'data': c.data
            'tipoEstado_id': c.tipoEstado_id
            'antropometria_id': c.antropometria_id
            'dieta': c.dieta
            'pagamento': c.pagamento
        })
    return True, consulas_dic
