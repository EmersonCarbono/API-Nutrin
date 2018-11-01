# -*- coding: utf-8 -*-
from flask import jsonify, request
from Nutrin import app
from Nutrin import response


#Tipo Refeição

@app.route('tipo-refeicao/cadastrar', methods=['POST'])
def cadastrarTipoRefeicao():
    from Nutrin.Alimentacao.Services.TipoRefeicao.createTipoRefeicao import createTipoRefeicao 
    dados = request.get_json()
    nome = dados["nome"]
    status, mensagem = createTipoRefeicao(nome)
    if status:
        response["Status"] = "Sucesso"
        response["Dados"] = ""
        response["Mensagem"] = mensagem
        return jsonify(response)
    response["Status"] = "Erro"
    response["Dados"] = ""
    response["Mensagem"] = mensagem
    return jsonify(response)

@app.route('tipo-refeicao', methods=['GET'])
def buscarTipoRefeicao():
    from Nutrin.Alimentacao.Services.TipoRefeicao.readTipoRefeicao import readTipoRefeicao 
    response["Status"] = "Sucesso"
    response["Dados"] = readTipoRefeicao
    response["Mensagem"] = mensagem
    return jsonify(response)

@app.route('tipo-refeicao/alterar', methods=['POST'])
def alterarTipoRefeicao():
    from Nutrin.Alimentacao.Services.TipoRefeicao.updateTipoRefeicao import updateTipoRefeicao 
    dados = request.get_json()
    id_tipoRef = dados['id']
    nome = dados["nome_novo"]
    status, mensagem = updateTipoRefeicao(id_tipoRef,nome)
    if status:
        response["Status"] = "Sucesso"
        response["Dados"] = ""
        response["Mensagem"] = mensagem
        return jsonify(response)
    response["Status"] = "Erro"
    response["Dados"] = ""
    response["Mensagem"] = mensagem
    return jsonify(response)

# Refeições

@app.route('refeicao/cadastrar', methods=['POST'])
def cadastrarRefeicao():
    from Nutrin.Alimentacao.Services.TipoRefeicao.createTipoRefeicao import createTipoRefeicao 
    dados = request.get_json()
    nome = dados["nome"]
    status, mensagem = createTipoRefeicao(nome)
    if status:
        response["Status"] = "Sucesso"
        response["Dados"] = ""
        response["Mensagem"] = mensagem
        return jsonify(response)
    response["Status"] = "Erro"
    response["Dados"] = ""
    response["Mensagem"] = mensagem
    return jsonify(response)





@app.route("/tipo-estado/cadastrar", methods=["POST"])
def CreateTipoEstadoRoute():
    from Nutrin.Consulta.Services.TipoEstado.createTipoEstado import createTipoEstado
    dados = request.get_json(force=True)
    nome = dados["nome"]
    status, mensagem = createTipoEstado(nome)
    if status:
        response["Status"] = "Sucesso"
        response["Dados"] = ""
        response["Mensagem"] = mensagem
        return jsonify(response)
    response["Status"] = "Erro"
    response["Dados"] = ""
    response["Mensagem"] = mensagem
    return jsonify(response)
