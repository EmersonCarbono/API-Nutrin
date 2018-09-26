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
  
# Antropometria

@app.route('/antropometria/cadastrar'. methods=["POST"])
def createAntropometriaRoute():
    from Nutrin.Consulta.Services.Antropometria.createAntropometria import createAntropometria
    dados = request.get_json()
    peso = dados["peso"]
    braco = dados["braco"]
    torax = dados["torax"]
    cintura = dados["cintura"]
    abdomen = dados["abdomen"]
    quadril = dados["quadril"]
    coxa = dados["coxa"]
    biceps = dados["biceps"]
    triceps = dados["triceps"]
    peito = dados["peito"]
    subsCap = dados["subsCap"]
    axilar = dados["axilar"]
    gorduraPerc = dados["gorduraPerc"]
    aguaPerc = dados["aguaPerc"]
    pesoMagro = dados["pesoMagro"]
    status, mensagem = createAntropometria(peso, braco, torax, cintura, abdomen, quadril, coxa, biceps, triceps, peito, subsCap, axilar, gorduraPerc, aguaPerc, pesoMagro)
    if status:
        response["Status"] = "Sucesso"
        response["Dados"] = ""
        response["Mensagem"] = mensagem
        return jsonify(response)
    response["Status"] = "Erro"
    response["Dados"] = ""
    response["Mensagem"] = mensagem
    return jsonify(response)
        

@app.route('/antropometria/alterar'. methods=["POST"])
def updateAntropometriaRoute():
    from Nutrin.Consulta.Services.Antropometria.updateAntropometria import updateAntropometria
    dados = request.get_json()
    antropometria_id = dados["id"]
    peso = dados["peso"]
    braco = dados["braco"]
    torax = dados["torax"]
    cintura = dados["cintura"]
    abdomen = dados["abdomen"]
    quadril = dados["quadril"]
    coxa = dados["coxa"]
    biceps = dados["biceps"]
    triceps = dados["triceps"]
    peito = dados["peito"]
    subsCap = dados["subsCap"]
    axilar = dados["axilar"]
    gorduraPerc = dados["gorduraPerc"]
    aguaPerc = dados["aguaPerc"]
    pesoMagro = dados["pesoMagro"]
    status, mensagem = updateAntropometria(antropometria_id,peso, braco, torax, cintura, abdomen, quadril, coxa, biceps, triceps, peito, subsCap, axilar, gorduraPerc, aguaPerc, pesoMagro)
    if status:
        response["Status"] = "Sucesso"
        response["Dados"] = ""
        response["Mensagem"] = mensagem
        return jsonify(response)
    response["Status"] = "Erro"
    response["Dados"] = ""
    response["Mensagem"] = mensagem
    return jsonify(response)

@app.route('/antropometria/bucar/<ID>'. methods=["GET"])
def readAntropometriaRoute(ID):
    from Nutrin.Consulta.Services.Antropometria.readAntropometria import readAntropometria
    status, mensagem = readAntropometria(ID)
    if status:
        response["Status"] = "Sucesso"
        response["Dados"] = ""
        response["Mensagem"] = mensagem
        return jsonify(response)
    response["Status"] = "Erro"
    response["Dados"] = ""
    response["Mensagem"] = mensagem
    return jsonify(response)
  
@app.route('/antropometria/deletar/<ID>'. methods=["GET"])
def deleteAntropometriaRoute(ID):
    from Nutrin.Consulta.Services.Antropometria.deleteAntropometria import deleteAntropometria
    status, mensagem = deleteAntropometria(ID)
    if status:
        response["Status"] = "Sucesso"
        response["Dados"] = ""
        response["Mensagem"] = mensagem
        return jsonify(response)
    response["Status"] = "Erro"
    response["Dados"] = ""
    response["Mensagem"] = mensagem
    return jsonify(response)
