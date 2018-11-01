# -*- coding: utf-8 -*-
from Nutrin.Alimentacao.Model.Anamnese import Anamnese
from Nutrin.Alimentacao.Services.Anamnese.validarNome import validarNome


def createAnamnese(paciente_id, qtdAtividadeFisica, tipoExercicio, horaAcorda,padraoRefeicao,deficienciaAlimentacaoDiaria,necessitaSuplementoAlimentar,retencaoLiquido,alergiaRemedio,alergiaSuplemento,intoleranciaAlimentar,problemaSaude,problemaSaudeFamilia,medicacao,suplementacao):
    nome = nome.upper()
    if validarNome(nome):
        tipoRef = Anamnese(nome)
        from Nutrin import db
        db.session.add(tipoRef)
        db.session.commit()
        return True, "Tipo Refeição cadastrado"
    return False, "Tipo já cadastrado"
