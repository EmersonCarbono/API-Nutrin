from flask import jsonify, request
from Nutrin import app, response

@app.route("/tipo-estado/cadastrar", methods=["POST"])
def CreateTipoEstado():
    from Nutrin.Consulta.Services.TipoEstado.createTipoEstado import createcriarTipoEstadoTipoEstado
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

