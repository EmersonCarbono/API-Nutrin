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

@app.route('/tipo-atendimento/cadastrar', methods=["POST"])
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

@app.route('/tipo-atendimento/buscar', methods=["POST"])
def buscarTipoAtendimentoRoute():
    from Nutrin.Consulta.Services.TipoAtendimento.readTipoAtendimento import readTipoAtendimento
    print("ATé aqui foi")
    dados = request.get_json()
    id_atendiemnto = dados["id_atual"]
    status, mensagem = readTipoAtendimento(False, id_atendiemnto)
    if status:
        response["Status"] = "Sucesso"
        response["Dados"] = mensagem
        response["Mensagem"] = ""
        return jsonify(response)
    response["Status"] = "Erro"
    response["Dados"] = ""
    response["Mensagem"] = mensagem
    return jsonify(response)

@app.route('/tipo-atendimento/alterar', methods=["POST"])
def updateTipoAtendimentoRoute():
    from Nutrin.Consulta.Services.TipoAtendimento.updateTipoAtendimento import updateTipoAtendimento
    dados = request.get_json()
    id_atendiemnto = dados["id_atendiemnto"]
    nome = dados["nome"]
    preco = dados["preco"]
    qtdRetorno = dados["qtdRetorno"]
    status, mensagem = updateTipoAtendimento(id_atendiemnto, nome, preco, qtdRetorno)
    if status:
        response["Status"] = "Sucesso"
        response["Dados"] = ""
        response["Mensagem"] = mensagem
        return jsonify(response)
    response["Status"] = "Erro"
    response["Dados"] = ""
    response["Mensagem"] = mensagem
    return jsonify(response)