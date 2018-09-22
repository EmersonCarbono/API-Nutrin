def updateTipoAtendimento(id_atendiemnto, nome, preo, qtdRetorno):
    from Nutrin.Consulta.Services.TipoAtendimento.readTipoAtendimento import readTipoAtendimento
    tipo_atendimento = readTipoAtendimento(True, id_tipo)
    if tipo_atendimento.nome != nome:
        from Nutrin.Consulta.Services.TipoAtendimento.validarNome import validarNome
        if not validarNome:
            return False, "Nome do tipo atendimento já existe"
    tipo_atendimento.nome = nome
    tipo_atendimento.preco = preco
    tipo_atendimento.qtdRetorno = qtdRetorno
    from Nutrin import db
    db.session.commit()
    return True, "Tipo atendimento alterado com sucesso"


    
