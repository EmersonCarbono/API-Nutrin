# -*- coding: utf-8 -*-
from Nutrin.Alimentacao.Model.Refeicao import Refeicao
from Nutrin.Alimentacao.Services.Refeicao.validarNome import validarNome


def createRefeicao(nome):
    nome = nome.upper()
    if validarNome(nome):
        tipoRef = Refeicao(nome)
        from Nutrin import db
        db.session.add(tipoRef)
        db.session.commit()
        return True, "Tipo Refeição cadastrado"
    return False, "Tipo já cadastrado"
