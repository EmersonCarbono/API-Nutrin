def validarNome(nome):
    from Nutrin.Consulta.Services.TipoAtendimento.readTipoAtendimento import readTipoAtendimento
    tipos_atendimentos = readTipoAtendimento(True)
    for t in tipos_atendimentos:
        if nome == t.nome:
            return False
    return True