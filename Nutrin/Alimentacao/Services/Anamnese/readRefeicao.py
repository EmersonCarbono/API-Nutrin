# -*- coding: utf-8 -*-
from Nutrin.Alimentacao.Model.Refeicao import Refeicao

def readRefeicao(f=False):
    refeicao = Refeicao.query.all()
    print(type(refeicao))
    if f:    
        return refeicao
    refeicao_dic = []
    for t in refeicao:
        refeicao_dic.append({
            'id': t.id,
            'nome': t.nome
        })
    return refeicao_dic

def readRefeicaoById(id_Ref):
    return Refeicao.query.get(id_Ref)


