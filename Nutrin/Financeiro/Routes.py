# -*- coding: utf-8 -*-
from flask import jsonify, request
from Nutrin import app
from Nutrin import response

@app.route('/lucros', methods=['GET'])
def lucroRoute():
    from Nutrin.Financeiro.Services.lucroMensal import pagamentosConsultas
    response["Status"] = "sucesso"
    response["Dados"] = pagamentosConsultas()
    response["Mensagem"] =  'total de lucros'
    return jsonify(response)