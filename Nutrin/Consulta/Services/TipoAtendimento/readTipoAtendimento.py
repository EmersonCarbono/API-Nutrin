def buscarTipoAtendimento(tipo_atendimento, id_tipo):
    for t in tipo_atendimento:
        if t.id == id_tipo:
            if f:
                return True, t
            return True, {
                'id': t.id,
                'nome': t.nome,
                'preco': t.preco,
                'qtdRetorno': t.qtdRetorno
            }
    return False, 'Tipo atendimento não existe'

def readTipoAtendimento(f = False, id_tipo = None):
    from Nutrin.Consulta.Model.TipoAtendimento import TipoAtendimento
    tipo_atendimento = TipoAtendimento.query.all()
    if id_tipo != None:
        return buscarTipoAtendimento(tipo_atendimento, id_tipo)
    if f:
        return True, tipo_atendimento
    tipo_atendimento_dic = []
    for t in tipo_atendimento:
        tipo_atendimento_dic.append({
            'id': t.id,
            'nome': t.nome,
            'preco': t.preco,
            'qtdRetorno': t.qtdRetorno
        })
    return True, tipo_atendimento_dic