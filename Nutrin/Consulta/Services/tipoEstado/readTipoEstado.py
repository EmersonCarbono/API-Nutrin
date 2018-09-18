from Nutrin.Consulta.Model.TipoEstado import TipoEstado

def readTipoEstado(f=False):
    tipos_estado = TipoEstado.query.all()
    if f:
        return tipos_estado
    tipos_estado_dic = []
    for t in tipos_estado:
        tipos_estado_dic.append({
            'id': t.id,
            'nome': t.nome
        })
    return tipos_estado_dic