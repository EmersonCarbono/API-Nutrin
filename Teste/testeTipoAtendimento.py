import requests as Req

url_padrao = "http://127.0.0.1:5000"

def TesteCreateTipoAtendimento(nome, preco, qtdRetorno):
    url = url_padrao + "/tipo-atendimento/cadastrar"
    tipoAtendimento = {
        "nome" : nome,
        "preco" : preco,
        "qtdRetorno" : qtdRetorno
        }
    Dados = Req.api.post(url, json=tipoAtendimento).json()
    return Dados

def TestebuscarTipoAtendimento(id_atual = None):
    url = url_padrao + "/tipo-atendimento/buscar"
    dados = {
        "id_atual": id_atual
    }
    Dados = Req.api.post(url, json=dados).json()
    return Dados

def TesteupdateTipoAtendimento(id_atendiemnto, nome, preco, qtdRetorno):
    url = url_padrao + "/tipo-atendimento/alterar"
    tipoAtendimento = {
        "id_atendiemnto" : id_atendiemnto,
        "nome" : nome,
        "preco" : preco,
        "qtdRetorno" : qtdRetorno
        }
    Dados = Req.api.post(url, json=tipoAtendimento).json()
    return Dados


def main():
    #print(TesteCreateTipoAtendimento("Vip", 500, 3))
    #print(TestebuscarTipoAtendimento())
    #print(TestebuscarTipoAtendimento(2))
    print(TesteupdateTipoAtendimento(1, 'vip', 100, 2))
main() 


