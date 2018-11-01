# -*- coding: utf-8 -*-
from Nutrin import db

def updateRefeicao(id_tipo_ref, novo_nome):
    from Nutrin.Alimentacao.Services.Refeicao.readRefeicao import readRefeicao
    from Nutrin.Alimentacao.Services.Refeicao.validarNome import validarNome
    novo_nome = novo_nome.upper()
    refeicao = readRefeicao(True)
    if validarNome(novo_nome):
        for t in refeicao:
            if t.id == id_tipo_ref:
                t.nome = novo_nome
                db.session.commit()
                return True, "Tipo refeição alterado com sucesso"
        return False , "Tipo refeição não encontrado"
    return False, "Nome do tipo refeição ja existe"