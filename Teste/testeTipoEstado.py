import requests as Req

url_padrao = 'http://127.0.0.1:5000'

def testeCadastrarUser(nome):
    url = url_padrao + "/tipo-estado/cadastrar"
    tipoEstado = {
        "nome" : nome
    }
    Dados = Req.api.post(url, json=tipoEstado).json()
    return Dados


def main():
    testeCadastrarUser("aprovado")

main()