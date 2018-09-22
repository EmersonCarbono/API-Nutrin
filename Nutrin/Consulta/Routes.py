from flask import jsonify, request
from Nutrin import app, response


# Tipo Estado

@app.route("/tipo-estado/cadastrar", methods=["POST"])
def CreateTipoEstadoRoute():
    from Nutrin.Consulta.Services.tipoEstado.createTipoEstado import createTipoEstado
    dados = request.get_json()
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

@app.route("/tipo-estado", methods=["GET"])
def ReadTipoEstadoRoute():
    from Nutrin.Consulta.Services.tipoEstado.readTipoEstado import readTipoEstado
    response['Status'] = "Sucesso"
    response['Dados'] = readTipoEstado()
    response['Mensagem'] = "Tipos de estado listado com sucesso"
    return jsonify(response)

@app.route("/tipo-estado/alterar", methods=["POST"])
def UpdateTipoEstadoRoute():
    from Nutrin.Consulta.Services.tipoEstado.updateTipoEstado import updateTipoEstado
    dados = request.get_json()
    id_estado = dados["id"]
    nome_novo = dados["nome_novo"]
    status, mensagem = updateTipoEstado(id_estado, nome_novo)
    if status:
        response["Status"] = "Sucesso"
        response["Dados"] = ""
        response["Mensagem"] = mensagem
        return jsonify(response)
    response["Status"] = "Erro"
    response["Dados"] = ""
    response["Mensagem"] = mensagem
    return jsonify(response)
    

# Tipo Atendimento

@app.route('/tipo-atendimento/cadastrar'. methods=["POST"])
def CreateTipoAtendimentoRoute():
    from Nutrin.Consulta.Services.TipoAtendimento.createTipoAtendimento import createTipoAtendimento
    dados = request.get_json()
    nome = dados["nome"]
    preco = dados["preco"]
    qtdRetorno = dados["qtdRetorno"]
    status, mensagem = createTipoAtendimento(nome, preco, qtdRetorno)
    if status:
        response["Status"] = "Sucesso"
        response["Dados"] = ""
        response["Mensagem"] = mensagem
        return jsonify(response)
    response["Status"] = "Erro"
    response["Dados"] = ""
    response["Mensagem"] = mensagem
    return jsonify(response)

@app.route('/tipo-atendimento/<id_atendiemnto>', defaut={'id_atendiemnto' : None
}, methods=["GET"])
def buscarTipoAtendimentoRoute(id_atendiemnto):
    from Nutrin.Consulta.Services.TipoAtendimento.readTipoAtendimento import readTipoAtendimento
    dados = request.get_json()
    status, mensagem = readTipoAtendimento(id_atendiemnto)
    if status:
        response["Status"] = "Sucesso"
        response["Dados"] = mensagem
        response["Mensagem"] = ""
        return jsonify(response)
    response["Status"] = "Erro"
    response["Dados"] = ""
    response["Mensagem"] = mensagem
    return jsonify(response)

@app.route('/tipo-atendimento/alterar'. methods=["POST"])
def updateTipoAtendimentoRoute():
    from Nutrin.Consulta.Services.TipoAtendimento.updateTipoAtendimento import updateTipoAtendimento
    dados = request.get_json()
    id_atendiemnto = daods["id"]
    nome = dados["nome"]
    preco = dados["preco"]
    qtdRetorno = dados["qtdRetorno"]
    status, mensagem = updateTipoAtendimento(nome, preco, qtdRetorno)
    if status:
        response["Status"] = "Sucesso"
        response["Dados"] = ""
        response["Mensagem"] = mensagem
        return jsonify(response)
    response["Status"] = "Erro"
    response["Dados"] = ""
    response["Mensagem"] = mensagem
    return jsonify(response)